import os
import streamlit as st

from core.scripts import user_repository
from core.scripts.utils import read_json_from_file, handle_next_button, handle_back_button, TASK_INFO, skip_to_next_sample
from german_answer_task.common import utils

samples = read_json_from_file(TASK_INFO["german_answer_task"]["annotation_filepath"])

if "progress" not in st.session_state:
    st.session_state.progress = user_repository.get_checkpoint("annotation")
    if not st.session_state.progress:
        st.session_state.progress = skip_to_next_sample(0, samples, st.session_state.user[3], 1, 
                                                        "annotation", qualification_function=None)
st.session_state.page = "german_answer_task_annotation_page_sample" + str(st.session_state.progress)

if user_repository.get_qualification() != 1:
    st.write("## Sie müssen die Qualifikation bestehen, bevor Sie mit der Annotation beginnen können.")
    st.info("👈 Wählen Sie **'Qualification'** in der Seitenleiste.")
elif user_repository.check_if_done(st.session_state.user_id):
    st.write("## Sie haben die Annotation abgeschlossen!")
    st.write("Vielen Dank für Ihre Zeit!")
    st.balloons()
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
        handle_next_button(annotation, index, samples, "annotation")

    if back_button:
        handle_back_button(annotation, index, samples, "annotation")
