import gradio as gr
import joblib
import numpy as np

# Load trained model and scaler
classifier = joblib.load("diabetees.joblib")
scaler = joblib.load("scaler.joblib")

# Prediction function
def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness,
                     Insulin, BMI, DiabetesPedigreeFunction, Age):
    
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = classifier.predict(input_scaled)[0]
    return "Diabetic" if prediction == 1 else "Not Diabetic"

# Gradio Interface
interface = gr.Interface(
    fn=predict_diabetes,
    inputs=[
        gr.Number(label="Pregnancies"),
        gr.Number(label="Glucose"),
        gr.Number(label="Blood Pressure"),
        gr.Number(label="Skin Thickness"),
        gr.Number(label="Insulin"),
        gr.Number(label="BMI"),
        gr.Number(label="Diabetes Pedigree Function"),
        gr.Number(label="Age"),
    ],
    outputs="text",
    title="Diabetes Prediction App",
    description="Enter patient data to predict whether they are diabetic using an SVM classifier."
)

interface.launch()
