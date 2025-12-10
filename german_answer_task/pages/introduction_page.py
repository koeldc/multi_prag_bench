import streamlit as st

st.session_state.page = "german_answer_task_introduction_page"

# Check if user is logged in
if not st.session_state.user_id:
    st.markdown("""
Note: You are **not logged in** in this tab, so the qualification and annotation task do not show up in the sidebar.  

---
""")

# Main content
st.title("🇩🇪 Direkte vs. Indirekte Antworten - Einführung")

st.markdown("""
## Willkommen zur Annotationsaufgabe!

### Ihre Aufgabe
Sie werden Gesprächsausschnitte auf Deutsch lesen. Für jeden Ausschnitt sehen Sie:
- **Kontext**: Die Situation des Gesprächs
- **Frage**: Eine Frage, die Person X an Person Y stellt
- **Antwort**: Die Antwort von Person Y

Ihre Aufgabe ist es zu bestimmen, ob die Antwort **direkt** oder **indirekt** ist.

---

## Was ist eine direkte Antwort?

Eine **direkte Antwort** beantwortet die Frage explizit und unmittelbar.

### ✅ Beispiele für direkte Antworten:

**Beispiel 1:**
- **Kontext:** X möchte wissen, welche Aktivitäten Y am Wochenende gerne macht.
- **Frage:** Bist du letzten Wochenende irgendwo hingegangen?
- **Antwort:** Ich war irgendwo am letzten Wochenende.
- **Klassifikation:** ✅ **Direct answer** (Die Antwort bestätigt direkt, dass die Person irgendwo war)

**Beispiel 2:**
- **Kontext:** X möchte wissen, was Y für Musik vorzieht.
- **Frage:** Magst du Rock?
- **Antwort:** Ich mag Rock.
- **Klassifikation:** ✅ **Direct answer** (Klare, direkte Bestätigung)

**Beispiel 3:**
- **Kontext:** X und Y sind Kollegen, die am Freitag gleichzeitig von der Arbeit ablassen.
- **Frage:** Hast du heute einen guten Tag gehabt?
- **Antwort:** Ich hatte heute einen schönen Tag.
- **Klassifikation:** ✅ **Direct answer** (Beantwortet die Frage direkt)

---

## Was ist eine indirekte Antwort?

Eine **indirekte Antwort** beantwortet die Frage nicht direkt, sondern:
- Gibt verwandte Informationen
- Impliziert die Antwort durch Kontext
- Weicht der Frage aus
- Gibt eine ausweichende oder tangentiale Antwort

### ❌ Beispiele für indirekte Antworten:

**Beispiel 1:**
- **Kontext:** Y hat X gerade gesagt, dass er überlegt, seinen Job zu wechseln.
- **Frage:** Ist deine Arbeit körperlich anstrengend?
- **Antwort:** Meine Position erforderte, dass ich den ganzen Tag vor dem Computer saß.
- **Klassifikation:** ❌ **Indirect answer** (Beschreibt die Arbeit, sagt aber nicht direkt "Ja" oder "Nein")

**Beispiel 2:**
- **Kontext:** Y ist gerade aus einer anderen Stadt gereist, um X zu treffen.
- **Frage:** Möchten Sie eine Show sehen?
- **Antwort:** Lass uns in einer Bar betrinken.
- **Klassifikation:** ❌ **Indirect answer** (Schlägt Alternative vor statt die Frage direkt zu beantworten)

**Beispiel 3:**
- **Kontext:** Y ist gerade aus einer anderen Stadt gereist, um X zu treffen.
- **Frage:** Willst du in ein Restaurant gehen?
- **Antwort:** Ich will dringend etwas zu essen.
- **Klassifikation:** ❌ **Indirect answer** (Drückt Hunger aus, aber keine direkte Antwort auf die spezifische Frage)

**Beispiel 4:**
- **Kontext:** X und Y sind Kollegen, die am Freitag gleichzeitig von der Arbeit ablassen.
- **Frage:** Magst du Käseburger?
- **Antwort:** Nur von Burger King.
- **Klassifikation:** ❌ **Indirect answer** (Gibt spezifische Bedingung an statt direkt "Ja" oder "Nein" zu sagen)

---

## Wichtige Hinweise

### 🎯 Konzentrieren Sie sich auf:
1. **Explizite vs. implizite Antworten**: Wird die Frage direkt adressiert?
2. **Vollständigkeit**: Beantwortet die Antwort die gestellte Frage vollständig?
3. **Klarheit**: Ist die Antwort eindeutig oder muss man zwischen den Zeilen lesen?

### ⚠️ Häufige Fallstricke:
- Eine Antwort kann positiv oder negativ sein und trotzdem **direkt** sein
- Eine verwandte Information bedeutet nicht automatisch eine direkte Antwort
- Achten Sie auf den genauen Wortlaut der Frage

### 💡 Tipps:
- Lesen Sie den Kontext sorgfältig
- Fragen Sie sich: "Wird die Frage explizit beantwortet?"
- Wenn Sie unsicher sind, denken Sie: "Muss ich raten oder interpretieren, was die Person meint?" → Dann ist es wahrscheinlich indirekt
- Nehmen Sie sich Zeit - Qualität ist wichtiger als Geschwindigkeit

---

## Nächste Schritte

1. ✅ Lesen Sie diese Richtlinien sorgfältig
2. 📝 Absolvieren Sie den Qualifikationstest (10 Fragen)
3. 🎯 Beginnen Sie mit der Hauptaufgabe

""")

st.info("📝 **Bereit anzufangen?** Klicken Sie auf 'Qualification' in der Seitenleiste, um den kurzen Qualifikationstest zu absolvieren!")

# Optional: Add a collapsible section with more examples
with st.expander("🔍 Weitere Beispiele anzeigen"):
    st.markdown("""
    ### Weitere Übungsbeispiele:
    
    **Beispiel 5 - DIREKT:**
    - Frage: "Genießt du das Leben hier?"
    - Antwort: "Ich genieße es hier zu leben."
    - Warum direkt? Klare Bestätigung der Frage
    
    **Beispiel 6 - INDIREKT:**
    - Frage: "Wann schließen Sie das Anwesen?"
    - Antwort: "Wir verhandeln jetzt."
    - Warum indirekt? Gibt Status an, aber keine konkrete Zeit
    
    **Beispiel 7 - DIREKT:**
    - Frage: "Ist New York Ihre einzige Option?"
    - Antwort: "New York ist meine einzige Option."
    - Warum direkt? Direkte Bestätigung der Frage
    
    **Beispiel 8 - INDIREKT:**
    - Frage: "Liest du gerne Romanzen?"
    - Antwort: "Ich bevorzuge Selbsthilfebücher."
    - Warum indirekt? Gibt Alternative an statt die Frage direkt zu beantworten
    """)
