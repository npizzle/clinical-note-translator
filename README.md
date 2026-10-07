"# clinical-note-translator" 
🩺 Clinical Note Translator & Audio Reader

An AI-powered web application that converts complex medical jargon, discharge summaries, and EHR clinical notes into accessible, audience-tailored translations with natural voice audio readouts.

📌 Overview

Medical documentation often contains dense terminology, abbreviations, and clinical shorthand that can be overwhelming for patients, caregivers, and early medical trainees.

The Clinical Note Translator bridges the health literacy gap by ingesting raw clinical narratives or unstructured PDF reports and translating them into clear, actionable summaries tailored to specific target audiences. Additionally, it integrates text-to-speech audio synthesis to support accessibility and auditory learning.

✨ Key Features

📄 Multi-Format Ingestion: Supports direct text entry as well as instant PDF document parsing using pypdf.

🎯 Target Audience Personas: Customizes translation complexity and terminology across multiple audience levels:

Patient & Family: Simplified to a 6th-grade reading level focusing on clear explanations.

Non-Medical Caregiver: Actionable key takeaways, medication directions, and warning signs.

Medical Student / Resident: Academic summaries retaining key pathophysiology and clinical logic.

🔊 Text-to-Speech (TTS) Audio Readout: Synthesizes translated medical text into natural-sounding speech using OpenAI's tts-1 model with dynamic voice selection.

🔒 Secure Architecture: Local API keys are protected using .streamlit/secrets.toml and kept out of version control via .gitignore.

🛠️ Tech Stack

Frontend & UI: Streamlit

LLM Engine: OpenAI GPT-4o-mini

Audio Engine: OpenAI Text-to-Speech (TTS-1)

Document Parsing: pypdf

Version Control & Deployment: Git, GitHub, Streamlit Community Cloud

🚀 Getting Started (Local Setup)

Follow these steps to run the application locally on your machine.

Prerequisites

Python 3.9 or higher installed

An active OpenAI API Key

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/clinical-note-translator.git
cd clinical-note-translator


Create and activate a virtual environment:

Windows:

python -m venv venv
venv\Scripts\activate


macOS/Linux:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Configure secrets:
Create a folder named .streamlit in the project root directory and add a secrets.toml file inside it:

# .streamlit/secrets.toml
OPENAI_API_KEY = "sk-proj-your-actual-api-key-here"


Run the Streamlit app:

streamlit run app.py


🌐 Deployment

This application is configured for continuous deployment on Streamlit Community Cloud:

Push your repository to GitHub (ensuring .streamlit/secrets.toml is listed in your .gitignore).

Connect your GitHub account to Streamlit Community Cloud.

Select your repository, set the main file to app.py, and add OPENAI_API_KEY under Advanced Settings > Secrets.

⚠️ Disclaimer

This project is built for educational, research, and demonstration purposes only. It is not intended to serve as formal medical advice, diagnosis, or treatment planning. Always consult a qualified healthcare professional regarding any medical conditions or treatments.