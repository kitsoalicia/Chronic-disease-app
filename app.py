import streamlit as st

# Title
st.set_page_config(page_title="Chronic Disease Risk Screening", page_icon="💊")
st.title("💊 Chronic Disease Risk Screening Tool")
st.write("Welcome! Fill in your information to see your preliminary risk assessment.")

# -----------------------------
# User Inputs
# -----------------------------
st.header("Personal Information")
age = st.number_input("Age (years)", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", ["Female", "Male", "Other"])

st.header("Health Metrics")
weight = st.number_input("Weight (kg)", min_value=0.0, value=70.0, step=0.1)
height = st.number_input("Height (cm)", min_value=0.0, value=170.0, step=0.1)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=0, value=120)
diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=0, value=80)
cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value=0, value=180)

# -----------------------------
# Calculations
# -----------------------------
bmi = weight / ((height / 100) ** 2)
bp_warning = ""
cholesterol_warning = ""

# Blood Pressure Check
if systolic_bp >= 130 or diastolic_bp >= 80:
    bp_warning = "⚠️ Elevated blood pressure: increased risk of cardiovascular disease."
else:
    bp_warning = "✅ Blood pressure in normal range."

# Cholesterol Check
if cholesterol >= 240:
    cholesterol_warning = "⚠️ High cholesterol: increased risk of heart disease."
elif cholesterol >= 200:
    cholesterol_warning = "⚠️ Borderline high cholesterol."
else:
    cholesterol_warning = "✅ Cholesterol in normal range."

# BMI Check
if bmi >= 30:
    bmi_warning = "⚠️ High BMI: increased risk for chronic diseases."
elif bmi >= 25:
    bmi_warning = "⚠️ Overweight BMI: moderate risk for chronic diseases."
else:
    bmi_warning = "✅ BMI in normal range."

# -----------------------------
# Display Results
# -----------------------------
st.header("Results Summary")
st.write(f"**BMI:** {bmi:.1f}")
st.write(bmi_warning)
st.write(bp_warning)
st.write(cholesterol_warning)

# -----------------------------
# Optional Health Tips
# -----------------------------
st.header("Health Tips")
if bmi >= 25 or systolic_bp >= 130 or cholesterol >= 200:
    st.write("""
    - Maintain a balanced diet and reduce sugar and saturated fats.
    - Exercise at least 30 minutes daily.
    - Monitor blood pressure and cholesterol regularly.
    - Consult a healthcare professional for personalized advice.
    """)
else:
    st.write("Keep up the healthy lifestyle! ✅")
