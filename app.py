import streamlit as st
from pint import UnitRegistry
import speech_recognition as sr
import json
import os
import pandas as pd
import re

# **SET PAGE CONFIG FIRST**
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Initialize unit registry
ureg = UnitRegistry()

# Define unit categories
unit_categories = {
    "Length": ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"],
    "Weight": ["kilogram", "gram", "milligram", "pound", "ounce"],
    "Volume": ["liter", "milliliter", "gallon", "quart", "pint"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "foot/second"],
    "Time": ["second", "minute", "hour", "day"]
}

# Load or initialize conversion history
history_file = "conversion_history.json"
if os.path.exists(history_file):
    try:
        with open(history_file, "r") as file:
            conversion_history = json.load(file)
    except json.JSONDecodeError:
        conversion_history = {category: [] for category in unit_categories}
else:
    conversion_history = {category: [] for category in unit_categories}

# Ensure all categories exist in history
for cat in unit_categories:
    if cat not in conversion_history:
        conversion_history[cat] = []

# Sidebar theme selection
with st.sidebar:
    st.title("🎨 Select Theme")
    mode = st.radio("", ["Light Mode", "Dark Mode", "Blue Mode"], index=0)

def apply_theme():
    styles = """
        <style>
            body, .stApp {background-color: %s !important; color: %s !important;}
            h1, h3 {color: %s !important;}
            label, .stSelectbox label, .stNumberInput label {color: inherit !important;}
            div.stButton > button {
                background-color: %s !important; color: %s !important;
                border-radius: 10px;
                transition: 0.3s;
            }

            div.stButton > button:hover {
                background-color: %s !important;
            }

            .result-box, .no-conversion-history {
                padding: 10px; 
                border-radius: 10px; 
                text-align: center; 
                font-size: 18px; 
                font-weight: bold;
                background-color: %s;
                color: %s;
            }

            .stSidebar, .css-1d391kg { 
                background-color: %s !important;
            }

            .css-1d391kg * { color: %s !important; 
            }

            .stSidebar * {
            color: inherit !important;
            }

            .stRadio label {
            color: %s !important; /* This will be dynamically replaced */
            }

            .developer-caption {
            padding: 5px;
            border-radius: 5px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            color: %s;
            }

            .styled-divider {
            border: none;
            height: 2px;
            background: linear-gradient(to right,rgb(9, 69, 129),rgb(56, 219, 244)); /* Gradient color */
            margin: 50px 0 10px 0;
            }

        </style>
    """
    if mode == "Light Mode":
        st.markdown(styles % ("white", "black", "blue", "blue", "white", "darkblue", "#f0f0f0", "black", "#f0f0f0", "black", "black", "green"), unsafe_allow_html=True)
    elif mode == "Dark Mode":
        st.markdown(styles % ("#121212", "white", "white", "gray", "white", "darkgray", "#333333", "white", "#1c1c1c", "white", "yellow", "white"), unsafe_allow_html=True)
    elif mode == "Blue Mode":
        st.markdown(styles % ("#001f3f", "white", "skyblue", "skyblue", "navy", "#0070BB", "#004080", "white", "#0C2340", "white", "white", "#0070BB"), unsafe_allow_html=True)

apply_theme()

# Streamlit UI
st.markdown("""
    <h1 style='text-align: center;'>Universal Unit Converter</h1>
    <h3 style='text-align: center;'>Convert values between different units.</h3>
""", unsafe_allow_html=True)

# Category selection
category = st.selectbox("Select a category", list(unit_categories.keys()))
units = unit_categories[category]

# Unit selection
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# User input
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

# Speech recognition function
# def voice_input():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         try:
#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
#             text = recognizer.recognize_google(audio).lower()
#             return text
#         except sr.UnknownValueError:
#             st.markdown("""<div style='color:#FF0000; padding:5px; font-size:16px;'>⚠️ <strong>Warning:</strong> Could not understand audio. </div>""", unsafe_allow_html=True)

#         except sr.RequestError:
#             st.markdown("""<div style='color:#FF0000; padding:5px; font-size:16px;'>🚫 <strong>Warning:</strong> Could not request results. Check your internet. </div>""", unsafe_allow_html=True)

#         except sr.WaitTimeoutError:
#             st.markdown("""<div style='color:#FF0000; padding:5px; font-size:16px;'>🔇 <strong>Warning:</strong> Timeout! No speech detected. Please try again. </div>""", unsafe_allow_html=True)

            
#     return ""

# # Extract value and units from voice input
# def parse_voice_command(command):
#     pattern = r"(\d+\.?\d*)\s*(\w+)\s*(to|in)?\s*(\w+)?"
#     match = re.search(pattern, command)
#     if match:
#         value = float(match.group(1))
#         from_unit = match.group(2)
#         to_unit = match.group(4) if match.group(4) else None
#         return value, from_unit, to_unit
#     return None, None, None

# if st.button("🎤 Voice Input"):
#     with st.spinner("Listening... Speak now!"):
#         voice_command = voice_input()
    
#     if voice_command:
#         st.markdown(f"""<div style='padding:10px; font-size:16px; font-weight:bold; color:gray; text-align:start;'> Recognized: {voice_command}</div>""", unsafe_allow_html=True)
#         value, from_unit, to_unit = parse_voice_command(voice_command)
        
#         if value and from_unit and to_unit:
#             try:
#                 result = (value * ureg(from_unit)).to(to_unit)
#                 st.markdown(f"""<div class='result-box' style='margin-bottom:10px;'>{value} {from_unit} = {result.magnitude:.2f} {to_unit}</div>""", unsafe_allow_html=True)
#                 conversion_history[category].append({
#                     "Value": value,
#                     "From": from_unit,
#                     "To": to_unit,
#                     "Result": f"{result.magnitude:.4f}"
#                 })
#                 with open(history_file, "w") as file:
#                     json.dump(conversion_history, file)
#             except Exception as e:
#                 st.error(f"Conversion error: {e}")
#         else:
#             st.markdown("""<div style='color:#FF0000; margin-bottom:10px; font-size:16px;'>⚠️ <strong>Warning:</strong> Could not extract conversion details from voice input. </div>""", unsafe_allow_html=True)


# Manual conversion logic for user to select his unit manually
if st.button("Convert"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        # st.success(f"{value} {from_unit} = {result.magnitude:.2f} {to_unit}")
        st.markdown(f"""<div class='result-box'>{value} {from_unit} = {result.magnitude:.2f} {to_unit}</div>""", unsafe_allow_html=True)
        conversion_history[category].append({
            "Value": value,
            "From": from_unit,
            "To": to_unit,
            "Result": f"{result.magnitude:.4f}"
        })
        with open(history_file, "w") as file:
            json.dump(conversion_history, file)
    except Exception as e:
        st.error(f"Conversion error: {e}")

# Display conversion history
st.subheader("Conversion History")
history_df = pd.DataFrame(conversion_history[category])
if not history_df.empty:
    if "S.No" not in history_df.columns:  # Ensure "S.No" is only added once
        history_df.insert(0, "S.No", range(1, len(history_df) + 1))
    history_df = history_df[["S.No", "Value", "From", "To", "Result"]]  # Reorder columns
    
    # Display without default index
    st.dataframe(history_df.set_index("S.No"))  # Hide default index and keep only "S.No"

    if st.button("Clear History"):
        conversion_history[category] = []
        with open(history_file, "w") as file:
            json.dump(conversion_history, file)
        st.rerun()
else:
    st.markdown("""<div class='no-conversion-history'>No conversion history available.</div>""", unsafe_allow_html=True)

st.markdown("<div class='styled-divider'></div>", unsafe_allow_html=True)
st.markdown("<div class='developer-caption'>Developed By ⮕ IMAD UL ISLAM</div>", unsafe_allow_html=True)



