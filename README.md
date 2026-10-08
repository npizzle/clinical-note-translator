# 🩺 Clinical Note & Jargon Translator

An AI-powered medical communication tool that converts dense clinical notes, discharge summaries, and medical reports into clear, audience-tailored language with audio readouts, multi-turn conversational chat memory, and strict domain guardrails.

---

## 🌟 Key Features

* **Multi-Source Document Ingestion:** Accepts direct raw text input or multi-page medical PDF uploads (`pypdf`).
* **Audience Personas:** Dynamically adjusts translation tone and complexity across three distinct target audiences:
  * **Patient & Family:** Plain, 6th-grade reading level focusing on key takeaways and clear instructions.
  * **Non-Medical Caregiver:** Practical, actionable guidance tailored for home and day-to-day caregiving.
  * **Medical Student / Resident:** Concise, structured academic summary highlighting clinical facts and terminology.
* **Multimodal Text-to-Speech (TTS):** Generates audio readouts using OpenAI’s `tts-1` model across customizable voice profiles (`alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`).
* **Multi-Turn Conversational Memory:** Interactive chat interface (`st.chat_message`, `st.chat_input`) allowing users to ask follow-up questions grounded directly in their clinical document.
* **Clinical System Guardrails:** Strict prompt boundaries enforce health-only context and politely refuse off-topic or non-medical queries (e.g., coding, trivia, sports).
* **Enterprise Security:** API keys are secured in `.streamlit/secrets.toml` locally and managed via Streamlit Secrets in cloud production (excluded from Git version control).

---

## 🏗️ Architecture & Tech Stack

* **Frontend & Framework:** Python, Streamlit
* **LLM Engine:** OpenAI API (`gpt-4o-mini`)
* **Audio Readout:** OpenAI Text-to-Speech (`tts-1`)
* **PDF Ingestion:** `pypdf`
* **Version Control & Cloud Deployment:** Git, GitHub, Streamlit Community Cloud

---

## 🚀 Local Setup & Installation

### 1. Clone the Repository
```cmd
git clone [https://github.com/YOUR_USERNAME/clinical-note-translator.git](https://github.com/YOUR_USERNAME/clinical-note-translator.git)
cd clinical-note-translator