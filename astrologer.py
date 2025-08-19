import streamlit as st
import datetime
import ollama

# --- Helper Functions ---

def get_sun_sign(date):
    """Calculates the Zodiac Sun Sign based on a date object."""
    day = date.day
    month = date.month
    if (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Aquarius ♒"
    if (month == 2 and day >= 19) or (month == 3 and day <= 20): return "Pisces ♓"
    if (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Aries ♈"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Taurus ♉"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Gemini ♊"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Cancer ♋"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Leo ♌"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Virgo ♍"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Libra ♎"
    if (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Scorpio ♏"
    if (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Sagittarius ♐"
    if (month == 12 and day >= 22) or (month == 1 and day <= 19): return "Capricorn ♑"
    return "Unknown"

def get_horoscope(sun_sign):
    """Provides a generic, rule-based horoscope for a given sun sign."""
    sign = sun_sign.split(' ')[0]
    horoscopes = {
        "Aries": "The fiery energy of Mars propels you forward. Today is a day for bold action.",
        "Taurus": "Venus graces your sign with a desire for comfort and beauty. Indulge your senses.",
        "Gemini": "Mercury's influence sharpens your wit. Engage in meaningful conversations.",
        "Cancer": "The Moon enhances your intuition. Pay attention to your dreams and feelings.",
        "Leo": "The Sun's vibrant rays boost your confidence. Step into the spotlight.",
        "Virgo": "Your analytical mind is at its peak. Focus on organizing your life.",
        "Libra": "Harmony and balance are your keywords today. Seek beauty and fairness.",
        "Scorpio": "Pluto's transformative energy encourages you to look beneath the surface.",
        "Sagittarius": "Jupiter's expansive influence fuels your adventurous spirit. Embrace growth.",
        "Capricorn": "Saturn's disciplined energy supports your ambitions. Focus on long-term goals.",
        "Aquarius": "Uranus inspires your innovative side. Think outside the box.",
        "Pisces": "Neptune enhances your imagination. A day for creative pursuits."
    }
    return horoscopes.get(sign, "The stars are quiet today, offering a moment of peaceful reflection.")

# --- Streamlit App UI ---

st.set_page_config(page_title="AI Astrologer", page_icon="✨", layout="centered")

st.title("AI Astrologer ✨")
st.markdown("Unlock the secrets of the cosmos based on your birth details.")

with st.form("astro_form"):
    name = st.text_input("Full Name", placeholder="Alex Doe")
    dob = st.date_input("Date of Birth", min_value=datetime.date(1920, 1, 1), max_value=datetime.date.today())
    tob = st.time_input("Time of Birth")
    pob = st.text_input("Place of Birth", placeholder="London, UK")
    question = st.text_area("Ask the Stars a Question", placeholder="What does my career path look like in the coming year?")

    submitted = st.form_submit_button("Get Your Reading")

if submitted:
    if not all([name, dob, tob, pob, question]):
        st.warning("Please fill out all the celestial details.")
    else:
        with st.spinner("Consulting the celestial bodies..."):
            # 1. Rule-based results
            sun_sign = get_sun_sign(dob)
            horoscope = get_horoscope(sun_sign)

            # 2. AI-driven response using Ollama with the Mistral model
            prompt = f"""
                You are a mystical and wise AI Astrologer. A user has provided their birth details and a question.
                Provide an insightful, positive, and astrology-themed answer in 2-3 paragraphs.

                - Name: {name}
                - Date of Birth: {dob}
                - Time of Birth: {tob}
                - Place of Birth: {pob}
                - Their Sun Sign is: {sun_sign}
                - Their Question is: "{question}"

                Now, answer their question as the AI Astrologer in a mystical tone.
            """
            try:
                # Call the Ollama model, hardcoded to "mistral"
                response = ollama.chat(
                    model='mistral',
                    messages=[{'role': 'user', 'content': prompt}]
                )
                ai_response_text = response['message']['content']

                # 3. Display results
                st.divider()
                st.subheader(f"Hello {name}, here is your cosmic reading:")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Your Sun Sign", sun_sign)
                with col2:
                    st.info("Your Cosmic Forecast")
                    st.write(horoscope)

                st.success("A Message from the Stars")
                st.markdown(ai_response_text)

            except Exception as e:
                st.error(f"Failed to connect to Ollama. Is the Ollama server running and the 'mistral' model downloaded?")
                st.error(f"Error details: {e}")

