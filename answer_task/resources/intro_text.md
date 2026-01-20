# Direct vs. Indirect Answer Classification Task

## Overview

This task evaluates your ability to distinguish between **direct** and **indirect responses** in conversations.

You will see conversational exchanges with:
- **Context**: The situation of the conversation
- **Question**: A question Person X asks Person Y  
- **Response**: Person Y's answer

Your task: Classify whether the response is **Direct** or **Indirect**.

---

## What is a Direct Answer?

A **direct answer** explicitly and immediately answers the question.

**Examples:**

**Example 1 (German):**
- **Context:** X will wissen, welche Musik Y bevorzugt.
- **Question:** Magst du Rock?
- **Response:** Ich mag Rock.
- **Classification:** Direct answer

**Example 2 (Hindi):**
- **Context:** Y अभी-अभी एक पड़ोस में आया है और अपने नए पड़ोसी X से मिलता है।
- **Question:** क्या आप यहाँ रहने का आनंद ले रहे हैं?
- **Response:** मैं यहाँ रहने का आनंद ले रहा हूँ.
- **Classification:** Direct answer

**Example 3 (Chinese):**
- **Context:** X和Y是小时候的邻居, 在咖啡馆突然碰到对方.
- **Question:** 我可以给你买一杯吗?
- **Response:** 你可以给我买一杯.
- **Classification:** Direct answer

---

## What is an Indirect Answer?

An **indirect answer** does not directly answer the question. Instead, it:
- Provides related information
- Implies the answer through context
- Avoids the question
- Suggests an alternative

**Examples:**

**Example 1 (German):**
- **Context:** Y ist gerade in eine Nachbarschaft gezogen und trifft seinen/ihren neuen Nachbarn X.
- **Question:** Haben Sie ein Haustier?
- **Response:** Wir haben neun Hunde.
- **Classification:** Indirect answer (gives specific information instead of yes/no)

**Example 2 (Hindi):**
- **Context:** Y ने अभी X को बताया है कि वह न्यूयॉर्क में एक फ्लैट खरीदने के बारे में सोच रहा है।
- **Question:** जब आप संपत्ति पर बंद हो जाएगा?
- **Response:** हम अभी बातचीत कर रहे हैं।
- **Classification:** Indirect answer (describes current status instead of answering when)

**Example 3 (Chinese):**
- **Context:** X想知道Y喜欢阅读什么类型的书籍.
- **Question:** 你喜欢短篇故事吗?
- **Response:** 如果我只有一点点的时间来阅读.
- **Classification:** Indirect answer (gives conditional response instead of yes/no)

**Example 4 (German):**
- **Context:** Y hat X gerade mitgeteilt, dass er/sie erwägt, seinen/ihren Job zu wechseln.
- **Question:** Sollte die neue Firma in der Nähe des Wohnortes ansässig sein?
- **Response:** Je näher, desto besser.
- **Classification:** Indirect answer (gives preference instead of yes/no)

**Example 5 (Hindi):**
- **Context:** Y अभी-अभी एक पड़ोस में आया है और अपने नए पड़ोसी X से मिलता है।
- **Question:** क्या आपके पास कोई पालतू जानवर है?
- **Response:** हमारे पास नौ कुत्ते हैं।
- **Classification:** Indirect answer (gives specific information instead of yes/no)

**Example 6 (Chinese):**
- **Context:** 他刚刚告诉我他正在考虑在纽约买一套公寓.
- **Question:** 什么时候你会关闭财产?
- **Response:** 我们现在正在谈判.
- **Classification:** Indirect answer (describes current status instead of answering when)

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
- **7 questions**
- **Need 5/7 correct to pass**
- Filters for quality annotators

### Main Annotation  
- **25 examples total**
- **~2 minutes per example**
- **Progress saved automatically**

For each example, you will:
1. Read the context, question, and response
2. Select: Direct answer OR Indirect answer
3. Rate your confidence (1-5)
4. Add optional notes

---

## Dataset Information

This task uses examples from the **Circa dataset**, balanced between direct and indirect answers. The data evaluates language models' capability to understand user intentions in dialogue systems.

---

**Ready to start? Click "Qualification" in the sidebar!**

