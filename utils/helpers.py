# ─────────────────────────────────────────────────────────────────────────────
# utils/helpers.py — shared utility functions for PSC 302 Streamlit Tutor
# ─────────────────────────────────────────────────────────────────────────────

from typing import List, Dict
import streamlit as st
from openai import OpenAI
import tiktoken

# -----------------------------------------------------------------------------
# Core system message and keyword triggers
# -----------------------------------------------------------------------------
SYSTEM_CORE = (
    "You are a patient, Socratic research methods tutor for PSC 302. "
    "You never write full assignments. You ask probing questions, explain tradeoffs, "
    "and keep the student doing the substantive reasoning. "
    "If the student requests recent literature, "
    "you recommend using Web GPT (external browsing) and provide a copy-ready prompt."
)

KEYWORDS_BROWSE = [
    "literature", "recent", "2024", "2025", "study", "journal",
    "meta-analysis", "systematic review", "DOI", "replication"
]

# -----------------------------------------------------------------------------
# Session setup
# -----------------------------------------------------------------------------
def ensure_session():
    """Initialize session state variables if not present."""
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "model" not in st.session_state:
        st.session_state.model = "gpt-4o-mini"
    if "histories" not in st.session_state:
        st.session_state.histories = {}

# -----------------------------------------------------------------------------
# API key management (safe per-session persistence)
# -----------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def _cached_key(k: str):
    """Cache API key for this browser session only."""
    return k

def get_api_key() -> str:
    """Retrieve API key from session or short-term cache."""
    if "api_key" in st.session_state and st.session_state.api_key:
        return st.session_state.api_key.strip()
    if st.session_state.get("temp_api_key"):
        return _cached_key(st.session_state.temp_api_key)
    return ""

def get_client() -> OpenAI | None:
    """Return OpenAI client using persistent per-session key."""
    key = get_api_key()
    if not key:
        st.warning("Enter your OpenAI API key on the home page to enable the tutor.")
        return None
    try:
        return OpenAI(api_key=key)
    except Exception as e:
        st.error(f"Error creating OpenAI client: {e}")
        return None

# -----------------------------------------------------------------------------
# Utility: token counting
# -----------------------------------------------------------------------------
def token_len(text: str, model: str = "gpt-4o-mini") -> int:
    """Count tokens for given text/model."""
    try:
        enc = tiktoken.encoding_for_model(model)
    except Exception:
        enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

# -----------------------------------------------------------------------------
# Core chat function
# -----------------------------------------------------------------------------
def send_chat(messages: List[Dict[str, str]], temperature: float = 0.3) -> str:
    """Send a chat completion request to OpenAI safely."""
    client = get_client()
    if client is None:
        return ""

    model = st.session_state.get("model", "gpt-4o-mini")

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return resp.choices[0].message.content

    except Exception as e:
        if "401" in str(e) or "invalid_api_key" in str(e).lower():
            st.error("❌ Your OpenAI API key appears invalid or expired. Please check and re-enter it on the home page.")
        else:
            st.error(f"OpenAI error: {e}")
        return ""

# ----------------------------------------------------------------------------- 
# Chat interface for each module (auto-logging only)
# -----------------------------------------------------------------------------
from datetime import datetime

def module_chat_ui(module_key: str, prompt_hint: str, starter: str = ""):
    """Display module chat UI and record each exchange in conversation_log."""
    history = st.session_state.histories.setdefault(module_key, [])

    # Show starter text first (Goal / Coach prompts)
    if starter and not history:
        history.append({"role": "assistant", "content": starter})

    # 👉 Now introduce the dialogue area
    st.subheader("Your Dialogue")

    # Display conversation so far
    for msg in history:
        st.chat_message(msg["role"]).markdown(msg["content"])

    # New user input
    u = st.chat_input(prompt_hint)
    if u:
        st.chat_message("user").markdown(u)
        history.append({"role": "user", "content": u})

        messages = [{"role": "system", "content": SYSTEM_CORE}] + history
        reply = send_chat(messages)

        if reply:
            st.chat_message("assistant").markdown(reply)
            history.append({"role": "assistant", "content": reply})

            # ✅ Auto-log prompt + reply in conversation_log
            if "conversation_log" not in st.session_state:
                st.session_state["conversation_log"] = []
            st.session_state["conversation_log"].append({
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "module": module_key,
                "prompt": u,
                "response": reply,
                "type": "interaction",
            })

    st.session_state.histories[module_key] = history


# -----------------------------------------------------------------------------
# Page helpers
# -----------------------------------------------------------------------------
def render_header(title: str, subtitle: str = ""):
    st.title(title)
    if subtitle:
        st.caption(subtitle)

def render_webgpt_banner():
    st.info(
        "**Need recent studies or factual retrieval?** Click to open Web GPT (browsing). "
        "Then paste citations back here."
    )
    cols = st.columns([1, 1])
    with cols[0]:
        st.link_button("Open Web GPT", "https://chat.openai.com/?model=o4-mini-2024-08-06")
    with cols[1]:
        st.link_button("Open Google Scholar", "https://scholar.google.com")

# ----------------------------------------------------------------------------- 
# Logging helper (for saving prompts, responses, and notes)
# -----------------------------------------------------------------------------
from datetime import datetime

def log_interaction(module: str, prompt: str, response: str = "", note_type: str = "interaction"):
    """
    Save a prompt–response or note entry into session_state["conversation_log"].
    
    Parameters
    ----------
    module : str
        The module name or section (e.g., 'Sampling & Inference').
    prompt : str
        The student input or description.
    response : str, optional
        The model's output or notes.
    note_type : str, optional
        Type label (e.g., 'interaction', 'notes', 'custom_prompt').
    """
    if "conversation_log" not in st.session_state:
        st.session_state["conversation_log"] = []
    st.session_state["conversation_log"].append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "module": module,
        "type": note_type,
        "prompt": prompt,
        "response": response,
    })
