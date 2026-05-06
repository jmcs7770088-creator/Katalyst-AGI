# Katalyst AI Stability Agent

## 🚀 Overview
Katalyst is a bounded-response stabilization engine designed to prevent runaway behavior in AI systems.

## 🧠 Core Idea
Instead of ignoring noise, the system constrains it using a bounded-response function:

f(x) = x / (1 + |x|)

This ensures:
- Stability under extreme inputs
- No divergence
- Predictable outputs

## ⚙️ Features
- Real-time stabilization demo
- Interactive UI
- Stability scoring
- Mirror-node simulation

## ▶️ Run Locally


pip install -r requirements.txt
streamlit run app.py