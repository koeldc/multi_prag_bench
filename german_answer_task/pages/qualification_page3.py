import streamlit as st
import os

from core.scripts import user_repository, utils as core_utils
from german_answer_task.common import logic, utils

if "qualification_progress" not in st.session_state:
    st.session_state.qualification_progress = user_repository.get_checkpoint("qualification") or 1
st.session_state.page = "german_answer_task_qualification_page_sample" + str(st.session_state.qualification_progress)

# Check qualification status
user_qualification = user_repository.get_qualification()

# If failed, show reset button for testing
if user_qualification == -1:
    st.warning("⚠️ Sie haben den Qualifikationstest bereits versucht und nicht bestanden.")
    
    # Reset button with automatic table detection
    if st.button("🔄 Qualifikation zurücksetzen und erneut versuchen"):
        try:
            conn = st.session_state.conn
            cursor = conn.cursor()
            
            # Find all tables in database
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            tables = cursor.fetchall()
            
            # Find the table with user_id and qualification columns
            found = False
            for table in tables:
                table_name = table[0]
                try:
                    # Check if this table has both columns
                    cursor.execute(f"""
                        SELECT column_name 
                        FROM information_schema.columns 
                        WHERE table_name = %s
                        AND column_name IN ('user_id', 'qualification')
                    """, (table_name,))
                    cols = [c[0] for c in cursor.fetchall()]
                    
                    if 'user_id' in cols and 'qualification' in cols:
                        st.info(f"✅ Tabelle gefunden: {table_name}")
                        
                        # Update qualification using parameterized query
                        query = f"UPDATE {table_name} SET qualification = 0 WHERE user_id = %s"
                        cursor.execute(query, (st.session_state.user_id,))
                        
                        rows_updated = cursor.rowcount
                        conn.commit()
                        
                        if rows_updated > 0:
                            st.success(f"✅ Qualifikation zurückgesetzt! Seite wird neu geladen...")
                            found = True
                            import time
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.warning(f"⚠️ Keine Zeilen gefunden für user_id: {st.session_state.user_id}")
                        break
                        
                except Exception as e:
                    continue
            
            if not found:
                st.error("❌ Keine passende Tabelle gefunden.")
                st.info("Verfügbare Tabellen: " + str([t[0] for t in tables]))
            
            cursor.close()
            
        except Exception as e:
            st.error(f"Fehler: {e}")
    
    st.markdown("---")
    prolific_code = os.getenv("PROLIFIC_SCREENOUT_CODE", "CF2QBA7L")
    st.markdown(f"## Ihr Completion-Code: {prolific_code}")
    st.info("Kopieren Sie diesen Code in Prolific.")

elif user_qualification == 1:
    st.markdown("## ✅ Sie haben den Qualifikationstest bestanden!")
    st.markdown("Wählen Sie **Annotation** in der Navigationsleiste, um mit der Annotation zu beginnen.")
    st.balloons()

else:
    # Qualification in progress
    index = int(st.session_state.qualification_progress)

    if index == 1:
        st.write("## 📝 Qualifikationstest - Direct/Indirect Classification")
        st.write("**Sie müssen 8 von 10 Fragen richtig beantworten.**")
        st.info("💡 Tipp: Lesen Sie die Einführung, bevor Sie beginnen!")
        st.markdown("---")

    # Display current question number
    st.caption(f"Frage {index} von 10")

    back_button = st.button(label="← Zurück", key=10 * index + 7)

    # Display annotation interface
    question, classification, confidence, comment, next_input = utils.print_annotation_schema("qualification", index)

    annotation = {
        "question": question,
        "classification": classification,
        "confidence": confidence,
        "comment": comment
    }
    
    samples = core_utils.read_json_from_file(core_utils.TASK_INFO["german_answer_task"]["qualification_filepath"])

    if next_input:
        # Only check qualification after completing all 10 questions
        if index == 10:
            # Last question - save and check if qualified
            st.info("⏳ Bewertung Ihrer Antworten...")
            core_utils.handle_next_button(annotation, index, samples, "qualification", logic.check_if_qualified)
        else:
            # Questions 1-9 - just save and continue
            core_utils.handle_next_button(annotation, index, samples, "qualification", None)

    if back_button:
        core_utils.handle_back_button(annotation, index, samples, "qualification")
