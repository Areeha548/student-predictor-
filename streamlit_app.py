import numpy as np
import joblib
import streamlit as st
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Student Predictor", page_icon="🎓", layout="centered")


@st.cache_resource
def load_model():
    """Load model.pkl. If it fails (version problem), train a fresh model."""
    try:
        return joblib.load("model.pkl")
    except Exception:
        X = np.array([[1, 40], [2, 45], [3, 50], [4, 60], [5, 65],
                      [6, 70], [7, 75], [8, 85], [2, 80], [1, 30]])
        y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 0])
        model = LogisticRegression()
        model.fit(X, y)
        return model


model = load_model()

st.title("🎓 Student Pass / Fail Predictor")
st.markdown("Enter the student's details below to predict the result.")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    study_hours = st.slider("Study Hours Per Day", 0.0, 10.0, 4.0, 0.5,
                            help="How many hours the student studies each day")
with col2:
    prev_score = st.slider("Previous Exam Score", 0.0, 100.0, 60.0, 1.0,
                           help="Score from the most recent exam (out of 100)")

st.markdown("---")

if st.button("🔮 Predict Result", use_container_width=True):
    data = np.array([[study_hours, prev_score]])
    prediction = int(model.predict(data)[0])
    confidence = float(model.predict_proba(data)[0][prediction])
    label = "Pass" if prediction == 1 else "Fail"

    if prediction == 1:
        st.success(f"✅ Prediction: **{label}**")
    else:
        st.error(f"❌ Prediction: **{label}**")

    st.metric("Model Confidence", f"{confidence * 100:.1f}%")

    with st.expander("See the input and result"):
        st.json({"study_hours": study_hours, "prev_score": prev_score,
                 "prediction": prediction, "result_label": label,
                 "confidence": round(confidence, 3)})

st.markdown("---")
st.subheader("Current Input Summary")
m1, m2 = st.columns(2)
m1.metric("Study Hours", f"{study_hours} hrs/day")
m2.metric("Previous Score", f"{prev_score}/100")
