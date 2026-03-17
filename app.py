import streamlit as st
from groq import Groq

# --- SECURITY: Load API Key from Streamlit Secrets ---
# You must add GROQ_API_KEY in your Streamlit Cloud Dashboard settings
try:
    API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=API_KEY)
except Exception:
    st.error("⚠️ API Key not found! Please add it to Streamlit Secrets.")
    st.stop()

# --- PAGE SETTINGS ---
st.set_page_config(
    page_title="MailWise AI | Global SaaS",
    page_icon="🤖",
    layout="wide"
)

# --- CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTextArea textarea { font-size: 16px !important; border-radius: 10px; }
    .success-box { 
        padding: 20px; 
        border-radius: 10px; 
        background-color: #ffffff;
        border-left: 5px solid #007bff;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🚀 MailWise AI")
    st.write("Professional Email Intelligence for Global Businesses.")
    st.divider()
    st.info("Version 1.1 - Secure Edition")

# --- MAIN INTERFACE ---
st.title("📨 AI Business Email Assistant")
st.write("Automatically summarize complex emails and generate high-quality replies.")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Email")
    email_text = st.text_area(
        "Paste the email content below:",
        height=350,
        placeholder="Dear Management, I am writing to..."
    )
    
    process_btn = st.button("🚀 Analyze & Generate Draft", use_container_width=True)

with col2:
    st.markdown("### ⚡ AI Intelligence Output")
    
    if process_btn:
        if email_text:
            with st.spinner("Llama 3.3 AI is processing..."):
                try:
                    # PROMPT LOGIC
                    system_msg = "You are a senior executive assistant. Provide a Summary, Tone analysis, and a Professional Reply."
                    user_msg = f"Analyze this email:\n\n{email_text}"

                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": system_msg},
                            {"role": "user", "content": user_msg}
                        ],
                        temperature=0.7
                    )

                    ai_response = completion.choices[0].message.content
                    
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.markdown(ai_response)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"AI Processing Error: {e}")
        else:
            st.warning("Please enter an email first.")

# --- FOOTER ---
st.divider()
st.caption("© 2025 MailWise AI | Scalable SaaS Solution")