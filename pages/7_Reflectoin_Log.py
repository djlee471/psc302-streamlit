# ─────────────────────────────────────────────────────────────────────────────
# pages/7_Reflection_Log.py
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import module_chat_ui, render_header
from utils.prompts import INTRO_REFLECT
import streamlit as st

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""


st.set_page_config(page_title="Reflection Log", page_icon="🪞", layout="wide")
render_header("Module 7 — Reflection Log", "Document ethical use and learning gains.")


starter = (
"**Goal:** Reflect on AI’s role in your learning.\n\n"
"**Coach prompts:** What did you verify? How did prompts evolve? What will you do differently next time?"
)


module_chat_ui(
module_key="reflectmodule",
prompt_hint="Write 3–5 bullets about how AI changed your understanding…",
starter=starter,
)