import streamlit as st
import os

from core.scripts import user_repository, utils as core_utils
from answer_task.common import logic, utils

if "qualification_progress" not in st.session_state:
    st.session_state.qualification_progress = user_repository.get_checkpoint("qualification") or 1
st.session_state.page = "answer_task_qualification_page_sample" + str(st.session_state.qualification_progress)

# Check qualification status
user_qualification = user_repository.get_qualification()

# If failed, show reset and force pass buttons
if user_qualification == -1:
    st.warning("⚠️ Sie haben den Qualifikationstest bereits versucht und nicht bestanden.")
    
    st.markdown("### Optionen für Test-Modus:")
    
    col1, col2 = st.columns(2)
    
    # seems to be the same as on qualification_page?
    with col1:
        if st.button("🔄 Reset", use_container_width=True):
            try:
                # qualification 0 -> neither qualified nor unqualified
                user_repository.set_qualification(st.session_state.user_id, 0)
                # set the index-tracking qualification progress back to 1
                st.session_state["qualification_progress"] = 1
                # remove the annotations done so far for a proper reset
                user_repository.reset_annotation(st.session_state.user_id, key="qualification")
                st.rerun()  # reload (probably necessary)
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col2:
        if st.button("✅ Force Pass", use_container_width=True):
            try:
                # qualification 1 -> qualified
                user_repository.set_qualification(st.session_state.user_id, 1)
                st.rerun()  # reload page to go back to the beginning of the script and show the "bestanden" message
            except Exception as e:
                st.error(f"Error: {e}")
    
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
    
    samples = core_utils.read_json_from_file(core_utils.TASK_INFO["answer_task"]["qualification_filepath"])

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
