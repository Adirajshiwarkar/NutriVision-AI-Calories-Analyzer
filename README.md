
# 🍎 NutriVision – AI Calorie Analyzer

**NutriVision** is an AI-powered web app that analyzes food images to provide a detailed calorie breakdown, healthiness score, and recommendations based on dietary fitness. Built with **Streamlit** and **Google's Gemini 1.5 Flash Vision model**, it offers an intuitive interface to understand your meals better — all from a single image upload.

---

## 🚀 Features

- 📸 Upload any food image
- 🧠 AI identifies food items
- 🔍 Provides per-item calorie & macronutrient breakdown
- ⚖️ Suggests ideal body weight range for the dish
- 💡 Tells you whether it's healthy to consume
- ⭐ Rates the dish's healthiness out of 10

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** Google Generative AI (Gemini 1.5 Flash)
- **Image Processing:** PIL, io
- **Deployment:** Localhost or Streamlit Cloud

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/AdirajShiwarkar/nutrivision.git
cd nutrivision
```

### 2. Create `.env` File

Create a file named `.env` and add your Gemini API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Or paste the key directly into `app.py` (not recommended for production).

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
nutrivision/
│
├── app.py               # Main Streamlit app
├── .env                 # API key (not committed)
├── favicon.png          # App icon
├── README.md            # Project description
└── requirements.txt     # Python dependencies
```

---

## 📸 Example Use

1. Upload a food photo (e.g. salad, burger).
2. Click **"Analyze Image"**.
3. See calorie breakdown, health suggestions, and a 1–10 health score.

---

## 🧠 AI Prompt Used

> "Please analyze the dish shown in this image.  
> Identify each food item, provide macronutrient and calorie breakdown, estimate total calories, assess healthiness, and give a rating out of 10."

---

## 📝 To-Do

- [ ] Add PDF export of report  
- [ ] Add BMI personalization  
- [ ] Deploy on Streamlit Cloud

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

Developed by [Your Name]  
Powered by [Google Gemini API](https://ai.google.dev)  
UI built with [Streamlit](https://streamlit.io/)
