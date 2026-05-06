import streamlit as st
from core.agent import run_agent

st.title("⚡ Katalyst AI Stability Agent")

value = st.slider("Input Signal", -1000.0, 1000.0, 0.0)

result = run_agent(value)

st.write("### Results")
st.write(f"Ω_G: {round(result['omega'], 6)}")
st.write(f"Stabilized Output: {round(result['stabilized'], 6)}")