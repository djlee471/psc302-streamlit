# ─────────────────────────────────────────────────────────────────────────────
# pages/4_Sampling_and_Inference.py
# PSC 302 Research Methods Tutor (Interactive)
# ─────────────────────────────────────────────────────────────────────────────

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.helpers import render_header, module_chat_ui

# -----------------------------------------------------------------------------
# Page setup
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Sampling and Inference", page_icon="📊", layout="wide")

# --- ensure per-page session key sync ---
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
render_header("Module 4 — Sampling and Inference",
              "From conceptual logic to basic statistical tests")

st.markdown(
"""
This module introduces the **logic of inference** — how we draw conclusions about
populations from samples. You’ll start by visualizing sampling error, then move
into interactive examples of hypothesis testing using *t*-statistics.
"""
)

st.divider()

# -----------------------------------------------------------------------------
# Sampling error visualization
# -----------------------------------------------------------------------------
st.subheader("🔢 Sampling Error in Action")

st.markdown(
"""
When we take a sample from a population, its mean will usually differ slightly
from the true population mean — just by chance. The spread of these sample means
represents **sampling error**.
"""
)

# population and sliders
pop_mean = 50
pop_sd = 10
population = np.random.normal(pop_mean, pop_sd, 10000)
sample_size = st.slider("Sample size (n)", 10, 500, 50, step=10)
n_samples = st.slider("Number of samples to draw", 10, 500, 100, step=10)

# draw repeated samples
sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(n_samples)]

st.write(f"Population mean ≈ {pop_mean:.2f}")
st.write(f"Mean of sample means ≈ {np.mean(sample_means):.2f}")
st.write(f"Standard error ≈ {np.std(sample_means):.2f}")

# clean dark-themed histogram
fig, ax = plt.subplots(figsize=(6, 4), facecolor="none")
ax.hist(sample_means, bins=25, color="#38bdf8", edgecolor="white", alpha=0.85)
for spine in ax.spines.values():
    spine.set_color("#e5e7eb")
ax.tick_params(colors="#e5e7eb", labelsize=8)
ax.xaxis.label.set_color("#e5e7eb")
ax.yaxis.label.set_color("#e5e7eb")
ax.title.set_color("#e5e7eb")
ax.set_xlabel("Sample Mean", fontsize=9)
ax.set_ylabel("Frequency", fontsize=9)
ax.set_title("Sampling Distribution of the Mean", fontsize=10, pad=6)
st.pyplot(fig, transparent=True)

st.caption(
"As n increases, the sampling distribution becomes tighter and more bell-shaped. "
"The spread (standard error) shrinks — meaning our estimates are more precise."
)

st.divider()

# -----------------------------------------------------------------------------
# One-Sample t-Test (Interactive)
# -----------------------------------------------------------------------------
st.subheader("🧮 One-Sample t-Test (Interactive)")

st.markdown(
"""
A one-sample *t*-test asks whether a single sample mean differs significantly
from a known or hypothesized population mean.

Formula: `t = (x̄ - μ₀) / (s / √n)`
"""
)

# --- Step 1: User inputs population parameters ---
col1, col2, col3 = st.columns(3)
with col1:
    mu_true = st.number_input("True population mean (μ)", value=50.0)
with col2:
    sigma_true = st.number_input("Population SD (σ)", value=10.0)
with col3:
    n = st.slider("Sample size (n)", 10, 500, 30, step=10)

# --- Step 2: Draw sample on demand ---
if st.button("🎲 Draw new sample"):
    sample = np.random.normal(mu_true, sigma_true, n)
    xbar = np.mean(sample)
    s = np.std(sample, ddof=1)
    se = s / np.sqrt(n)
    t_stat = (xbar - mu_true) / se

    # --- Step 3: Plot sample distribution ---
    fig, ax = plt.subplots(figsize=(6, 4), facecolor="none")
    ax.hist(sample, bins=20, color="#38bdf8", edgecolor="white", alpha=0.8)
    ax.axvline(mu_true, color="white", linestyle="--", linewidth=1.2, label="True Mean (μ)")
    ax.axvline(xbar, color="#f472b6", linestyle="-", linewidth=1.5, label="Sample Mean (x̄)")

    for spine in ax.spines.values():
        spine.set_color("#e5e7eb")
    ax.tick_params(colors="#e5e7eb", labelsize=8)
    ax.xaxis.label.set_color("#e5e7eb")
    ax.yaxis.label.set_color("#e5e7eb")
    ax.title.set_color("#e5e7eb")

    ax.set_xlabel("Sample Values", fontsize=9)
    ax.set_ylabel("Frequency", fontsize=9)
    ax.set_title("Sample Distribution", fontsize=10, pad=6)
    ax.legend(facecolor="none", edgecolor="none", labelcolor="#e5e7eb", fontsize=8)
    st.pyplot(fig, transparent=True)

    # --- Step 4: Display results ---
    st.write(f"Sample mean (x̄): **{xbar:.2f}**")
    st.write(f"Sample SD (s): **{s:.2f}**")
    st.write(f"Standard error (s/√n): **{se:.2f}**")
    st.write(f"t-statistic: **{t_stat:.2f}**")
    st.caption(
        "Interpretation: Even when the true mean equals μ, random samples will differ. "
        "The t-statistic shows how many standard errors this sample mean is from the true value."
    )

st.divider()

# -----------------------------------------------------------------------------
# Difference of Means Test (Interactive)
# -----------------------------------------------------------------------------
st.subheader("⚖️ Difference of Means Test (Interactive)")

st.markdown(
"""
A difference of means test compares two group means.  
Formula: `t = (x̄₁ - x̄₂) / sqrt(s₁²/n₁ + s₂²/n₂)`
"""
)

# --- Step 1: User inputs population parameters for both groups ---
col1, col2 = st.columns(2)
with col1:
    mu1 = st.number_input("Group 1 mean (μ₁)", value=50.0)
    sigma1 = st.number_input("Group 1 SD (σ₁)", value=10.0)
with col2:
    mu2 = st.number_input("Group 2 mean (μ₂)", value=52.0)
    sigma2 = st.number_input("Group 2 SD (σ₂)", value=10.0)

n_groups = st.slider("Sample size per group", 10, 500, 30, step=10)

# --- Step 2: Draw new samples ---
if st.button("🎲 Draw new group samples"):
    group1 = np.random.normal(mu1, sigma1, n_groups)
    group2 = np.random.normal(mu2, sigma2, n_groups)

    mean1, mean2 = np.mean(group1), np.mean(group2)
    s1, s2 = np.std(group1, ddof=1), np.std(group2, ddof=1)
    diff = mean1 - mean2
    se_diff = np.sqrt((s1**2 / n_groups) + (s2**2 / n_groups))
    t_diff = diff / se_diff

    # --- Step 3: Plot overlapping histograms ---
    fig, ax = plt.subplots(figsize=(6, 4), facecolor="none")
    ax.hist(group1, bins=20, color="#38bdf8", edgecolor="white", alpha=0.6, label="Group 1")
    ax.hist(group2, bins=20, color="#f472b6", edgecolor="white", alpha=0.6, label="Group 2")

    for spine in ax.spines.values():
        spine.set_color("#e5e7eb")
    ax.tick_params(colors="#e5e7eb", labelsize=8)
    ax.xaxis.label.set_color("#e5e7eb")
    ax.yaxis.label.set_color("#e5e7eb")
    ax.title.set_color("#e5e7eb")

    ax.set_xlabel("Values", fontsize=9)
    ax.set_ylabel("Frequency", fontsize=9)
    ax.set_title("Two Group Distributions", fontsize=10, pad=6)
    ax.legend(facecolor="none", edgecolor="none", labelcolor="#e5e7eb", fontsize=8)
    st.pyplot(fig, transparent=True)

    # --- Step 4: Display results ---
    st.write(f"Mean₁ = **{mean1:.2f}**, Mean₂ = **{mean2:.2f}**")
    st.write(f"Difference (x̄₁ - x̄₂): **{diff:.2f}**")
    st.write(f"Standard error of difference: **{se_diff:.2f}**")
    st.write(f"t-statistic: **{t_diff:.2f}**")
    st.caption(
        "Interpretation: The larger the t-statistic (in absolute value), the more confident we are "
        "that the two groups differ beyond random sampling variation."
    )

st.divider()

# -----------------------------------------------------------------------------
# Conceptual tie-back and Tutor chat
# -----------------------------------------------------------------------------
st.subheader("💬 Discuss with the Tutor")

st.markdown(
"""
These interactive tests show that **inference is just structured uncertainty**:
we use statistics like *t* to measure how far a sample estimate is from a null
expectation, in standard error units.
"""
)

starter = (
    "Let's discuss how sampling error leads to uncertainty, and how t-tests "
    "quantify whether observed differences are likely due to chance."
)

module_chat_ui(
    module_key="Sampling & Inference",  # ← clean, descriptive name for logs
    prompt_hint="Ask about sampling error, hypothesis tests, or p-values…",
    starter=starter
)
