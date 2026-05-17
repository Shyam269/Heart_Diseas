# Heart Disease Prediction Web App

An interactive web application built with Streamlit that utilizes a K-Nearest Neighbors (KNN) machine learning model to predict the risk of heart disease based on user-input clinical parameters. 

---

## 🚀 Features
* **Interactive UI:** Input clinical data effortlessly using custom sliders, select boxes, and numeric inputs.
* **Robust Pipeline:** Seamlessly scales user input using a pre-trained `StandardScaler` and matches the exact feature schema required by the model.
* **Instant Predictions:** Real-time feedback displaying either a high-risk warning or a low-risk confirmation.

---

## 📂 Project Structure
```text
├── KNN_heart.pkl          # Trained K-Nearest Neighbors model
├── scaler.pkl             # Trained Scaler object (StandardScaler)
├── columns.pkl            # Pickled list of trained feature column names (for One-Hot Encoding alignment)
├── app.py                 # Main Streamlit application script (your code)
└── README.md              # Project documentation
