# ─────────────────────────────────────────────────────────────────────────────
# pages/3_Variable_Measurement.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import module_chat_ui, render_header

# -----------------------------------------------------------------------------
# Page setup
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Variable Measurement", page_icon="📏", layout="wide")

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

render_header("Module 3 — Variable Measurement", "Operationalize concepts into data.")

starter = (
    "**Goal:** Define IV and DV and propose concrete measurements.\n\n"
    "**Coach prompts:** Levels of measurement, reliability, validity, bias, and proxies."
)

# -----------------------------------------------------------------------------
# Tutor chat interface (auto-logging handled inside module_chat_ui)
# -----------------------------------------------------------------------------
module_chat_ui(
    module_key="Variable Measurement",
    prompt_hint="Name your IV and DV and propose specific measurements…",
    starter=starter,
)
