# app.py
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load and preprocess the dataset
d = pd.read_csv("C:/Users/Rahav Ramkr/mlops2/Streamlitml/Medicaldataset.csv")
l = LabelEncoder()
d["Result"] = l.fit_transform(d["Result"])

# Define features and target variable
X = d.iloc[:,[0,1,2,3,4,5,6,7]]
y = d.iloc[:,-1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Initialize the Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the Decision Tree classifier
clf.fit(X_train, y_train)

# Define prediction function
def predict(age, gender, heart_rate, systolic_bp, diastolic_bp, blood_sugar, ck_mb, troponin):
    input_data = [[age, gender, heart_rate, systolic_bp, diastolic_bp, blood_sugar, ck_mb, troponin]]
    prediction = clf.predict(input_data)
    return l.inverse_transform(prediction)[0]

# Streamlit UI
st.title("Heart Disease Prediction")
st.write("Predicts heart disease outcome (positive/negative) based on various features.")

# Input components
age = st.number_input("Age", min_value=0, max_value=150, step=1)
gender = st.text_input("Gender (0 for female, 1 for male)")
heart_rate = st.number_input("Heart rate", min_value=0, max_value=300, step=1)
systolic_bp = st.number_input("Systolic blood pressure", min_value=0, max_value=300, step=1)
diastolic_bp = st.number_input("Diastolic blood pressure", min_value=0, max_value=300, step=1)
blood_sugar = st.number_input("Blood sugar", min_value=0.0, max_value=1000.0, step=0.1)
ck_mb = st.number_input("CK-MB", min_value=0.0, max_value=100.0, step=0.1)
troponin = st.number_input("Troponin", min_value=0.0, max_value=100.0, step=0.1)

# Prediction button
if st.button("Predict"):
    prediction = predict(age, gender, heart_rate, systolic_bp, diastolic_bp, blood_sugar, ck_mb, troponin)
    st.write(f"Predicted outcome: {prediction}")