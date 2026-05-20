
import streamlit as st
import pandas as pd
from groq import Groq

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Student Marks Data Analyst",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# GROQ API CONFIGURATION
# =========================================================

GROQ_API_KEY = st.secrets["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"]

client = Groq(api_key=GROQ_API_KEY)

# =========================================================
# TITLE
# =========================================================

st.title("📊 AI Student Marks Data Analyst")

st.markdown("""
### Generative AI Educational Analytics Platform

Analyze student performance using:
- AI Educational Insights
- Subject Performance Analytics
- Student Intelligence Reports
- Generative AI Recommendations
""")

# =========================================================
# FILE UPLOADER
# =========================================================

uploaded_file = st.file_uploader(
    "📁 Upload Student Marks CSV File",
    type=["csv"]
)

# =========================================================
# MAIN APPLICATION
# =========================================================

if uploaded_file is not None:

    # =====================================================
    # LOAD DATASET
    # =====================================================

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset Uploaded Successfully")

    # =====================================================
    # DISPLAY DATASET
    # =====================================================

    st.subheader("📋 Dataset Preview")

    st.dataframe(df)

    # =====================================================
    # DATA ANALYSIS
    # =====================================================

    df["Total"] = (
        df["Science"] +
        df["English"] +
        df["History"] +
        df["Maths"]
    )

    df["Average"] = df["Total"] / 4

    topper = df.loc[df["Total"].idxmax()]

    # =====================================================
    # METRICS
    # =====================================================

    st.subheader("📈 Subject-wise Average Marks")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Science Average",
            round(df["Science"].mean(), 2)
        )

        st.metric(
            "English Average",
            round(df["English"].mean(), 2)
        )

    with col2:
        st.metric(
            "History Average",
            round(df["History"].mean(), 2)
        )

        st.metric(
            "Maths Average",
            round(df["Maths"].mean(), 2)
        )

    # =====================================================
    # TOPPER
    # =====================================================

    st.subheader("🏆 Top Performing Student")

    st.write(topper)

    # =====================================================
    # AI PROMPT
    # =====================================================

    dataset_sample = df.head(10).to_string()

    prompt = f"""
You are an Educational Data Analyst AI.

Analyze the following student marks dataset.

Dataset Headers:
id,name,gender,age,section,Science,English,History,Maths

Dataset Sample:
{dataset_sample}

Perform:

1. Overall academic performance analysis
2. Subject-wise performance analysis
3. Weak subject identification
4. Strong subject identification
5. Student performance insights
6. Gender-wise performance analysis
7. Improvement recommendations
8. Final educational analytics report

Generate professional educational insights.
"""

    # =====================================================
    # GENERATE AI ANALYSIS
    # =====================================================

    if st.button("🚀 Generate AI Analysis"):

        with st.spinner("Generating AI Educational Insights..."):

            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1000
            )

            ai_output = response.choices[0].message.content

        st.success("✅ AI Analysis Generated Successfully")

        st.subheader("🤖 AI Educational Analytics Report")

        st.write(ai_output)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
### 🎓 AI Educational Analytics Platform

Built Using:
- Streamlit
- Groq API
- LLaMA 3
- Generative AI
- Educational Data Analytics
""")
