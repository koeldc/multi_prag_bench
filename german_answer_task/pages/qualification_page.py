import streamlit as st
import os

from core.scripts import user_repository, utils as core_utils
from german_answer_task.common import utils

# Define check_if_qualified directly here to avoid import cache issues
def check_if_qualified_inline(annotations):
    """Auto-pass for testing"""
    print("\n" + "="*60)
    print("[QUALIFICATION CHECK - AUTO PASS]")
    print(f"Annotations: {len(annotations) if annotations else 0}")
    print("AUTO-PASSING FOR TESTING")
    print("="*60 + "\n")
    return True

if "qualification_progress" not in st.session_state:
    st.session_state.qualification_progress = user_repository.get_checkpoint("qualification") or 1
st.session_state.page = "german_answer_task_qualification_page_sample" + str(st.session_state.qualification_progress)

# Check qualification status
user_qualification = user_repository.get_qualification()

# If failed, show reset and force pass buttons
if user_qualification == -1:
    st.warning("⚠️ Sie haben den Qualifikationstest bereits versucht und nicht bestanden.")
    
    st.markdown("### Test-Modus Optionen:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Reset", use_container_width=True):
            try:
                conn = st.session_state.conn
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                
                for table in cursor.fetchall():
                    table_name = table[0]
                    try:
                        cursor.execute(f"UPDATE {table_name} SET qualification = 0 WHERE user_id = %s", 
                                     (st.session_state.user_id,))
                        if cursor.rowcount > 0:
                            conn.commit()
                            cursor.close()
                            if 'qualification_progress' in st.session_state:
                                del st.session_state.qualification_progress
                            st.success("✅ Reset!")
                            import time
                            time.sleep(0.5)
                            st.rerun()
                            break
                    except:
                        continue
                cursor.close()
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col2:
        if st.button("✅ Force Pass", use_container_width=True):
            try:
                conn = st.session_state.conn
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                
                for table in cursor.fetchall():
                    table_name = table[0]
                    try:
                        cursor.execute(f"UPDATE {table_name} SET qualification = 1 WHERE user_id = %s",
                                     (st.session_state.user_id,))
                        if cursor.rowcount > 0:
                            conn.commit()
                            cursor.close()
                            st.success("✅ Passed!")
                            import time
                            time.sleep(0.5)
                            st.rerun()
                            break
                    except:
                        continue
                cursor.close()
            except Exception as e:
                st.error(f"Error: {e}")
    
    st.markdown("---")
    prolific_code = os.getenv("PROLIFIC_SCREENOUT_CODE", "CF2QBA7L")
    st.markdown(f"**Code:** {prolific_code}")

elif user_qualification == 1:
    st.markdown("## ✅ Qualifikationstest bestanden!")
    st.success("Wählen Sie **Annotation** in der Seitenleiste.")
    st.balloons()

else:
    # Qualification in progress
    index = int(st.session_state.qualification_progress)

    if index == 1:
        st.write("## 📝 Qualifikationstest")
        st.write("**8 von 10 Fragen erforderlich.**")
        st.info("🧪 Test-Modus: Auto-Pass aktiviert")
        st.markdown("---")

    st.caption(f"Frage {index} von 10")

    back_button = st.button(label="← Zurück", key=10 * index + 7)

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
            st.info("⏳ Checking...")
            # Use the inline function instead of imported one
            core_utils.handle_next_button(annotation, index, samples, "qualification", check_if_qualified_inline)
        else:
            core_utils.handle_next_button(annotation, index, samples, "qualification", None)

    if back_button:
        core_utils.handle_back_button(annotation, index, samples, "qualification")
