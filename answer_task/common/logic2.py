import json
"""
Qualification logic for German Direct/Indirect Classification Task
"""

def check_if_qualified(annotations):
    """
    Check if user passed qualification (need 8/10 correct).
    
    Args:
        annotations: List of user annotations
        samples: List of qualification samples (each sample has an "id" field)
        
    Returns:
        bool: True if qualified (>= 8/10 correct)
    """

    with open("german_answer_task/resources/qualification_questions.json", "r") as f:
        samples = json.load(f)
    # Convert samples list into a lookup by ID (int)
    sample_dict = {int(sample["id"]): sample for sample in samples}

    correct_count = 0
    total_count = len(annotations)

    for i, annotation in enumerate(annotations):
        user_answer = annotation.get("classification", "")
        
        # assume annotation index matches sample id 0..N-1
        if i in sample_dict:
            correct_answer = sample_dict[i].get("correct answer", "")
            if user_answer == correct_answer:
                correct_count += 1

    passed = correct_count >= 8

    print(f"[Qualification] Score: {correct_count}/{total_count} - {'PASSED' if passed else 'FAILED'}")

    return passed

