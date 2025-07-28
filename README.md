
# Diabetes Prediction 🩺🔍

A web-based machine learning application to predict the likelihood of diabetes in patients using health metrics. This project uses a trained Support Vector Machine (SVM) model and provides an interactive interface via **Gradio**.

---

## 🧠 Overview

This application takes input parameters such as glucose level, BMI, age, insulin level, and other medical data to predict whether a person is diabetic or not. It is built using Python, trained on the **Pima Indian Diabetes dataset**, and deployed with **Gradio** for real-time usage.

---

## 📁 Project Structure

```
Diabetes-Prediction/
│
├── diabetes_predictor.py          # Gradio interface to run the app
├── Project_3_Diabetes_Prediction.ipynb  # Jupyter notebook for training and analysis
├── diabetes.csv                   # Dataset used for model training
├── diabetees.joblib              # Trained SVM model
├── scaler.joblib                 # Scaler object for feature normalization
├── requirements.txt              # Required Python packages
└── README.md                     # Project documentation
```

---

## 🚀 Getting Started

### ✅ Prerequisites

Install Python 3.8 or higher and create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💡 How to Run the App

```bash
python diabetes_predictor.py
```

The Gradio web interface will open in your browser where you can enter patient details to get predictions.

---

## 📊 Model Details

- **Algorithm:** Support Vector Machine (SVM)
- **Scaler:** StandardScaler
- **Dataset:** `diabetes.csv` (Pima Indians Diabetes dataset)
- **Trained Features:**
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age

---

## 🧪 Example

Enter the following sample values to test the app:

- Glucose: 130  
- BMI: 28.1  
- Age: 45  
- ... (Fill in other values)

The model will return either `Diabetic` or `Not Diabetic`.

---

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Numpy / Pandas
- Gradio
- Joblib

---

## 📈 Future Improvements

- Add model performance metrics in the UI (accuracy, precision, recall).
- Improve UI with visualizations.
- Deploy on Hugging Face Spaces or Streamlit Cloud.

---

## 🙋‍♂️ Author

[Rohit Mondal](https://github.com/RohitMondal7)

---

## 📄 License

This project is licensed under the MIT License.
