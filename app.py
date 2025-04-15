import streamlit as st
import numpy as np
import joblib

# Load the model and label encoder
model = joblib.load('randomf_model_comp.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Now you can use model.predict(...) as usual

st.title("Nano-Wire FET Id Prediction App")

st.markdown("Enter the following parameters to predict the Drain Current (Id):")

# User inputs
vg_input = st.number_input("Vg (in V)", min_value=0.0, max_value=2.0, step=0.1)
gate_input = st.number_input("Gate Length (nm)", min_value=4.0, max_value=10.0, step=0.1)
tox_input = st.number_input("Tox", min_value=3.0, max_value=8.0, step=0.1)
side_input = st.number_input("Number of Sides", min_value=3, max_value=8, step=1)
trap_input = st.selectbox("Trap Charge Present?", ["No", "Yes"])
trap_input_val = 1.0 if trap_input == "Yes" else 0.0
work_function_input = st.number_input("Work Function (eV)", min_value=4.3, max_value=5.0, step=0.1)

if st.button("Predict Id"):
    # Direct input to model (no scaling)
    custom_input = np.array([[vg_input, gate_input, tox_input, side_input, trap_input_val, work_function_input]])
    
    predicted_class_index = model.predict(custom_input)[0]
    predicted_label = label_encoder.inverse_transform([predicted_class_index])[0]

    st.success(f"Predicted Id Class: {predicted_label}")