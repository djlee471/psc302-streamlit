# ─────────────────────────────────────────────────────────────────────────────
# app.py — Home + global sidebar
# PSC 302: Research Methods Tutor
# ─────────────────────────────────────────────────────────────────────────────

import streamlit as st
from utils.helpers import ensure_session, render_header, render_webgpt_banner

# -----------------------------------------------------------------------------
# Page setup
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="PSC 302 Tutor",
    page_icon="📚",
    layout="wide"
)

ensure_session()

render_header(
    title="PSC 302 — AI Research Methods Tutor",
    subtitle="Tier 1: Socratic coaching (no browsing). Tier 2: Web GPT for literature."
)

# -----------------------------------------------------------------------------
# How-to section
# -----------------------------------------------------------------------------
with st.expander("How to use this app", expanded=True):
    st.markdown(
        """
        **Welcome!** This tutor helps you practice *reasoning* in research methods.

        - Use the **sidebar** to navigate modules.
        - Enter your **OpenAI API key** below to enable the coach.
        - For literature or current events, the app will recommend you open **Web GPT**.
        - Paste your citations back here and we’ll help you interpret them.
        """
    )

st.divider()

# -----------------------------------------------------------------------------
# ✅ API key + model selection (safe, per-session, works across pages)
# -----------------------------------------------------------------------------
apikey = st.text_input(
    "Enter your OpenAI API key (kept only in your browser session)",
    type="password",
    key="api_key_input"
)

if apikey:
    # Store the key safely for this browser session only
    st.session_state["api_key"] = apikey.strip()
    st.session_state["temp_api_key"] = apikey.strip()
    st.success("✅ API key loaded! You can now use the tutor.")
else:
    st.info("🔑 Please enter your OpenAI API key above to start.")

# Model choice (for cost sensitivity)
model = st.selectbox(
    "Model (cost-sensitive):",
    ["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini"],
    index=0,
    key="model"
)

st.caption("Tip: 4o-mini is usually <$0.20 for the entire semester of light use.")

# -----------------------------------------------------------------------------
# Web GPT banner + modules overview
# -----------------------------------------------------------------------------
render_webgpt_banner()

st.markdown(
    """
    ### Modules
    Use the sidebar (left) to open:
    1. Scientific Method
    2. Hypothesis Design
    3. Variable Measurement
    4. Sampling & Inference
    5. Regression Logic (interpretation only)
    6. Writing & Reporting
    7. Reflection Log

    **Reminder:** This app is your *reasoning coach*. It won’t write your paper for you.
    """
)
