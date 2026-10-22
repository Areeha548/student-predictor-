# 🎓 Student Pass / Fail Predictor

A simple Machine Learning web app that predicts whether a student will **Pass or Fail** based on daily study hours and previous exam score.

## 🔗 Live Demo

[Try the Student Pass / Fail Predictor](https://areeha-student-predictor.streamlit.app/)

## ✨ Features

- 📚 Two sliders for daily study hours and previous exam score
- 🎯 Pass / Fail prediction with confidence percentage
- 📊 Pass and Fail probability bars
- 🎨 Clean, colorful interface with a sidebar

## 🧰 Built With

- Python
- scikit-learn (Logistic Regression)
- Streamlit
- Flask (learning example)
- FastAPI (learning examples)

## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Areeha548/student-predictor-.git
cd student-predictor-
```

### 2. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit App

```bash
streamlit run streamlit_app.py
```

## 📁 Project Files

| File | Description |
|---|---|
| `streamlit_app.py` | Main Streamlit web application |
| `train_model.py` | Trains the machine learning model and saves it as `model.pkl` |
| `main.py` | FastAPI prediction API example |
| `main_fast_api.py` | FastAPI student CRUD example |
| `app.py` | Flask student CRUD example |
| `async_example.py` | Demonstrates synchronous and asynchronous execution |
| `session_state_example.py` | Demonstrates Streamlit session state |

## ⚠️ Important Note

The model is trained on a small sample dataset of only 10 students for learning and demonstration purposes. Its predictions are not reliable enough for real academic decisions.

## 👩‍💻 Author

**Areeha Shafique**
