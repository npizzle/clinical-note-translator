import io
import streamlit as st
from openai import OpenAI
import pypdf

st.set_page_config(page_title="Clinical Note Translator", page_icon="🩺", layout="wide")

st.title("🩺 Medical Jargon & Clinical Note Translator")
st.write("Extract text from clinical PDFs or paste raw notes, then translate them into clear language with audio readouts.")

# --- API KEY & CONFIGURATION SIDEBAR ---
st.sidebar.header("⚙️ Configuration")

# Retrieve API key from secrets or sidebar input
api_key = st.secrets.get("OPENAI_API_KEY", "")
if not api_key:
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")

selected_persona = st.sidebar.selectbox(
    "Translate For (Audience Persona):",
    [
        "Patient & Family (6th-Grade Reading Level)",
        "Non-Medical Caregiver (Clear Actionable Terms)",
        "Medical Student / Resident (Academic Summary)"
    ]
)

selected_voice = st.sidebar.selectbox(
    "Text-to-Speech Voice:",
    ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
)

# --- INPUT SECTION (PASTE OR UPLOAD) ---
st.subheader("1. Input Clinical Documentation")
input_mode = st.radio("Choose Input Method:", ["Upload File (PDF / TXT)", "Paste Text Directly"], horizontal=True)

extracted_text = ""

if input_mode == "Upload File (PDF / TXT)":
    uploaded_file = st.file_uploader("Upload a clinical note, discharge summary, or report", type=["pdf", "txt"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".pdf"):
            pdf_reader = pypdf.PdfReader(uploaded_file)
            pdf_text = []
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    pdf_text.append(text)
            extracted_text = "\n".join(pdf_text)
        else:
            extracted_text = uploaded_file.read().decode("utf-8")

        if extracted_text.strip():
            st.success(f"Successfully loaded '{uploaded_file.name}' ({len(extracted_text)} characters).")
            with st.expander("Preview Extracted Document Text"):
                st.write(extracted_text)
        else:
            st.warning("No readable text found in the uploaded file.")
else:
    extracted_text = st.text_area("Paste raw medical narrative, clinical note, or discharge summary here:", height=200)

# --- TRANSLATION LOGIC ---
if st.button("🚀 Translate Clinical Note", type="primary"):
    if not api_key:
        st.error("Please provide an OpenAI API Key in the sidebar or secrets.toml to proceed.")
    elif not extracted_text.strip():
        st.warning("Please upload a file or paste text to translate.")
    else:
        client = OpenAI(api_key=api_key)

        system_prompt = (
            f"You are an expert clinical communication assistant. Translate the provided medical text "
            f"for the following target audience: '{selected_persona}'. "
            f"Guidelines:\n"
            f"- Explain complex medical terminology, acronyms, and diagnoses in simple terms.\n"
            f"- Group findings into three distinct sections: 'Key Summary', 'Medications & Treatments', and 'Next Steps'.\n"
            f"- Maintain accurate clinical facts while removing unnecessary medical jargon."
        )

        with st.spinner("Translating narrative..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": extracted_text}
                    ],
                    temperature=0.3
                )

                translation = response.choices[0].message.content
                st.session_state["latest_translation"] = translation

            except Exception as e:
                st.error(f"Translation Error: {e}")

# --- DISPLAY RESULTS & AUDIO GENERATION ---
if "latest_translation" in st.session_state:
    st.divider()
    st.subheader("2. Translated Output")
    translation_text = st.session_state["latest_translation"]
    st.markdown(translation_text)

    st.divider()
    st.subheader("3. Audio Readout (Text-to-Speech)")

    col1, col2 = st.columns([1, 2])
    with col1:
        generate_audio = st.button("🔊 Generate Audio Readout")

    if generate_audio:
        if not api_key:
            st.error("OpenAI API Key required for Text-to-Speech.")
        else:
            client = OpenAI(api_key=api_key)
            with st.spinner(f"Generating audio with voice '{selected_voice}'..."):
                try:
                    # Truncate text if it exceeds OpenAI TTS limit (4,096 chars)
                    audio_input = translation_text[:4000]

                    tts_response = client.audio.speech.create(
                        model="tts-1",
                        voice=selected_voice,
                        input=audio_input
                    )

                    # Streamlit audio player accepts byte buffers
                    audio_bytes = tts_response.content
                    st.audio(audio_bytes, format="audio/mp3")

                except Exception as e:
                    st.error(f"Audio Generation Error: {e}")