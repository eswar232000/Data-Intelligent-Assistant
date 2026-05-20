
import pandas as pd
from groq import Groq

# =========================================================
# GROQ API CONFIGURATION
# =========================================================

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv("/content/marksheet.csv")

# =========================================================
# DISPLAY DATASET
# =========================================================

print("\n==============================")
print("STUDENT MARKS DATASET")
print("==============================\n")

print(df.head())

# =========================================================
# DATA ANALYSIS
# =========================================================

# Total Marks
df["Total"] = (
    df["Science"] +
    df["English"] +
    df["History"] +
    df["Maths"]
)

# Average Marks
df["Average"] = df["Total"] / 4

# Topper
topper = df.loc[df["Total"].idxmax()]

# Subject Averages
science_avg = df["Science"].mean()
english_avg = df["English"].mean()
history_avg = df["History"].mean()
maths_avg = df["Maths"].mean()

# =========================================================
# PRINT ANALYTICS
# =========================================================

print("\n==============================")
print("DATA ANALYTICS")
print("==============================\n")

print(f"Average Science Marks : {science_avg:.2f}")
print(f"Average English Marks : {english_avg:.2f}")
print(f"Average History Marks : {history_avg:.2f}")
print(f"Average Maths Marks   : {maths_avg:.2f}")

print("\n==============================")
print("TOP PERFORMING STUDENT")
print("==============================\n")

print(topper)

# =========================================================
# GENERATIVE AI PROMPT
# =========================================================

dataset_sample = df.head(10).to_string()

prompt = f"""
You are an Educational Data Analyst AI.

Analyze the following student marks dataset.

Dataset Headers:
id,name,gender,age,section,Science,English,History,Maths

Dataset Sample:
{dataset_sample}

Perform the following:

1. Overall academic performance analysis
2. Subject-wise performance analysis
3. Student performance insights
4. Weak subject identification
5. Gender-wise performance analysis
6. Top performer analysis
7. Improvement recommendations
8. Final educational report

Generate a professional educational analytics report.
"""

# =========================================================
# GROQ AI ANALYSIS
# =========================================================

print("\n==============================")
print("GENERATING AI ANALYSIS...")
print("==============================\n")

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

# =========================================================
# OUTPUT
# =========================================================

ai_output = response.choices[0].message.content

print("\n==============================")
print("AI EDUCATIONAL ANALYTICS REPORT")
print("==============================\n")

print(ai_output)
