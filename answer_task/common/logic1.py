"""
Qualification logic for German Direct/Indirect Classification Task
"""


def check_if_qualified(annotations, samples):
    """
    Check if user passed qualification (need 8/10 correct).
    
    Args:
        annotations: List of user annotations
        samples: Dict of qualification samples {"1": {...}, "2": {...}, ...}
        
    Returns:
        bool: True if qualified (>= 8/10 correct)
    """
    
    correct_count = 0
    total_count = len(annotations)
    for 
    for i, annotation in enumerate(annotations, 1):  # Start from 1
        sample_key = str(i)
        
        if sample_key in samples:
            sample = samples[sample_key]
            user_answer = annotation.get("classification", "")
            correct_answer = sample.get("correct_answer", "")
            
            if user_answer == correct_answer:
                correct_count += 1
    
    # Need at least 8 out of 10 correct
    passed = correct_count >= 8
    
    print(f"[Qualification] Score: {correct_count}/{total_count} - {'PASSED' if passed else 'FAILED'}")
    
    return passed
