AI Astrologer ✨
A simple web application that provides personalized astrological readings using a local Large Language Model (LLM) powered by Ollama.

Project Overview
This application was created as an internship project to demonstrate the integration of a simple, rule-based system with a powerful, locally-run AI model. It collects a user's birth details (name, date, time, and place), calculates their sun sign, provides a generic horoscope, and then uses the Mistral LLM to answer a specific, user-submitted question in a mystical, astrological tone.

The entire backend runs locally, ensuring user privacy and zero API costs.

Features
Clean & Simple UI: An intuitive web interface built with Streamlit for easy user interaction.

Sun Sign Calculator: Automatically determines the user's zodiac sign from their date of birth.

Rule-Based Horoscope: Provides a classic, pre-defined horoscope for the calculated sun sign.

AI-Powered Q&A: Leverages a local LLM (Mistral) via Ollama to generate a detailed, personalized answer to a user's question.

Fully Local: All processing is done on the user's machine, requiring no internet connection (after setup) and ensuring data privacy.

Tech Stack
Python: The core programming language.

Streamlit: For creating the interactive web user interface.

Ollama: For serving and managing the local Large Language Model.

Mistral: The specific LLM used for generating personalized readings.

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.8+: You can download it from python.org.

Ollama: You must have the Ollama server application installed and running. Download it from ollama.com.

🚀 Setup and Installation
Follow these steps to get the application running on your local machine.

1. Clone the Repository
First, clone this repository to your local machine (or simply download the source code files).

# Replace with your actual repository URL if you create one
git clone https://github.com/your-username/ai-astrologer.git
cd ai-astrologer

2. Install Python Dependencies
Install the required Python libraries using the requirements.txt file. It's recommended to do this within a virtual environment.

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the packages
pip install -r requirements.txt

3. Download the LLM Model
You need to pull the mistral model for Ollama to use. Make sure the Ollama application is running, then open your terminal and run:

ollama pull mistral

This will download the model files to your machine. This only needs to be done once.

▶️ Running the Application
With the setup complete, you can now run the Streamlit application.

Make sure the Ollama application is running in the background.

Open your terminal, navigate to the project directory, and run the following command:

streamlit run app.py

If the command above doesn't work, try this alternative:

python -m streamlit run app.py

Your default web browser should automatically open a new tab with the AI Astrologer application ready to use.

📂 Project Structure
.
├── app.py              # The main Streamlit application script
├── requirements.txt      # Python dependencies
└── README.md           # This file
