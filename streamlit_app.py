import numpy as np
import joblib
import streamlit as st
from sklearn.linear_model import LogisticRegression

# ---------------------------------------------------------------
# 1. PAGE SETTINGS
# ---------------------------------------------------------------
st.set_page_config(
    page_title="Student Predictor",
    page_icon="🎓",
    layout="centered",
)

# ---------------------------------------------------------------
# 2. CUSTOM STYLE (CSS) - colors, cards, buttons
# ---------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Top banner */
    .hero {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
        padding: 2.2rem 1.5rem;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 24px rgba(79, 70, 229, 0.30);
    }
    .hero h1 {
        color: #ffffff;
        margin: 0;
        font-size: 2.1rem;
        font-weight: 800;
    }
    .hero p {
        color: #e0e7ff;
        margin: 0.5rem 0 0 0;
        font-size: 1.05rem;
    }

    /* Small section titles */
    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0.5rem 0 0.2rem 0;
    }

    /* Result cards */
    .result-card {
        padding: 1.6rem 1rem;
        border-radius: 18px;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    .result-pass { background: linear-gradient(135deg, #059669, #10b981); }
    .result-fail { background: linear-gradient(135deg, #dc2626, #f43f5e); }
    .result-card .big {
        color: #ffffff;
        font-size: 2.4rem;
        font-weight: 800;
        margin: 0;
    }
    .result-card .small {
        color: #ffffff;
        opacity: 0.92;
        font-size: 1rem;
        margin: 0.3rem 0 0 0;
    }

    /* Probability bars */
    .bar-label {
        display: flex;
        justify-content: space-between;
        font-weight: 600;
        margin-top: 0.8rem;
        margin-bottom: 0.25rem;
    }
    .bar-bg {
        background: rgba(128, 128, 128, 0.25);
        border-radius: 10px;
        height: 16px;
        overflow: hidden;
    }
    .bar-fill-pass {
        background: linear-gradient(90deg, #059669, #34d399);
        height: 100%;
        border-radius: 10px;
    }
    .bar-fill-fail {
        background: linear-gradient(90deg, #dc2626, #fb7185);
        height: 100%;
        border-radius: 10px;
    }

    /* Predict button */
    div.stButton > button {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1rem;
        font-size: 1.1rem;
        font-weight: 700;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(79, 70, 229, 0.45);
        color: #ffffff;
        border: none;
    }

    /* Footer */
    .footer {
        text-align: center;
        opacity: 0.7;
        font-size: 0.9rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------
# 3. LOAD THE MODEL
# ---------------------------------------------------------------
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

# ---------------------------------------------------------------
# 4. SIDEBAR - about the project
# ---------------------------------------------------------------
with st.sidebar:
    st.header("ℹ️ About")
    st.write(
        "This app predicts whether a student will **Pass** or **Fail** "
        "using two things: daily study hours and the previous exam score."
    )
    st.markdown("---")
    st.subheader("⚙️ How it works")
    st.markdown(
        "1. Move the two sliders\n"
        "2. Click **Predict Result**\n"
        "3. See the result and confidence"
    )
    st.markdown("---")
    st.subheader("🧰 Built with")
    st.markdown("- Python\n- scikit-learn (Logistic Regression)\n- Streamlit")
    st.markdown("---")
    st.caption("Made by Areeha Shafique")

# ---------------------------------------------------------------
# 5. HEADER BANNER
# ---------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>🎓 Student Pass / Fail Predictor</h1>
        <p>Enter the student's details and let the model predict the result</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------
# 6. INPUT SECTION
# ---------------------------------------------------------------
st.markdown('<p class="section-title">📝 Student Details</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    study_hours = st.slider(
        "📚 Study Hours Per Day",
        min_value=0.0,
        max_value=10.0,
        value=4.0,
        step=0.5,
        help="How many hours the student studies each day",
    )
with col2:
    prev_score = st.slider(
        "📊 Previous Exam Score",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0,
        help="Score from the most recent exam (out of 100)",
    )

# Live summary (updates as sliders move)
m1, m2 = st.columns(2)
m1.metric("Study Hours", f"{study_hours} hrs/day")
m2.metric("Previous Score", f"{prev_score:.0f}/100")

st.markdown("")

# ---------------------------------------------------------------
# 7. PREDICT BUTTON AND RESULT
# ---------------------------------------------------------------
if st.button("🔮 Predict Result", use_container_width=True):
    data = np.array([[study_hours, prev_score]])
    prediction = int(model.predict(data)[0])
    probabilities = model.predict_proba(data)[0]

    fail_pct = float(probabilities[0]) * 100
    pass_pct = float(probabilities[1]) * 100
    confidence = pass_pct if prediction == 1 else fail_pct

    if prediction == 1:
        st.markdown(
            f"""
            <div class="result-card result-pass">
                <p class="big">✅ PASS</p>
                <p class="small">The model is {confidence:.1f}% confident</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.balloons()
    else:
        st.markdown(
            f"""
            <div class="result-card result-fail">
                <p class="big">❌ FAIL</p>
                <p class="small">The model is {confidence:.1f}% confident</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Probability bars
    st.markdown(
        f"""
        <div class="bar-label"><span>Pass chance</span><span>{pass_pct:.1f}%</span></div>
        <div class="bar-bg"><div class="bar-fill-pass" style="width:{pass_pct:.1f}%"></div></div>
        <div class="bar-label"><span>Fail chance</span><span>{fail_pct:.1f}%</span></div>
        <div class="bar-bg"><div class="bar-fill-fail" style="width:{fail_pct:.1f}%"></div></div>
        """,
        unsafe_allow_html=True,
    )

    # Simple advice
    st.markdown("")
    if prediction == 1:
        st.info("💡 Keep up the good work! Regular study and revision will help maintain this result.")
    else:
        st.warning("💡 Try increasing daily study hours and revising weak topics to improve the result.")

    with st.expander("🔎 See the input and result details"):
        st.json({
            "study_hours": study_hours,
            "prev_score": prev_score,
            "prediction": prediction,
            "result_label": "Pass" if prediction == 1 else "Fail",
            "pass_probability": round(pass_pct / 100, 3),
            "fail_probability": round(fail_pct / 100, 3),
        })

# ---------------------------------------------------------------
# 8. FOOTER
# ---------------------------------------------------------------
st.markdown(
    '<div class="footer">Built with ❤️ using Python, scikit-learn and Streamlit</div>',
    unsafe_allow_html=True,
)