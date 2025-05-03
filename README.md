# Nano-Wire FET Id Prediction App

## 📌 Overview
This application predicts the **Drain Current (Id)** of a **Nano-Wire Field-Effect Transistor (FET)** based on user-provided input parameters. It is developed as a final-year project with the goal of providing an intuitive tool for simulating and predicting nano-scale transistor behavior for sub 10nm Multi-gate MOSFET device considering real life parameters such as trap charges.

---

## 🔧 Features
- **Input Parameters**: The app accepts the following inputs:
  - Gate Voltage (`Vg`)
  - Gate Length (in nanometers)
  - Oxide Thickness (`tox`)
  - Number of Sides
  - Trap Charge Present? (Yes/No)
  - Work Function (in eV)

- **Prediction**: Upon submitting the inputs, the app calculates and displays the predicted Drain Current (`Id`).

- **User-Friendly Interface**: Designed with simplicity and usability in mind.

---

## 🖼️ Screenshots
![App Screenshot](nano-wire.png)  
*Example of the app interface showing input fields and the prediction result.*

---

## 💻 Technologies Used
- **Backend**: Streamlit
- **Model**: XGBoost Machine Learning for predicting `Id`
- **Dataset**: Custom dataset built by simulating 300+ nano-devices in Synopsis TCAD.

---
## 🧪 How to Use
- Enter Input Parameters :
- Fill in all required input fields accurately.
- Ensure valid numerical values where applicable.
- Predict Id :
- Click the "Predict Id" button.
- The predicted Drain Current will appear below the form.

---
## Access the App
- Open your browser and go to:
- https://project-ii-nanowire.streamlit.app/

---

## 📬 Contact
For questions, feedback, or collaboration opportunities, feel free to reach out:

- GitHub : https://github.com/siddha-forever
- Email : mohapatra.siddhabrata@gmail.com
- LinkedIn : [https://www.linkedin.com/in/siddhabrata-mohapatra](https://www.linkedin.com/in/siddhabrata-mohapatra)

---

## 🙏 Acknowledgments
- Dataset source: Custom build
- Mentor - Faculty: Dr. Biswajit Jena
