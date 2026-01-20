"""
Qualification logic for German Direct/Indirect Classification Task
"""


def check_if_qualified(annotations):
    """
    Check if user passed qualification (need 8/10 correct).
    
    Args:
        annotations: List of user annotations from database
        
    Returns:
        bool: True if qualified (>= 8/10 correct)
    """
    import json
    
    print(f"[DEBUG] Received {len(annotations)} annotations")
    
    # Handle empty annotations
    if not annotations or len(annotations) == 0:
        print("[ERROR] No annotations found!")
        return False
    
    # Load qualification samples
    with open("german_answer_task/resources/qualification_questions.json", "r") as f:
        samples = json.load(f)
    
    correct_count = 0
    total_count = len(annotations)
    
    for i, annotation in enumerate(annotations):
        question_key = str(i + 1)
        
        print(f"[DEBUG] Processing annotation {i}: type={type(annotation)}")
        
        # Parse annotation if it's a JSON string
        if isinstance(annotation, str):
            try:
                annotation = json.loads(annotation)
                print(f"[DEBUG] Parsed to: {annotation}")
            except Exception as e:
                print(f"[ERROR] Could not parse annotation: {annotation}, error: {e}")
                continue
        
        if question_key in samples:
            user_answer = annotation.get("classification", "")
            correct_answer = samples[question_key].get("correct_answer", "")
            
            match = user_answer == correct_answer
            print(f"[DEBUG] Q{question_key}: user='{user_answer}', correct='{correct_answer}', match={match}")
            
            if match:
                correct_count += 1
        else:
            print(f"[WARNING] Question key {question_key} not found in samples")
    
    # Need at least 8 out of 10 correct
    passed = correct_count >= 8
    
    print(f"[Qualification] Score: {correct_count}/{total_count} - {'PASSED' if passed else 'FAILED'}")
    
    return passed

