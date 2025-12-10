"""
Database utilities for German Answer Task
"""
import streamlit as st
import json

# letting copilot handle the database is dangerous.
'''
def save_annotation_safe(user_id, index, annotation):
    """
    Safely save annotation to database with proper error handling.
    
    Args:
        user_id: User ID
        index: Sample index (1-based)
        annotation: Annotation dict with classification, confidence, comment
    """
    conn = st.session_state.conn
    cursor = None
    
    try:
        cursor = conn.cursor()
        
        # Find the user data table
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        
        tables = [t[0] for t in cursor.fetchall()]
        
        # Find table with user_id column
        user_table = None
        for table in tables:
            try:
                cursor.execute(f"""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name = %s AND column_name = 'user_id'
                """, (table,))
                if cursor.fetchone():
                    user_table = table
                    break
            except:
                continue
        
        if not user_table:
            print(f"[ERROR] No user table found")
            conn.rollback()
            return False
        
        print(f"[DEBUG] Using table: {user_table}")
        
        # Check if german_answer_annotations column exists
        cursor.execute(f"""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = %s AND column_name = 'german_answer_annotations'
        """, (user_table,))
        
        if not cursor.fetchone():
            # Add column
            print(f"[DEBUG] Adding german_answer_annotations column to {user_table}")
            cursor.execute(f"""
                ALTER TABLE {user_table} 
                ADD COLUMN german_answer_annotations TEXT
            """)
            conn.commit()
        
        # Get current annotations
        cursor.execute(f"""
            SELECT german_answer_annotations 
            FROM {user_table} 
            WHERE user_id = %s
        """, (user_id,))
        
        result = cursor.fetchone()
        
        if result and result[0]:
            # Parse existing annotations
            try:
                annotations = json.loads(result[0])
            except:
                annotations = {}
        else:
            annotations = {}
        
        # Save this annotation
        annotations[str(index)] = {
            "classification": annotation["classification"],
            "confidence": annotation["confidence"],
            "comment": annotation["comment"],
            "question_id": annotation["question"]
        }
        
        # Update database
        cursor.execute(f"""
            UPDATE {user_table}
            SET german_answer_annotations = %s
            WHERE user_id = %s
        """, (json.dumps(annotations), user_id))
        
        rows_updated = cursor.rowcount
        
        if rows_updated == 0:
            print(f"[WARNING] No rows updated for user_id: {user_id}")
        
        conn.commit()
        
        print(f"[SUCCESS] Saved annotation for sample {index} (total: {len(annotations)} annotations)")
        
        if cursor:
            cursor.close()
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Failed to save annotation: {e}")
        import traceback
        traceback.print_exc()
        
        # CRITICAL: Rollback the failed transaction
        try:
            conn.rollback()
            print("[DEBUG] Transaction rolled back")
        except:
            pass
        
        if cursor:
            try:
                cursor.close()
            except:
                pass
        
        return False
'''