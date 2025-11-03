# ─────────────────────────────────────────────────────────────────────────────
# pages/6_Writing_and_Reporting.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import module_chat_ui, render_header

# -----------------------------------------------------------------------------
# Page setup
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Writing & Reporting", page_icon="📝", layout="wide")

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

render_header("Module 6 — Writing & Reporting", "Clear, honest claims without overreach.")

starter = (
    "**Goal:** Draft a short, sober results paragraph (hypothetical).\n\n"
    "**Coach prompts:** Scope conditions, limitations, effect sizes, and policy relevance."
)

# -----------------------------------------------------------------------------
# Tutor chat interface (auto-logging handled inside module_chat_ui)
# -----------------------------------------------------------------------------
module_chat_ui(
    module_key="Writing & Reporting",  # ← changed from 'wmodule'
    prompt_hint="Draft a 3-sentence results paragraph and list one limitation…",
    starter=starter,
)
