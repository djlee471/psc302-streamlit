# ─────────────────────────────────────────────────────────────────────────────
# pages/2_Hypothesis_Design.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import module_chat_ui, render_header
from utils.prompts import INTRO_HYP
import streamlit as st

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""


st.set_page_config(page_title="Hypothesis Design", page_icon="🧠", layout="wide")
render_header("Module 2 — Hypothesis Design", "Turn ideas into testable causal claims.")


starter = (
"**Goal:** Draft a precise, directional, falsifiable hypothesis.\n\n"
"**Coach prompts:** Identify IV→DV direction, mechanism, and rival explanations."
)


module_chat_ui(
module_key="hypmodule",
prompt_hint="Write your one-sentence hypothesis and why it is causal…",
starter=starter,
)