# Customer Segmentation & Recommendation System

## Overview
This repository contains an end-to-end retail data analytics workflow using the UCI Online Retail dataset. It focuses on understanding customer behavior through data science and making those insights accessible via a generative AI chatbot.

The project features a full exploratory data analysis (EDA), **RFM (Recency, Frequency, Monetary)** analysis, and **K-Means Clustering** built in Jupyter Notebooks. Additionally, it includes a multilingual (FR/EN) **Streamlit web application** powered by the **Groq API (Llama 3)**, allowing users to interactively query customer segments, cluster behaviors, and churn risks using natural language.

## Features
- **Data Preprocessing & EDA:** Comprehensive cleaning and narrative exploratory data analysis to build business intuition.
- **RFM Analysis:** Scoring customers based on their purchasing habits (Recency, Frequency, Monetary value).
- **Customer Segmentation:** Applying K-Means clustering on the RFM scores to identify distinct behavioral groups (e.g., Champions, Loyal Customers, At-Risk).
- **Interactive AI Chatbot (`app.py`):** A Streamlit interface that leverages `llama-3.3-70b-versatile` via Groq to answer natural language questions about the retail data and segmentation results.

## Tech Stack
- **Data Science:** Python, Pandas, Scikit-Learn, Plotly
- **Web Interface:** Streamlit
- **AI/LLM:** Groq API (Llama 3)
- **Environment:** Jupyter Notebooks (`.ipynb`)

## How to Run the Web App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fedi-Jouili/Customer-Segmentation-Recommendation-System.git
   cd Customer-Segmentation-Recommendation-System
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install streamlit pandas groq requests plotly scikit-learn
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. **Add your API Key:**
   When the app opens in your browser, enter your Groq API key in the sidebar to start asking questions about the customer segments!

## Project Structure
- `app.py`: The main Streamlit application code.
- `Atelier_version_amélioré.ipynb`: The main notebook containing the data processing, mathematical modeling, and clustering logic.
- *Data files (excluded from repo)*: The original `.xlsx` constraints, `.csv` exports, and generated summaries are kept local using `.gitignore`.
