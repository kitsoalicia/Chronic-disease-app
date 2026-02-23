import streamlit as st
import pandas as pd

# -----------------------------
# App Title
# -----------------------------
st.title("🩺 Chronic Disease Risk Screening Tool")
st.markdown("A simple tool to assess your risk for common chronic diseases.")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Personal Information")
age = st.sidebar.number_input("Age (years)", min_value=0, max_value=120, value=30)
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Other"])

st.sidebar.header("Health Metrics")
weight = st.sidebar.number_input("Weight (kg)", min_value=0.0, value=70.0, step=0.1)
height = st.sidebar.number_input("Height (cm)", min_value=0.0, value=170.0, step=0.1)
systolic_bp = st.sidebar.number_input("Systolic Blood Pressure (mmHg)", min_value=0, value=120)
diastolic_bp = st.sidebar.number_input("Diastolic Blood Pressure (mmHg)", min_value=0, value=80)
cholesterol = st.sidebar.number_input("Total Cholesterol (mg/dL)", min_value=0, value=180)

# -----------------------------
# Compute Metrics
# -----------------------------
height_m = height / 100
bmi = weight / (height_m ** 2)

# BMI category
if bmi < 18.5:
    bmi_category = "Underweight"
    bmi_color = "blue"
elif 18.5 <= bmi < 25:
    bmi_category = "Normal"
    bmi_color = "green"
elif 25 <= bmi < 30:
    bmi_category = "Overweight"
    bmi_color = "orange"
else:
    bmi_category = "Obese"
    bmi_color = "red"

# Blood pressure risk
if systolic_bp < 120 and diastolic_bp < 80:
    bp_risk = "Normal"
    bp_color = "green"
elif 120 <= systolic_bp < 130 and diastolic_bp < 80:
    bp_risk = "Elevated"
    bp_color = "yellow"
elif 130 <= systolic_bp < 140 or 80 <= diastolic_bp < 90:
    bp_risk = "High (Stage 1)"
    bp_color = "orange"
else:
    bp_risk = "High (Stage 2)"
    bp_color = "red"

# Cholesterol risk
if cholesterol < 200:
    chol_risk = "Desirable"
    chol_color = "green"
elif 200 <= cholesterol < 240:
    chol_risk = "Borderline High"
    chol_color = "orange"
else:
    chol_risk = "High"
    chol_color = "red"

# -----------------------------
# Display Results
# -----------------------------
st.header("Your Health Summary")

st.subheader("BMI")
st.markdown(f"<span style='color:{bmi_color}; font-weight:bold'>{bmi:.1f} ({bmi_category})</span>", unsafe_allow_html=True)

st.subheader("Blood Pressure")
st.markdown(f"<span style='color:{bp_color}; font-weight:bold'>{systolic_bp}/{diastolic_bp} mmHg ({bp_risk})</span>", unsafe_allow_html=True)

st.subheader("Cholesterol")
st.markdown(f"<span style='color:{chol_color}; font-weight:bold'>{cholesterol} mg/dL ({chol_risk})</span>", unsafe_allow_html=True)

# -----------------------------
# Health Tips
# -----------------------------
st.header("Health Tips")
tips = []

if bmi >= 25:
    tips.append("Consider a balanced diet and regular exercise to manage your weight.")
if bp_risk in ["Elevated", "High (Stage 1)", "High (Stage 2)"]:
    tips.append("Monitor your blood pressure regularly and reduce salt intake.")
if chol_risk in ["Borderline High", "High"]:
    tips.append("Eat a heart-healthy diet and exercise regularly to lower cholesterol.")

if tips:
    for tip in tips:
        st.markdown(f"✅ {tip}")
else:
    st.markdown("🎉 All your metrics are within healthy ranges! Keep it up.")

# -----------------------------
# Prepare Results for Download
# -----------------------------
results_df = pd.DataFrame({
    "Metric": ["BMI", "BMI Category", "Systolic BP", "Diastolic BP", "BP Risk", "Cholesterol", "Cholesterol Risk"],
    "Value": [f"{bmi:.1f}", bmi_category, systolic_bp, diastolic_bp, bp_risk, cholesterol, chol_risk]
})
st.header("Download Your Health Summary")

st.download_button(
    label="📥 Download Results as CSV",
    data=results_df.to_csv(index=False),
    file_name="chronic_disease_results.csv",
    mime="text/csv"
)

# -----------------------------
# Simple Visualization
# -----------------------------
st.header("Metric Overview")

metrics = pd.DataFrame({
    "Metric": ["BMI", "Systolic BP", "Diastolic BP", "Cholesterol"],
    "Value": [bmi, systolic_bp, diastolic_bp, cholesterol]
})

st.bar_chart(metrics.set_index("Metric"))


