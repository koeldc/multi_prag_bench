import os
import streamlit as st

from core.scripts import user_repository
from core.scripts.utils import read_json_from_file, handle_next_button, handle_back_button, TASK_INFO, skip_to_next_sample
from german_answer_task.common import utils

samples = read_json_from_file(TASK_INFO["german_answer_task"]["annotation_filepath"])

if "progress" not in st.session_state:
    st.session_state.progress = user_repository.get_checkpoint("annotation")
    if not st.session_state.progress:  # no checkpoint yet -> simply go to the first relevant sample
        st.session_state.progress = skip_to_next_sample(0, samples, st.session_state.user[3], 1, 
                                                        "annotation", qualification_function=None)
st.session_state.page = "german_answer_task_annotation_page_sample" + str(st.session_state.progress)

# BOTH CHECKS DISABLED FOR TEST MODE
if 0:  # Qualification check disabled
    st.write("## Sie müssen die Qualifikation bestehen, bevor Sie mit der Annotation beginnen können. \n\n Wählen Sie **Qualification** in der Navigationsleiste links, um den Qualifikationstest zu absolvieren.")
elif 0:  # Done check disabled
    st.write("## Sie haben die Annotation abgeschlossen. \n\nVielen Dank für Ihre Zeit!")
    st.write("\n\n\n")
else:
    index = int(st.session_state.progress)

    back_button = st.button(label="Zurück", key=10 * index + 7, help="Zurück zum vorherigen Sample.")

    question, classification, confidence, comment, next_input = utils.print_annotation_schema("annotation", index)
    
    annotation = {
        "question": question,
        "classification": classification,
        "confidence": confidence,
        "comment": comment
    }

    if next_input:
	if st.session_state.conn is None:
		st.session_state.progress = min(index + 1, len(samples))
                st.rerun()
	else:
		handle_next_button(annotation, index, samples, "annotation")
    if back_button:
        if st.session_state.conn is None:
            # Test mode: just go back without saving
            st.session_state.progress = max(index - 1, 1)
            st.rerun()
        else:
            handle_back_button(annotation, index, samples, "annotation")
        handle_next_button(annotation, index, samples, "annotation")

    #if back_button:
    #    handle_back_button(annotation, index, samples, "annotation")
