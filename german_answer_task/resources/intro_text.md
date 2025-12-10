# Direct vs. Indirect Answer Classification Task

## Overview

This task evaluates your ability to distinguish between **direct** and **indirect responses** in German conversations.
ii
You will see German conversational exchanges with:
- **Context**: The situation of the conversation
- **Question**: A question Person X asks Person Y  
- **Response**: Person Y's answer

Your task: Classify whether the response is **Direct** or **Indirect**.

---

## What is a Direct Answer?

A **direct answer** explicitly and immediately answers the question.

**Examples:**

**Example 1:**
- **Context:** X möchte wissen, welche Aktivitäten Y am Wochenende gerne macht.
- **Question:** Bist du letzten Wochenende irgendwo hingegangen?
- **Response:** Ich war irgendwo am letzten Wochenende.
- **Classification:** Direct answer

**Example 2:**
- **Context:** X möchte wissen, was Y für Musik vorzieht.
- **Question:** Magst du Rock?
- **Response:** Ich mag Rock.
- **Classification:** Direct answer

---

## What is an Indirect Answer?

An **indirect answer** does not directly answer the question. Instead, it:
- Provides related information
- Implies the answer through context
- Avoids the question
- Suggests an alternative

**Examples:**

**Example 1:**
- **Question:** Ist deine Arbeit körperlich anstrengend?
- **Response:** Meine Position erforderte, dass ich den ganzen Tag vor dem Computer saß.
- **Classification:** Indirect answer (describes the work but doesn't directly say yes/no)

**Example 2:**
- **Context:** Y hat X gerade gesagt, dass er überlegt, seinen Job zu wechseln.
- **Question:** Möchten Sie eine Show sehen?
- **Response:** Lass uns in einer Bar betrinken.
- **Classification:** Indirect answer (suggests alternative instead of answering the question)

**Example 3:**
- **Context:** X und Y sind Kollegen, die am Freitag gleichzeitig von der Arbeit ablassen.
- **Question:** Magst du Käseburger?
- **Response:** Nur von Burger King.
- **Classification:**  Indirect answer (gives specific condition instead of yes/no)

---

## Guidelines

### Key Points:
1. **Focus on whether the question is explicitly answered**
2. **Direct = Clear yes/no or direct information**
3. **Indirect = Related info, implications, or alternatives**

### Tips:
- Read the context carefully
- Ask yourself: "Is the question explicitly answered?"
- If you need to interpret or read between the lines → likely indirect
- Take your time - quality matters

---

## The Task

### Qualification Test
- **10 questions**
- **Need 8/10 correct to pass**
- Filters for quality annotators

### Main Annotation  
- **100 examples total**
- **~2 minutes per example**
- **Progress saved automatically**

For each example, you will:
1. Read the context, question, and response
2. Select: Direct answer OR Indirect answer
3. Rate your confidence (1-5)
4. Add optional notes

---

## Dataset Information

This task uses 100 examples from the **Circa dataset**, balanced between direct and indirect answers. The data evaluates language models' capability to understand user intentions in dialogue systems.

---

**Ready to start? Click "Qualification" in the sidebar!**
