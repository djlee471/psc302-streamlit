# ─────────────────────────────────────────────────────────────────────────────
# pages/7_AI_Research_Workflow.py
# PSC 302 — Tier 2: AI Research Workflow
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
from utils.helpers import render_header, log_interaction

st.set_page_config(page_title="AI Research Workflow", page_icon="🧠", layout="wide")

# -----------------------------------------------------------------------------
# 1. Header + purpose
# -----------------------------------------------------------------------------
render_header("Module 7 — AI Research Workflow", "Using AI responsibly for research tasks")

st.markdown("""
This module helps you use AI **responsibly and effectively** for real research tasks —
not to write your paper, but to guide your **literature review, data discovery,**
and **question refinement**.

Here, you’ll learn how to design your own prompts and reflect on what you find.
""")

st.divider()

# -----------------------------------------------------------------------------
# 2. Instructional section — how to craft good prompts
# -----------------------------------------------------------------------------
st.subheader("🎯 How to Craft Effective Research Prompts")

st.markdown("""
When designing a prompt for ChatGPT (or Perplexity, Claude, etc.), try to include most or all of these elements:

| Element | Description | Example |
|----------|--------------|----------|
| **Persona** | Who the model should act as | “You are a political science research assistant.” |
| **Task** | The specific action | “Summarize 3 peer-reviewed studies on campaign finance reform.” |
| **Format** | Desired output style | “Use APA-style citations with DOI links.” |
| **Context** | Background or goal | “This is for a PSC 302 research design paper.” |
| **References / Scope** | Keywords, authors, or time frame | “Focus on studies from 2020–2025.” |

You can mix these into one concise paragraph prompt.
""")

st.info("💡 Example: *You are a political science research assistant. Summarize 2–3 peer-reviewed studies (2020–2025) on how campaign finance laws affect incumbent advantage, using APA-style citations with DOI links.*")

st.divider()

# -----------------------------------------------------------------------------
# 3. Step 1 — Student creates their own prompt
# -----------------------------------------------------------------------------
st.subheader("✍️ Step 1: Write Your Own Prompt")

user_prompt = st.text_area(
    "Write your full AI prompt here:",
    placeholder="Example: You are a political science research assistant..."
)

if user_prompt.strip():
    log_interaction("AI Research Workflow", user_prompt, note_type="custom_prompt")

st.divider()

# -----------------------------------------------------------------------------
# 4. Step 2 — Paste citations, summaries, or notes
# -----------------------------------------------------------------------------
st.subheader("📚 Step 2: Paste Literature Review Notes")

notes = st.text_area(
    "After using your prompt in ChatGPT (with browsing) or Perplexity, paste your citations or summaries below:",
    placeholder="Paste your APA citations or notes here..."
)

if notes.strip():
    log_interaction("AI Research Workflow", notes, note_type="notes")

st.divider()

# -----------------------------------------------------------------------------
# 5. Footer note
# -----------------------------------------------------------------------------
st.markdown("""
---
**Reminder:** Your data stay local in this browser session.  
Use this space to think critically about what you find — not to automate writing.
""")
