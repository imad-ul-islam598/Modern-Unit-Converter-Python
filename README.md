# 🔄 Universal Unit Converter

## 🚀 Project Overview
The **Universal Unit Converter** is a powerful and user-friendly **Streamlit** application that allows users to convert values between different units seamlessly. It supports **voice input**, offers **multiple themes**, and maintains a **conversion history** for easy reference.

## 🎯 Features
✅ **Multi-Category Unit Conversion:**
- **Length** (meters, kilometers, inches, feet, etc.)
- **Weight** (kilograms, grams, pounds, etc.)
- **Volume** (liters, milliliters, gallons, etc.)
- **Temperature** (Celsius, Fahrenheit, Kelvin)
- **Speed** (m/s, km/h, mph, etc.)
- **Time** (seconds, minutes, hours, days)

✅ **Voice Input Support** 🎤
- Speak your conversion command (e.g., *"10 Kilograms to Grams"*), and the app will process it.

✅ **Theming Options** 🎨
- Light Mode
- Dark Mode
- Blue Mode

✅ **Conversion History** 📜
- View past conversions and clear history when needed.

✅ **User-Friendly Interface** 💡
- Minimalistic and intuitive design for easy usage.

---

## Tech Stack
- **Frontend & Backend:** Streamlit
- **Unit Conversion:** Pint
- **Voice Processing:** SpeechRecognition
- **Data Handling:** Pandas, JSON
- **Programming Language:** Python

---

## 📌 Installation & Setup

### 1️⃣ Prerequisites
#### Ensure you have the following installed:
✔️ Python 3.8+  
✔️ pip (Python package manager)  

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/unit-converter.git
cd unit-converter
```

### 3️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 📖 How to Use
🔹 Select a **category** (Length, Weight, Volume, etc.).  
🔹 Choose the **from unit** and **to unit**.  
🔹 Enter the **value** you want to convert.  
🔹 Click the **Convert** button to see the result.  
🔹 Use the **Voice Input** feature to convert by speaking.  
🔹 Check the **Conversion History** for previous conversions.  

---

## 📦 Dependencies
The project uses the following libraries:

- **Streamlit** (`streamlit`): Used for creating the interactive web app interface.
- **Pint** (`pint`): A powerful unit conversion library to handle measurement conversions.
- **SpeechRecognition** (`speech_recognition`): Enables voice input functionality to process spoken conversion commands.
- **JSON** (`json`): Used to store and retrieve conversion history.
- **OS** (`os`): Provides functions to interact with the operating system, such as file handling.
- **Pandas** (`pandas`): Used for managing and displaying the conversion history in a structured table format.
- **Regular Expressions** (`re`): Helps extract numerical values and units from voice input.

To install all dependencies manually:
```sh
pip install streamlit pint SpeechRecognition pandas
```

---

## Follow For More...
🔗 GitHub: [imad-ul-islam598](https://github.com/imad-ul-islam598)  

## Developed By
**Imad Ul Islam** 

