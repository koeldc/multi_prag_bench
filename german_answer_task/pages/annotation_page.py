import os
import streamlit as st

from core.scripts import user_repository, utils as core_utils
from core.scripts.utils import read_json_from_file, TASK_INFO, skip_to_next_sample
from german_answer_task.common import utils, database_utils

samples = read_json_from_file(TASK_INFO["german_answer_task"]["annotation_filepath"])

if "progress" not in st.session_state:
    st.session_state.progress = user_repository.get_checkpoint("annotation")
    if not st.session_state.progress:
        st.session_state.progress = skip_to_next_sample(0, samples, st.session_state.user[3], 1, 
                                                        "annotation", qualification_function=None)
st.session_state.page = "german_answer_task_annotation_page_sample" + str(st.session_state.progress)

# Check qualification
if user_repository.get_qualification() != 1:
    st.write("## Sie müssen die Qualifikation bestehen, bevor Sie mit der Annotation beginnen können.")
    st.info("👈 Wählen Sie **'Qualification'** in der Seitenleiste.")
elif False:  # DISABLED
    st.write("## Sie haben die Annotation abgeschlossen!")
    st.balloons()
else:
    # Main annotation interface
    index = int(st.session_state.progress)
    
    # Show progress
    total = len(samples)
    st.progress(index / total if total > 0 else 0)
    st.caption(f"Sample {index} von {total}")

    back_button = st.button(label="← Zurück", key=10 * index + 7)

    question, classification, confidence, comment, next_input = utils.print_annotation_schema("annotation", index)
    
    annotation = {
        "question": question,
        "classification": classification,
        "confidence": confidence,
        "comment": comment
    }

    if next_input:
        # the normal script should work fine
        core_utils.handle_next_button(annotation, index, samples, "annotation", None)
        
        if index >= len(samples):
            st.info("🎉 Alle Samples annotiert!")

    if back_button:
        # Go back
        # a properly working back button is deceptively complex, so use the function here too
        core_utils.handle_back_button(annotation, index, samples, "annotation")
