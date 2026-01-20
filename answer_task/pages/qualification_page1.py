import streamlit as st
import os

from core.scripts import user_repository, utils as core_utils
from german_answer_task.common import logic, utils

if "qualification_progress" not in st.session_state:
    st.session_state.qualification_progress = user_repository.get_checkpoint("qualification") or 1
st.session_state.page = "german_answer_task_qualification_page_sample" + str(st.session_state.qualification_progress)

# Check qualification status
user_qualification = user_repository.get_qualification()

if user_qualification == 1:
    st.markdown("\n## ✅ Sie haben den Qualifikationstest bestanden! \n\n Wählen Sie **Annotation** in der Navigationsleiste, um mit der Annotation zu beginnen.")
elif user_qualification == -1:
    st.markdown("\n## ❌ Sie haben den Qualifikationstest nicht bestanden. \n\n")
    prolific_code = os.getenv("PROLIFIC_SCREENOUT_CODE", "COMPLETION123")
    st.markdown(f"## Ihr Completion-Code: {prolific_code}")
else:
    # Get current index
    index = int(st.session_state.qualification_progress)

    if index == 1:
        st.write("## 📝 Qualifikationstest - Direct/Indirect Classification")
        st.write("**Sie müssen 8 von 10 Fragen richtig beantworten.**")
        st.info("💡 Tipp: Lesen Sie die Einführung, bevor Sie beginnen!")
        st.markdown("---")

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
        core_utils.handle_next_button(annotation, index, samples, "qualification", logic.check_if_qualified)

    if back_button:
        core_utils.handle_back_button(annotation, index, samples, "qualification")
