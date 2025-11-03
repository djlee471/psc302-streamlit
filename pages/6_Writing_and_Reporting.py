# ─────────────────────────────────────────────────────────────────────────────
# pages/6_Writing_and_Reporting.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import module_chat_ui, render_header
from utils.prompts import INTRO_WR
import streamlit as st

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""


st.set_page_config(page_title="Writing & Reporting", page_icon="📝", layout="wide")
render_header("Module 6 — Writing & Reporting", "Clear, honest claims without overreach.")


starter = (
"**Goal:** Draft a short, sober results paragraph (hypothetical).\n\n"
"**Coach prompts:** Scope conditions, limitations, effect sizes, and policy relevance."
)


module_chat_ui(
module_key="wmodule",
prompt_hint="Draft a 3-sentence results paragraph and list one limitation…",
starter=starter,
)