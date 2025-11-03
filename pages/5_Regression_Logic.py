# ─────────────────────────────────────────────────────────────────────────────
# pages/5_Regression_Logic.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import module_chat_ui, render_header
from utils.prompts import INTRO_REG
import streamlit as st

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

st.set_page_config(page_title="Regression Logic", page_icon="📈", layout="wide")
render_header("Module 5 — Regression Logic (Interpretation Only)", "What coefficients mean conceptually; no computation here.")


starter = (
"**Goal:** Practice interpretation of coefficients, SEs, p-values, and model fit.\n\n"
"**Coach prompts:** Omitted variable bias, sign/direction, magnitude vs significance."
)


module_chat_ui(
module_key="rmodule",
prompt_hint="Explain how you’d interpret a positive, significant coefficient on your IV…",
starter=starter,
)