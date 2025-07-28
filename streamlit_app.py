import streamlit as st

# Title
st.title("Biological Age Calculator")

# Prompt user for input variables
chron_age = st.number_input("Chronological Age", min_value=20, max_value=100, value=73)
sex = st.selectbox("Sex", ["M", "F"])
ethnicity = st.selectbox("Ethnicity", ["White", "Black", "Hispanic", "Asian", "Other"])
sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=12.0, value=6.5)
vo2 = st.number_input("VO2 Max", min_value=10.0, max_value=80.0, value=46.0)
grip = st.number_input("Hand Grip Strength (lbs)", min_value=0, max_value=200, value=86)
sit_stand = st.number_input("30-second Sit-to-Stand Repetitions", min_value=0, max_value=60, value=20)
waist = st.number_input("Waist Circumference (inches)", min_value=20, max_value=70, value=34)
height = st.number_input("Height (inches)", min_value=50, max_value=84, value=70)
weight = st.number_input("Weight (lbs)", min_value=70, max_value=400, value=169)
sbp = st.number_input("Systolic BP", min_value=80, max_value=200, value=120)
dbp = st.number_input("Diastolic BP", min_value=40, max_value=120, value=90)
glucose = st.number_input("Fasting Glucose", min_value=50.0, max_value=200.0, value=103.0)
a1c = st.number_input("HbA1c", min_value=4.0, max_value=12.0, value=5.8)
crp = st.number_input("CRP", min_value=0.0, max_value=10.0, value=0.4)
creatinine = st.number_input("Creatinine", min_value=0.3, max_value=2.0, value=1.1)
exercise = st.selectbox("Exercise Level", ["None", "Low", "Moderate", "High"])
stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])
alcohol = st.selectbox("Alcohol Use", ["Never", "Occasional", "Regular"])
smoking = st.selectbox("Smoking Status", ["Never", "Past", "Current"])
ldl = st.number_input("LDL Cholesterol", min_value=20, max_value=300, value=126)
hdl = st.number_input("HDL Cholesterol", min_value=10, max_value=150, value=55)
cac = st.number_input("Coronary Artery Calcium Score", min_value=0, max_value=1000, value=0)
bun = st.number_input("BUN", min_value=1.0, max_value=50.0, value=15.0)
bun_creatinine_ratio = bun / creatinine if creatinine else 0

# Placeholder calculation
bio_age = chron_age  # You can later replace this with your final algorithm
if cac == 0:
    cardiac_risk_modifier = -5  # override LDL impact
else:
    cardiac_risk_modifier = int((ldl - 100) / 10)

bio_age += (
    (6.5 - sleep) * 0.5
    - (vo2 - 30) * 0.2
    - (grip - 40) * 0.05
    - (sit_stand - 10) * 0.3
    + (waist - 34) * 0.2
    + (sbp - 120) * 0.05
    + (glucose - 100) * 0.1
    + (a1c - 5.4) * 4
    + (crp - 0.3) * 2
    + (creatinine - 1) * 3
    + cardiac_risk_modifier
)

# Output
st.subheader(f"Estimated Biological Age: {bio_age:.1f} years")
