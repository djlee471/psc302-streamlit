# ─────────────────────────────────────────────────────────────────────────────
# pages/1_Scientific_Method.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import module_chat_ui, render_header
from utils.prompts import INTRO_SM

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

st.set_page_config(page_title="Scientific Method", page_icon="🔬", layout="wide")
render_header("Module 1 — Scientific Method", "What makes a claim *scientific* in political inquiry?")

starter = (
    "**Goal:** Articulate a political phenomenon, a theory, and a testable implication.\n\n"
    "**Coach promises:** I’ll ask for clarity on mechanisms, scope conditions, and falsifiability."
)

# -----------------------------------------------------------------------------
# Tutor chat interface (auto-logging handled inside module_chat_ui)
# -----------------------------------------------------------------------------
module_chat_ui(
    module_key="Scientific Method",  # ← changed from "smodule" for clean logs
    prompt_hint="Describe your phenomenon, theory, and a testable implication…",
    starter=starter,
)
