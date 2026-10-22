🎓 Student Pass / Fail Predictor

A simple machine learning web app that predicts whether a student will Pass or Fail based on daily study hours and previous exam score.

🔗 Live Demo

https://areeha-student-predictor.streamlit.app/

✨ Features
Two sliders for study hours and previous exam score
Pass / Fail prediction with confidence percentage
Pass and Fail probability bars
Clean, colorful interface with a sidebar
🧰 Built With
Python
scikit-learn (Logistic Regression)
Streamlit
Flask and FastAPI (learning examples included in this repo)
▶️ How to Run Locally

1. Clone the repo

git clone https://github.com/Areeha548/student-predictor-.git 
cd student-predictor-

2. Install the libraries

pip install -r requirements.txt

3. Start the app

streamlit run streamlit_app.py
📁 Project Files
File	What it does
streamlit_app.py	The Streamlit web app
train_model.py	Trains the model and saves it as model.pkl
main.py	FastAPI version of the prediction API
main_fast_api.py	FastAPI student CRUD example
app.py	Flask student CRUD example
async_example.py	Sync vs async example
session_state_example.py	Streamlit session state example
⚠️ Note

The model is trained on a small sample dataset of 10 students for learning and demo purposes. It is not meant for real academic decisions.

👩‍💻 Author

Areeha Shafique
