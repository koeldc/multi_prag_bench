import streamlit as st
import os

from core.scripts import user_repository, utils as core_utils
from german_answer_task.common import logic, utils

if "qualification_progress" not in st.session_state:
    st.session_state.qualification_progress = user_repository.get_checkpoint("qualification") or 1
st.session_state.page = "german_answer_task_qualification_page_sample" + str(st.session_state.qualification_progress)

# Check qualification status
user_qualification = user_repository.get_qualification()

# If failed, show reset and force pass buttons
if user_qualification == -1:
    st.warning("⚠️ Sie haben den Qualifikationstest bereits versucht und nicht bestanden.")
    
    st.markdown("### Optionen für Test-Modus:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Qualifikation zurücksetzen", use_container_width=True):
            try:
                conn = st.session_state.conn
                cursor = conn.cursor()
                
                # Find all tables
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                
                found = False
                for table in cursor.fetchall():
                    table_name = table[0]
                    try:
                        cursor.execute(f"""
                            UPDATE {table_name} 
                            SET qualification = 0 
                            WHERE user_id = %s
                        """, (st.session_state.user_id,))
                        
                        if cursor.rowcount > 0:
                            conn.commit()
                            cursor.close()
                            
                            # Reset session state
                            if 'qualification_progress' in st.session_state:
                                del st.session_state.qualification_progress
                            
                            st.success("✅ Zurückgesetzt!")
                            found = True
                            import time
                            time.sleep(0.5)
                            st.rerun()
                            break
                    except:
                        continue
                
                if not found:
                    st.error("Tabelle nicht gefunden")
                cursor.close()
                    
            except Exception as e:
                st.error(f"Fehler: {e}")
    
    with col2:
        if st.button("✅ Qualifikation erzwingen (Pass)", use_container_width=True):
            try:
                conn = st.session_state.conn
                cursor = conn.cursor()
                
                # Find all tables
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                
                found = False
                for table in cursor.fetchall():
                    table_name = table[0]
                    try:
                        cursor.execute(f"""
                            UPDATE {table_name} 
                            SET qualification = 1 
                            WHERE user_id = %s
                        """, (st.session_state.user_id,))
                        
                        if cursor.rowcount > 0:
                            conn.commit()
                            cursor.close()
                            st.success("✅ Qualifikation bestanden!")
                            found = True
                            import time
                            time.sleep(0.5)
                            st.rerun()
                            break
                    except:
                        continue
                
                if not found:
                    st.error("Tabelle nicht gefunden")
                cursor.close()
                    
            except Exception as e:
                st.error(f"Fehler: {e}")
    
    st.markdown("---")
    prolific_code = os.getenv("PROLIFIC_SCREENOUT_CODE", "CF2QBA7L")
    st.markdown(f"**Completion-Code:** {prolific_code}")
    st.caption("Kopieren Sie diesen Code in Prolific.")

elif user_qualification == 1:
    st.markdown("## ✅ Sie haben den Qualifikationstest bestanden!")
    st.success("Wählen Sie **Annotation** in der Navigationsleiste, um mit der Annotation zu beginnen.")
    st.balloons()

else:
    # Qualification in progress
    index = int(st.session_state.qualification_progress)

    if index == 1:
        st.write("## 📝 Qualifikationstest - Direct/Indirect Classification")
        st.write("**Sie müssen 8 von 10 Fragen richtig beantworten.**")
        st.info("💡 Tipp: Lesen Sie die Einführung, bevor Sie beginnen!")
        st.info("🧪 **Test-Modus aktiv:** Alle Antworten werden als richtig gewertet.")
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
        if index == 10:
            # Last question - check qualification (auto-pass in test mode)
            st.info("⏳ Bewertung Ihrer Antworten...")
            core_utils.handle_next_button(annotation, index, samples, "qualification", logic.check_if_qualified)
        else:
            # Questions 1-9 - just save and continue
            core_utils.handle_next_button(annotation, index, samples, "qualification", None)

    if back_button:
        core_utils.handle_back_button(annotation, index, samples, "qualification")
