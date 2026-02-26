# 🥗 Advancing Nutrition Science through GeminiAI

An AI-powered web application that provides instant nutritional insights, personalized meal plans, and virtual nutrition coaching using Google Gemini AI.

---

## 🚀 Features

### 🍎 Nutrition Analyzer

- Analyze nutritional values of food items

# 🥗 NutriAI — Advancing Nutrition with Gemini AI

A Streamlit web app that provides instant nutritional insights, personalized meal plans, and a virtual nutrition coach powered by Google Gemini (Generative AI).

---

## 🚀 Features

- 🍎 Nutrition Analyzer — estimates calories, protein, fat, carbs, vitamins, and minerals for user-provided foods.
- 📅 Meal Planner — generates a balanced 7-day meal plan with breakfast, lunch, dinner, and a grocery list.
- 💬 AI Nutrition Coach — provides diet recommendations, healthy tips, and fitness guidance.

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- Google Generative AI (Gemini)

---

## ⚙️ Quickstart (Windows)

1. Clone the repository (or use your local copy):

```bash
git clone https://github.com/balajigotloori/Advancing-Nutrition-Science-through-GeminiAI.git
cd Advancing-Nutrition-Science-through-GeminiAI
```

2. Create and activate a virtual environment:

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows (cmd):

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the Google Gemini API key (recommended: environment variable):

PowerShell (session only):

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
```

Windows (cmd):

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

macOS / Linux:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

If the app currently sets the key directly in `app.py`, you can change it to read from the environment instead:

```python
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

5. Run the app:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

_(Add screenshots in the `docs/` folder or include images in this section.)_

---

## 🧠 How it works

The Streamlit UI collects user input (food items, preferences, goals) and sends structured prompts to the Gemini model. The model returns nutrition estimates, meal plans, and advice which the app formats and displays to the user.

---

## 📌 Future enhancements

- User authentication and profiles
- Barcode / camera-based food recognition
- Diet tracking, progress charts, and exportable reports

---

## 👨‍💻 Author

Gotloori Balaji — [GitHub](https://github.com/balajigotloori)

---

