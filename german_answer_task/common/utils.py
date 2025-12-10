import streamlit as st
from core.scripts.utils import read_json_from_file, TASK_INFO


def print_annotation_schema(mode, index):
    """
    Display the annotation interface for German direct/indirect classification.
    
    Args:
        mode: "qualification" or "annotation"
        index: Current sample index (1-based)
        
    Returns:
        tuple: (question_id, classification, confidence, comment, next_button_clicked)
    """
    
    # Load appropriate data
    if mode == "qualification":
        samples = read_json_from_file(TASK_INFO["german_answer_task"]["qualification_filepath"])
        # Qualification is a dict with string keys: {"1": {...}, "2": {...}}
        sample = samples[str(index)]
    else:
        samples = read_json_from_file(TASK_INFO["german_answer_task"]["annotation_filepath"])
        # Annotation is a list of dicts from JSONL: [{...}, {...}, ...]
        sample = samples[index - 1]  # index is 1-based, list is 0-based
    
    # Display sample info
    st.markdown(f"### 📝 Sample {index} von {len(samples)}")
    st.markdown("---")
    
    # Parse and display the pretext
    pretext = sample["pretext"]
    
    # Split by newlines and display with formatting
    lines = pretext.strip().split('\\n')
    for line in lines:
        if line.startswith('Context:'):
            st.markdown(f"**{line}**")
        elif line.startswith('Question:'):
            st.markdown(f"**{line}**")
        elif line.startswith('Response:'):
            st.markdown(f"**{line}**")
        elif line.strip():  # Non-empty line
            st.markdown(line)
    
    st.markdown("---")
    
    # Get question ID
    question_id = sample.get("id", str(index))
    
    # Classification section
    st.markdown("### 🎯 Ihre Annotation")
    
    classification = st.radio(
        "**Klassifizierung:**",
        options=["Direct answer", "Indirect answer"],
        key=f"{mode}_class_{index}",
        help="Wird die Frage explizit beantwortet?"
    )
    
    # Confidence slider
    st.markdown("**Konfidenz:**")
    confidence = st.select_slider(
        "Wie sicher sind Sie?",
        options=[1, 2, 3, 4, 5],
        value=3,
        key=f"{mode}_conf_{index}",
        format_func=lambda x: ["😟 Sehr unsicher", "😕 Unsicher", "😐 Neutral", "🙂 Sicher", "😀 Sehr sicher"][x-1]
    )
    
    # Optional comment
    comment = st.text_area(
        "**Anmerkungen (optional):**",
        key=f"{mode}_comment_{index}",
        placeholder="Notizen, Unsicherheiten, Beobachtungen...",
        height=80
    )
    
    # Next button
    st.markdown("---")
    next_input = st.button(
        label="Weiter →",
        key=f"{mode}_next_{index}",
        type="primary",
        use_container_width=True
    )
    
    # Sidebar quick reference
    with st.sidebar:
        st.markdown("---")
        st.markdown("### 📖 Schnellreferenz")
        
        with st.expander("✅ Direct Answer"):
            st.markdown("""
            - Explizite Antwort
            - Klares Ja/Nein
            - Direkte Information
            
            **Beispiel:**
            - F: "Magst du Rock?"
            - A: "Ich mag Rock."
            """)
        
        with st.expander("❌ Indirect Answer"):
            st.markdown("""
            - Implizite Antwort
            - Verwandte Info
            - Alternative/Ausweichung
            
            **Beispiel:**
            - F: "Magst du Käseburger?"
            - A: "Nur von Burger King."
            """)
        
        st.markdown("---")
        st.markdown("### 💡 Tipps")
        st.caption("• Lesen Sie sorgfältig")
        st.caption("• Frage explizit beantwortet?")
        st.caption("• Interpretation nötig? → Indirekt")
    
    return question_id, classification, confidence, comment, next_input
