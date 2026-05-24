
import streamlit as st
import requests
import time

st.set_page_config(page_title="Retail Intelligence Chatbot", page_icon="🛒", layout="wide")

if "messages"  not in st.session_state: st.session_state.messages  = []
if "api_key"   not in st.session_state: st.session_state.api_key   = ""
if "lang"      not in st.session_state: st.session_state.lang      = "FR"

GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_URL   = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPTS = {
    "FR": "Tu es un expert retail analytics. Tu analyses des données de segmentation client RFM et clustering K-Means pour un retailer UK (UCI Online Retail 2010-2011). Réponds en français de façon claire et structurée.",
    "EN": "You are a retail analytics expert. You analyse RFM customer segmentation and K-Means clustering data for a UK retailer (UCI Online Retail 2010-2011). Respond in English clearly and professionally."
}

PROMPTS = {
    "FR": {
        "title": "🛒 Assistant Retail Intelligence",
        "key_ph": "Entrez votre clé API Groq pour commencer",
        "key_help": "Obtenez-la sur [console.groq.com](https://console.groq.com/keys)",
        "save_key": "Valider la clé",
        "welcome": "Bonjour ! Je suis votre analyste retail. Comment puis-je vous aider ?",
        "chat_ph": "Posez votre question (ex: Quels sont les clusters à risque ?)",
        "err_key": "Veuillez entrer une clé API valide.",
        "err_api": "Erreur de l'API. Vérifiez votre clé."
    },
    "EN": {
        "title": "🛒 Retail Intelligence Assistant",
        "key_ph": "Enter your Groq API Key to begin",
        "key_help": "Get yours at [console.groq.com](https://console.groq.com/keys)",
        "save_key": "Save Key",
        "welcome": "Hello! I am your retail analyst. How can I help you today?",
        "chat_ph": "Ask a question (e.g. Which clusters are at risk of churning?)",
        "err_key": "Please enter a valid API Key.",
        "err_api": "API Error. Check your key."
    }
}

st.sidebar.markdown(f"### {PROMPTS[st.session_state.lang]['title']}")
st.sidebar.selectbox("Language / Langue", ["FR", "EN"], key="lang")
p = PROMPTS[st.session_state.lang]

if not st.session_state.api_key:
    a_key = st.sidebar.text_input(p["key_ph"], type="password", help=p["key_help"])
    if st.sidebar.button(p["save_key"]):
        if a_key.startswith("gsk_"): 
            st.session_state.api_key = a_key
            st.rerun()
        else:
            st.sidebar.error(p["err_key"])

if st.session_state.api_key:
    if not st.session_state.messages:
        st.session_state.messages.append({"role": "assistant", "content": p["welcome"]})

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_q = st.chat_input(p["chat_ph"])
    if user_q:
        st.session_state.messages.append({"role": "user", "content": user_q})
        with st.chat_message("user"): st.markdown(user_q)

        with st.chat_message("assistant"):
            phs = st.empty()
            phs.markdown("⏳ Analyse...")

            headers = {
                "Authorization": f"Bearer {st.session_state.api_key}",
                "Content-Type": "application/json"
            }

            # Concaténation de l'historique
            payload_msgs = [{"role": "system", "content": SYSTEM_PROMPTS[st.session_state.lang]}]
            payload_msgs.extend([{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[-5:]])

            payload = {
                "model": GROQ_MODEL,
                "messages": payload_msgs,
                "temperature": 0.3
            }

            try:
                res = requests.post(GROQ_URL, headers=headers, json=payload)
                if res.status_size == 200:
                    ans = res.json()["choices"][0]["message"]["content"]
                    phs.markdown(ans)
                    st.session_state.messages.append({"role": "assistant", "content": ans})
                else:
                    phs.error(f"{p['err_api']} ({res.status_code})")
            except Exception as e:
                phs.error(f"{p['err_api']} : {str(e)}")
