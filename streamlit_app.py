import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Id Prediction App", layout="centered")

st.title("Nano-Wire FET Id Prediction App")
st.markdown("Enter the following parameters to predict the Drain Current (Id):")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load('rf_regressor_model_comp.pkl')
    return model

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file not found. Make sure 'randomf_model_comp1.pkl' is in the same directory.")
    st.stop()

# -----------------------------
# Input Fields - Linear Layout (No Columns)
# -----------------------------
st.header("Input Parameters")

Vg = st.number_input("Gate Voltage (Vg)", value=0.2, step=0.1)
gate_length = st.number_input("Gate Length (nm)",  min_value=4.0, max_value=10.0, step=0.1)
tox = st.number_input("Oxide Thickness (tox)", min_value=3.0, max_value=8.0, step=0.1)
sides = st.number_input("Number of Sides",min_value=3, max_value=8, step=1)
trap = st.selectbox("Trap Charge Present?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
work_function = st.number_input("Work Function (eV)", min_value=4.3, max_value=5.0, step=0.1)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🔍 Predict Id"):
    # Create DataFrame for prediction
    input_data = pd.DataFrame({
        'Vg': [Vg],
        'gate_length': [gate_length],
        'tox': [tox],
        'sides': [sides],
        'trap': [trap],
        'work_function': [work_function]
    })

    # Make prediction
    predicted_id = model.predict(input_data)[0]

    # Display result
    st.success(f"✅ Predicted Drain Current (`Id`): **{predicted_id:} mA**")