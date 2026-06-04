import streamlit as st
import numpy as np
import pandas as pd
from itertools import combinations

# Site's name
st.set_page_config(page_title="Bibi's site 😼 !!!", page_icon="", layout="wide")

# Colors
COLOR_PRIMARY = "#97BDDA"   # Destaques (botões, medalhas, badges)
COLOR_BG      = "#2b2d42"   # Fundo geral
COLOR_TEXT    = "#edf2f4"   # Textos, títulos, labels
COLOR_SURFACE = "#4366b6"   # Fundo dos cards e inputs
COLOR_BORDER  = "#4978BF"   # Bordas
COULEURS_UI   = "#edf2f4"   # Cor da barra de progresso e header

#Fonts
FONT_TITLE = "Syne"          # Titles, headings, material names
FONT_MONO  = "Syne"    # Labels, badges, data, buttons
FONT_IMPORT_URL = "https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap"

# Font sizes
FS_XS    = "10px"   # Step labels, pair labels, sensitivity header labels
FS_SM    = "11px"   # Secondary info, metric labels, bar chart values
FS_BASE  = "12px"   # Buttons, widget labels, badges, dot labels, general body
FS_MD    = "13px"   # Input text, score values
FS_LG    = "15px"   # Pair names
FS_XL    = "18px"   # Silver/bronze podium medal emoji
FS_2XL   = "24px"   # Gold podium medal emoji
FS_TITLE = "clamp(26px,3.5vw,48px)"  # Page h1 headings

# Global CSS
st.markdown(f"""
<style>
@import url('{FONT_IMPORT_URL}');

*, *::before, *::after {{ box-sizing: border-box; }}
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ visibility: hidden; display: none; }}
section[data-testid="stSidebar"] {{ display: none; }}

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"], .main {{
    background: {COLOR_BG} !important;
    color: {COLOR_TEXT} !important;
    font-family: '{FONT_TITLE}', sans-serif;
}}
[data-testid="stAppViewContainer"] > div {{ background: {COLOR_BG} !important; }}
.block-container {{ padding: 2rem 6rem 4rem 6rem !important; max-width: 100% !important; }}

/* Buttons */
.stButton > button {{
    background: {COLOR_PRIMARY};
    color: {COLOR_BG};
    border: none; border-radius: 2px;
    font-family: '{FONT_MONO}', monospace; font-weight: 700; font-size: {FS_BASE};
    padding: 11px 24px; letter-spacing: .06em; text-transform: uppercase;
    width: 100%; cursor: pointer; transition: background .15s, transform .1s;
}}
.stButton > button:hover {{ filter: brightness(1.2); transform: translateY(-1px); }}
.stButton > button:active {{ transform: translateY(0); }}

/* Labels */
.stSelectbox label, .stNumberInput label, .stTextInput label,
.stMultiSelect label, .stRadio label, .stSlider label {{
    font-family: '{FONT_MONO}', monospace !important; font-size: {FS_BASE} !important;
    color: {COLOR_TEXT} !important; text-transform: uppercase; letter-spacing: .08em;
}}

/* Inputs */
.stSelectbox > div > div, .stTextInput > div > div > input,
.stNumberInput > div > div > input {{
    background: {COLOR_SURFACE} !important;
    border: 1px solid {COLOR_BORDER} !important;
    color: {COLOR_BG} !important; border-radius: 2px !important;
    font-family: '{FONT_MONO}', monospace !important; font-size: {FS_MD} !important;
}}

/* Multiselect */
.stMultiSelect > div > div {{
    background: {COLOR_SURFACE} !important;
    border: 1px solid {COLOR_BORDER} !important;
    border-radius: 2px !important;
}}
[data-baseweb="tag"] {{ background: {COLOR_BG} !important; border: 1px solid {COLOR_PRIMARY}44 !important; }}
[data-baseweb="tag"] span {{ color: {COLOR_PRIMARY} !important; font-family: '{FONT_MONO}', monospace !important; font-size: {FS_BASE} !important; }}

/* Dataframe */
[data-testid="stDataFrame"] {{ border: 1px solid {COLOR_BORDER}; border-radius: 3px; }}

/* Alerts */
.stSuccess > div {{ background: #0c1a0c !important; border: 1px solid #2a4a2a !important; }}
.stWarning > div {{ background: #1a160c !important; border: 1px solid #4a3a1a !important; }}
.stInfo > div    {{ background: #0c0e1a !important; border: 1px solid #1e2a4a !important; }}
.stError > div   {{ background: #1a0c0c !important; border: 1px solid #4a1e1e !important; }}

/* Progress bar */
[data-testid="stProgress"] > div {{ background: {COLOR_BORDER} !important; }}
[data-testid="stProgress"] > div > div {{ background: {COLOR_PRIMARY} !important; }}

/* Metrics */
[data-testid="stMetricValue"] {{ font-family: '{FONT_TITLE}', sans-serif !important; font-weight: 800 !important; color: {COLOR_PRIMARY} !important; }}
[data-testid="stMetricLabel"] {{ font-family: '{FONT_MONO}', monospace !important; font-size: {FS_BASE} !important; color: {COLOR_TEXT} !important; }}

/* Slider — styled, no tick labels */
div[data-testid="stSlider"] {{ margin-top: 8px !important; }}
div[data-testid="stSlider"] > div > div > div {{
    background: {COLOR_SURFACE}44 !important;
}}
div[data-testid="stSlider"] > div > div > div > div {{
    background: {COLOR_PRIMARY} !important;
}}
div[data-testid="stSlider"] [role="slider"] {{
    background: {COLOR_PRIMARY} !important;
    border: 2px solid {COLOR_BG} !important;
    box-shadow: 0 0 0 3px {COLOR_PRIMARY}55 !important;
}}
/* Hide ALL text/labels inside slider — keep only the track and handle */
div[data-testid="stSlider"] p,
div[data-testid="stSlider"] span,
div[data-testid="stSlider"] [data-testid="stTickBarMin"],
div[data-testid="stSlider"] [data-testid="stTickBarMax"],
div[data-testid="stSlider"] [class*="StyledThumbValue"],
div[data-testid="stSlider"] [class*="tickBar"],
div[data-testid="stSlider"] [class*="sliderValue"],
div[data-testid="stSlider"] > div > div > div + div,
div[data-testid="stSlider"] > div > div > div ~ div {{
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    height: 0 !important;
}}

/* Pair cards */
.pair-card {{
    background: {COLOR_BORDER}; border: 1px solid {COLOR_BORDER};
    border-radius: 4px; padding: 20px 24px; margin-bottom: 14px;
}}
.pair-label {{ font-family: '{FONT_MONO}', monospace; font-size: {FS_XS}; color: {COLOR_TEXT};
               text-transform: uppercase; letter-spacing: .12em; margin-bottom: 10px; }}
.pair-names {{ display: flex; justify-content: space-between; margin-bottom: 16px; }}
.pair-name  {{ font-family: '{FONT_TITLE}', sans-serif; font-weight: 700; font-size: {FS_LG}; color: {COLOR_PRIMARY};
               max-width: 44%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
.pair-vs    {{ font-family: '{FONT_MONO}', monospace; font-size: {FS_BASE}; color: {COLOR_TEXT}; align-self: center; }}
.val-badge  {{ font-family: '{FONT_MONO}', monospace; font-size: {FS_BASE}; font-weight: 700;
               color: {COLOR_PRIMARY}; text-align: center; margin-top: 10px; min-height: 18px; }}

/* Dots */
.dots-container {{ display: flex; align-items: center; justify-content: center; gap: 6px; flex-wrap: nowrap; }}
.dot {{
    width: 24px; height: 24px; border-radius: 50%; cursor: pointer;
    transition: transform .15s, background .15s;
    display: flex; align-items: center; justify-content: center;
    font-family: '{FONT_MONO}', monospace; font-size: {FS_BASE}; font-weight: 700;
    color: {COLOR_BG}; flex-shrink: 0;
}}
.dot:hover {{ transform: scale(1.3); }}
.dot-center {{ background: {COLOR_TEXT}44; width: 20px; height: 20px; }}
.dot-center.active {{ background: {COLOR_PRIMARY}; }}
.dot-left  {{ background: {COLOR_TEXT}22; }}
.dot-left.active  {{ background: {COLOR_PRIMARY}; }}
.dot-right {{ background: {COLOR_TEXT}22; }}
.dot-right.active {{ background: {COLOR_PRIMARY}; }}
.dot-label-row {{
    display: flex; justify-content: space-between;
    font-family: '{FONT_MONO}', monospace; font-size: {FS_BASE};
    color: {COLOR_TEXT}88; margin-top: 6px; padding: 0 2px;
}}
</style>
""", unsafe_allow_html=True)

# ── Constants ──────────────────────────────────────────────────────────────────

CRITERIA_META = {
    "Density (kg/m^3)":                             {"type": "cost",    "short": "Densidade"},
    "Young's modulus (GPa)":                        {"type": "benefit", "short": "Módulo de Young"},
    "Yield Strength (Mpa)":                         {"type": "benefit", "short": "Limite de Escoamento"},
    "Tensile Strength (MPa)":                       {"type": "benefit", "short": "Resistência a Tração"},
    "Elongation (%)":                               {"type": "benefit", "short": "Alongamento"},
    "Hardness Vickers (HV)":                        {"type": "benefit", "short": "Dureza de Vickers"},
    "Fatigue Strength at 10^7 cycles (MPa)":        {"type": "benefit", "short": "Resistência à Fadiga"},
    "Fracture Toughness (Mpa.m^0-5)":              {"type": "benefit", "short": "Tenacidade à fratura"},
    "Toughness (kJ/m^2)":                          {"type": "benefit", "short": "Tenacidade"},
    "Minimum Service Temperature (ºC)":             {"type": "cost",    "short": "Temperatura de Serviço Mínima"},
    "Thermal conductivity (W/m.ºC)":               {"type": "cost",    "short": "Condutividade Térmica"},
    "Thermal expansion Coefficient (strain/ºC)":   {"type": "cost",    "short": "Coeficiente de Expansão Térmica"},
    "Thermal Shock Resistance (ºC)":               {"type": "benefit", "short": "Resistência a Impacto Térmico"},
    "Thermal distortion Resistance (MW/m)":        {"type": "benefit", "short": "Resistência a Distorção Térmica"},
}

RI_TABLE = {1:0,2:0,3:.58,4:.90,5:1.12,6:1.24,7:1.32,8:1.41,9:1.45,
            10:1.49,11:1.51,12:1.54,13:1.56,14:1.57}

DOT_VALUES = [1/9,1/8,1/7,1/6,1/5,1/4,1/3,1/2,1,2,3,4,5,6,7,8,9]
DOT_LABELS = ["1/9","1/8","1/7","1/6","1/5","1/4","1/3","1/2","1","2","3","4","5","6","7","8","9"]

# Data
@st.cache_data
def load_data():
    df = pd.read_csv("materials.csv", header=1, index_col=0)
    df.index.name = "Material"
    df.columns = list(CRITERIA_META.keys())
    df = df.apply(pd.to_numeric, errors='coerce')
    return df.dropna(how='all')

MAT_DF        = load_data()
ALL_MATERIALS = list(MAT_DF.index)
ALL_CRITERIA  = list(CRITERIA_META.keys())

# ── Session state ──────────────────────────────────────────────────────────────
def init():
    for k, v in dict(step=1, sel_criteria=[], ahp_matrix=None,
                     weights=None, cr=None, lambda_max=None, ci=None,
                     method="TOPSIS").items():
        if k not in st.session_state:
            st.session_state[k] = v
init()

# Math

# AHP
def compute_ahp(matrix):
    n        = matrix.shape[0]
    norm     = matrix / matrix.sum(axis=0)
    weights  = norm.mean(axis=1)
    lambdas  = (matrix @ weights) / weights
    lmax     = lambdas.mean()
    ci       = (lmax - n) / (n - 1) if n > 1 else 0
    ri       = RI_TABLE.get(n, 1.57)
    cr       = ci / ri if ri > 0 else 0
    return weights, lmax, ci, cr

def topsis(values, weights, criteria):
    denom  = np.sqrt((values**2).sum(axis=0)); denom[denom==0] = 1e-9
    V      = (values / denom) * weights
    best   = np.array([V[:,j].min() if CRITERIA_META[c]["type"]=="cost" else V[:,j].max() for j,c in enumerate(criteria)])
    worst  = np.array([V[:,j].max() if CRITERIA_META[c]["type"]=="cost" else V[:,j].min() for j,c in enumerate(criteria)])
    d_b    = np.sqrt(((V - best)**2).sum(axis=1))
    d_w    = np.sqrt(((V - worst)**2).sum(axis=1))
    denom2 = d_b + d_w; denom2[denom2==0] = 1e-9
    return d_w / denom2

def wpm(values, weights, criteria):
    v = values.copy().astype(float)
    for j, c in enumerate(criteria):
        if CRITERIA_META[c]["type"] == "cost":
            m = v[:,j].max(); v[:,j] = (m if m != 0 else 1e-9) / v[:,j]
    v = np.where(v <= 0, 1e-9, v)
    return np.prod(v ** weights, axis=1)

# ── UI helpers ─────────────────────────────────────────────────────────────────
def page_header(step, title, sub=""):
    st.markdown(f"""
    <div style="padding:40px 0 0 0;">
      <div style="border-left:3px solid {COULEURS_UI};padding-left:20px;margin-bottom:28px;">
        <div style="font-family:'{FONT_MONO}',monospace;font-size:{FS_XS};color:{COULEURS_UI};
                    text-transform:uppercase;letter-spacing:.18em;margin-bottom:6px;">STEP {step} / 5</div>
        <h1 style="font-size:{FS_TITLE};font-weight:800;color:{COLOR_TEXT};
                   line-height:1.05;margin:0 0 6px 0;">{title}</h1>
        <p style="font-family:'{FONT_MONO}',monospace;font-size:{FS_XS};color:{COLOR_TEXT}88;margin:0;">{sub}</p>
      </div>
    </div>""", unsafe_allow_html=True)

def progress_bar(step):
    segs = "".join([
        f'<div style="flex:1;height:3px;background:{"' + COULEURS_UI + '" if i<=step else "' + COLOR_BORDER + '44"};border-radius:2px;"></div>'
        for i in range(1, 6)])
    st.markdown(f'<div style="display:flex;gap:6px;margin-bottom:32px;">{segs}</div>', unsafe_allow_html=True)

def wrap_open():
    pass  # margins handled by .block-container

def wrap_close():
    pass  # margins handled by .block-container

# ── Dot rating component ───────────────────────────────────────────────────────
def rating_dots(pair_idx, name_a, name_b):
    key = f"dot_{pair_idx}"
    if key not in st.session_state:
        st.session_state[key] = 8  # default = equal importance

    val   = st.session_state[key]
    ratio = DOT_VALUES[val]
    label = DOT_LABELS[val]

    if ratio == 1:
        val_text = "Equal importance (1)"
    elif ratio > 1:
        val_text = f"{name_b} is {label}× more important than {name_a}"
    else:
        val_text = f"{name_a} is {DOT_LABELS[16-val]}× more important than {name_b}"

    # Build dots HTML — purely visual, click handled by hidden slider below
    dots_html = ""
    for d in range(17):
        active = "active" if d == val else ""
        lbl    = DOT_LABELS[d] if d == val else ""
        if d == 8:
            cls = f"dot dot-center {active}"
        elif d < 8:
            cls = f"dot dot-left {active}"
        else:
            cls = f"dot dot-right {active}"
        dots_html += f'<div class="{cls}" title="{DOT_LABELS[d]}">{lbl}</div>'

    st.markdown(f"""
    <div class="pair-card">
      <div class="pair-label">PAIR {pair_idx+1}</div>
      <div class="pair-names">
        <span class="pair-name">{name_a}</span>
        <span class="pair-vs">vs</span>
        <span class="pair-name">{name_b}</span>
      </div>
      <div class="dots-container">{dots_html}</div>
      <div class="dot-label-row">
        <span>← {name_a} more important</span>
        <span>Equal</span>
        <span>{name_b} more important →</span>
      </div>
      <div class="val-badge">{val_text}</div>
    </div>""", unsafe_allow_html=True)

    # Slider is the actual interactive control (hidden via CSS)
    new_val = st.slider(
        f"Importance: {name_a} vs {name_b}",
        min_value=0, max_value=16,
        key=key,
        label_visibility="collapsed"
    )
    return new_val

# ── STEP 1 — Select Criteria ───────────────────────────────────────────────────
def step1():
    page_header(1, "Escolha as propriedades a serem consideradas")
    wrap_open()

    st.markdown(f"""
    <div style="background:{COLOR_SURFACE}22;border:1px solid {COLOR_BORDER}44;border-radius:4px;
                padding:14px 20px;margin-bottom:20px;">
      <span style="font-family:'{FONT_MONO}',monospace;font-size:{FS_BASE};color:{COLOR_TEXT}88;">Base de dados · </span>
      <span style="font-family:'{FONT_MONO}',monospace;font-size:{FS_BASE};color:{COLOR_PRIMARY};">
        {len(ALL_MATERIALS)} materiais · {len(ALL_CRITERIA)} propriedades disponíveis
      </span>
    </div>""", unsafe_allow_html=True)

    selected = st.multiselect(
        "Selecione as propriedades (mínimo 2)",
        options=ALL_CRITERIA,
        default=st.session_state.sel_criteria if st.session_state.sel_criteria else [],
        format_func=lambda x: f"{CRITERIA_META[x]['short']}  ({'↓ cost' if CRITERIA_META[x]['type']=='cost' else '↑ benefit'})",
        key="ms_criteria"
    )

    n = len(selected)
    if n > 0:
        st.markdown(f"""
        <div style="font-family:'{FONT_MONO}',monospace;font-size:{FS_BASE};color:{COLOR_PRIMARY};margin:12px 0;">
          {n} criteria selected → {n*(n-1)//2} pairwise comparisons
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Continue →", key="s1btn"):
        if n < 2:
            st.error("Selecione 2+ propriedades.")
        else:
            st.session_state.sel_criteria = selected
            prev = st.session_state.ahp_matrix
            if prev is None or prev.shape[0] != n:
                st.session_state.ahp_matrix = np.ones((n, n))
                for k in list(st.session_state.keys()):
                    if k.startswith("dot_"):
                        del st.session_state[k]
            st.session_state.step = 2
            st.rerun()
    wrap_close()

# ── STEP 2 — Pairwise Comparisons ─────────────────────────────────────────────
def step2():
    crits  = st.session_state.sel_criteria
    n      = len(crits)
    pairs  = list(combinations(range(n), 2))
    page_header(2, "Comparação de propriedades",
                f"Avalie a importância de cada par — {len(pairs)} comparisons")
    wrap_open()

    matrix = st.session_state.ahp_matrix.copy()
    for idx, (i, j) in enumerate(pairs):
        sa = CRITERIA_META[crits[i]]["short"]
        sb = CRITERIA_META[crits[j]]["short"]
        dot_idx       = rating_dots(idx, sa, sb)
        matrix[i, j]  = 1.0 / DOT_VALUES[dot_idx]
        matrix[j, i]  = DOT_VALUES[dot_idx]
    st.session_state.ahp_matrix = matrix

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([7, 1])
    with c1:
        if st.button("← Voltar", key="s2back"):
            st.session_state.step = 1; st.rerun()
    with c2:
        if st.button("Calcular pesos →", key="s2btn"):
            w, lmax, ci, cr           = compute_ahp(matrix)
            st.session_state.weights  = w
            st.session_state.lambda_max = lmax
            st.session_state.ci       = ci
            st.session_state.cr       = cr
            st.session_state.step     = 3
            st.rerun()
    wrap_close()

# ── STEP 3 — Weights & Method ──────────────────────────────────────────────────
def step3():
    crits      = st.session_state.sel_criteria
    weights    = st.session_state.weights
    cr         = st.session_state.cr
    lmax       = st.session_state.lambda_max
    ci         = st.session_state.ci
    n          = len(crits)
    consistent = cr <= 0.10

    page_header(3, "Weights & Method",
                "Review AHP results, check consistency, and choose ranking method")
    wrap_open()

    # Consistency metrics
    st.markdown("### AHP Consistency Analysis")
    col1, col2, col3 = st.columns(3)
    col1.metric("λ_max  (eigenvalue)",       f"{lmax:.4f}")
    col2.metric("Consistency Index  (CI)",   f"{ci:.4f}")
    col3.metric("Consistency Ratio  (CR)",   f"{cr:.4f}")

    cr_color  = COLOR_PRIMARY if consistent else "#ff6b4a"
    cr_status = "✓ Consistent" if consistent else "⚠ Inconsistent — consider revising"
    st.markdown(f"""
    <div style="background:{'#0c1a0c' if consistent else '#1a0e0c'};
                border:1px solid {'#2a4a2a' if consistent else '#4a2a1e'};
                border-radius:3px;padding:12px 18px;margin:8px 0 20px 0;">
      <span style="font-family:'{FONT_MONO}',monospace;font-size:{FS_BASE};color:{cr_color};">{cr_status}</span>
      {"<span style='font-family:{FONT_MONO},monospace;font-size:{FS_SM};color:#aaa;margin-left:16px;'>CR must be ≤ 0.10 for coherent judgments.</span>" if not consistent else ""}
    </div>""", unsafe_allow_html=True)

    with st.expander("ℹ️ What does the eigenvalue tell us?"):
        st.markdown(f"""
**λ_max (Principal Eigenvalue) = {lmax:.4f}**

In AHP, the matrix is perfectly consistent when λ_max = n (here n = {n}).

| Metric | Value | Meaning |
|--------|-------|---------|
| λ_max | {lmax:.4f} | Should be close to {n} |
| λ_max − n | {lmax-n:.4f} | Deviation from perfect consistency |
| CI = (λ_max − n)/(n−1) | {ci:.4f} | Normalised inconsistency |
| CR = CI / RI | {cr:.4f} | {'✓ Acceptable (< 0.10)' if consistent else '⚠ Too high — revise comparisons'} |

{'Judgments are **consistent**. Proceed with confidence.' if consistent else '**Recommendation:** go back and revise the least certain comparisons.'}
        """)

    # Criteria weights — table + bar chart
    st.markdown("### Criteria Weights")
    wdf = pd.DataFrame({
        "Criterion": [CRITERIA_META[c]["short"] for c in crits],
        "Full Name":  crits,
        "Type":       [CRITERIA_META[c]["type"].upper() for c in crits],
        "Weight":     [round(float(w), 4) for w in weights],
        "Weight %":   [f"{float(w)*100:.1f}%" for w in weights],
    })
    st.dataframe(wdf, width='stretch', hide_index=True)

    wdf2 = pd.DataFrame(
        {"Weight": [float(w) for w in weights]},
        index=[CRITERIA_META[c]["short"] for c in crits]
    )
    st.bar_chart(wdf2.sort_values("Weight", ascending=False))

    # Method selection
    st.markdown("### Ranking Method")
    method = st.radio(
        "Choose method", ["TOPSIS", "WPM"], horizontal=True,
        index=0 if st.session_state.method == "TOPSIS" else 1,
        key="method_radio"
    )
    st.session_state.method = method

    if method == "TOPSIS":
        st.info("**TOPSIS** — Ranks by distance to the ideal and anti-ideal solutions. Best for continuous numerical data.")
    else:
        st.info("**WPM** (Weighted Product Model) — Multiplies normalised values raised to weight powers. Good for ratio-scale data.")

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([9, 1])
    with c1:
        if st.button("← Back", key="s3back"):
            st.session_state.step = 2; st.rerun()
    with c2:
        if st.button("Run Analysis →", key="s3btn"):
            st.session_state.step = 4; st.rerun()
    wrap_close()

# ── STEP 4 — Results ───────────────────────────────────────────────────────────
def step4():
    crits   = st.session_state.sel_criteria
    weights = st.session_state.weights
    method  = st.session_state.method

    page_header(4, "Results",
                f"{method} ranking · {len(ALL_MATERIALS)} materials · {len(crits)} criteria")
    wrap_open()

    # Compute scores
    values    = MAT_DF[crits].copy().values.astype(float)
    mats      = list(MAT_DF.index)
    col_means = np.nanmean(values, axis=0)
    for j in range(values.shape[1]):
        values[np.isnan(values[:, j]), j] = col_means[j]

    scores  = topsis(values, weights, crits) if method == "TOPSIS" else wpm(values, weights, crits)
    ranking = np.argsort(scores)[::-1]

    # Top 5 podium
    st.markdown("### Top 5 Materials")
    medals = ["🥇", "🥈", "🥉", "4th", "5th"]
    top5   = ranking[:5]
    cols   = st.columns(5)
    for pos, idx in enumerate(top5):
        with cols[pos]:
            pct = scores[idx] / scores[ranking[0]] * 100 if scores[ranking[0]] > 0 else 0
            st.markdown(f"""
            <div style="background:{COLOR_SURFACE}33;border:1px solid {COLOR_PRIMARY if pos==0 else COLOR_BORDER+'44'};
                        border-radius:4px;padding:16px 12px;text-align:center;">
              <div style="font-size:{FS_2XL if pos==0 else FS_XL};margin-bottom:8px;">{medals[pos]}</div>
              <div style="font-family:'{FONT_TITLE}',sans-serif;font-weight:700;font-size:{FS_BASE};
                          color:{COLOR_PRIMARY if pos==0 else COLOR_TEXT};word-break:break-word;
                          line-height:1.3;margin-bottom:8px;">{mats[idx]}</div>
              <div style="font-family:'{FONT_MONO}',monospace;font-size:{FS_MD};font-weight:700;
                          color:{COLOR_PRIMARY};">{scores[idx]:.4f}</div>
              <div style="background:{COLOR_BG};border-radius:2px;height:3px;margin-top:8px;">
                <div style="background:{COLOR_PRIMARY};height:3px;width:{pct:.0f}%;border-radius:2px;"></div>
              </div>
            </div>""", unsafe_allow_html=True)

    # Full ranking — all materials
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Full Ranking — All Materials")
    result_df = pd.DataFrame({
        "Rank":            list(range(1, len(mats) + 1)),
        "Material":        [mats[i] for i in ranking],
        f"{method} Score": [round(float(scores[i]), 4) for i in ranking],
    })
    st.dataframe(result_df, width='stretch', hide_index=True, height=600)

    # Download
    csv_out = result_df.to_csv(index=False).encode()
    st.download_button(
        "⬇ Download Ranking as CSV",
        data=csv_out,
        file_name=f"ranking_{method.lower()}.csv",
        mime="text/csv"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,2,1])
    with c1:
        if st.button("← Change Method / Weights", key="s4back"):
            st.session_state.step = 3; st.rerun()
    with c2:
        if st.button("↺ Start Over", key="s4restart"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
    with c3:
        if st.button("Sensitivity Analysis →", key="s4sens"):
            st.session_state.step = 5; st.rerun()
    wrap_close()

# ── STEP 5 — Sensitivity Analysis ─────────────────────────────────────────────
def run_simulation(method_name, weights_list, values, crits):
    """Run TOPSIS or WPM for each weight vector, return win counts."""
    n_mats = values.shape[0]
    win_counts = np.zeros(n_mats, dtype=int)
    for w in weights_list:
        if method_name == "TOPSIS":
            scores = topsis(values, w, crits)
        else:
            scores = wpm(values, w, crits)
        winner = np.argmax(scores)
        win_counts[winner] += 1
    return win_counts

def sample_weights_uniform(n_criteria, n_sim):
    """Dirichlet(1,1,...) = uniform over simplex."""
    return np.random.dirichlet(np.ones(n_criteria), size=n_sim)

def sample_weights_interval(base_weights, interval_pct, n_sim):
    """Sample within ±interval_pct% of each base weight, then normalise."""
    n = len(base_weights)
    delta = base_weights * (interval_pct / 100.0)
    samples = []
    for _ in range(n_sim):
        w = base_weights + np.random.uniform(-delta, delta)
        w = np.clip(w, 1e-6, None)
        w /= w.sum()
        samples.append(w)
    return np.array(samples)

def sample_weights_dirichlet(base_weights, concentration, n_sim):
    """Dirichlet(α) centred on base_weights with given concentration."""
    alpha = base_weights * concentration
    alpha = np.clip(alpha, 1e-6, None)
    return np.random.dirichlet(alpha, size=n_sim)

def render_sensitivity_result(label, win_counts, mats, n_sim, color):
    """Render a single sensitivity result block."""
    top_idx  = np.argsort(win_counts)[::-1][:10]   # top 10
    top_names = [mats[i] for i in top_idx]
    top_pcts  = [win_counts[i] / n_sim * 100 for i in top_idx]

    st.markdown(f"""
    <div style="background:{color}18; border:1px solid {color}44;
                border-radius:6px; padding:16px 20px; margin-bottom:8px;">
      <div style="font-family:'{FONT_MONO}',monospace;font-size:{FS_SM};
                  color:{color};text-transform:uppercase;letter-spacing:.1em;
                  margin-bottom:14px;">{label}</div>""",
        unsafe_allow_html=True)

    for name, pct in zip(top_names, top_pcts):
        bar = int(pct)
        st.markdown(f"""
      <div style="margin-bottom:10px;">
        <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
          <span style="font-family:'{FONT_TITLE}',sans-serif;font-size:{FS_BASE};
                       color:{COLOR_TEXT};font-weight:600;">{name}</span>
          <span style="font-family:'{FONT_MONO}',monospace;font-size:{FS_SM};
                       color:{color};font-weight:700;">{pct:.1f}%</span>
        </div>
        <div style="background:{COLOR_BG};border-radius:2px;height:5px;">
          <div style="background:{color};height:5px;width:{bar}%;
                      border-radius:2px;transition:width .3s;"></div>
        </div>
      </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def step5():
    crits   = st.session_state.sel_criteria
    weights = st.session_state.weights
    method  = st.session_state.method
    mats    = list(MAT_DF.index)

    # Update header step label to 5
    st.markdown(f"""
    <div style="padding:40px 0 0 0;">
      <div style="border-left:3px solid {COULEURS_UI};padding-left:20px;margin-bottom:28px;">
        <div style="font-family:'{FONT_MONO}',monospace;font-size:{FS_XS};color:{COULEURS_UI};
                    text-transform:uppercase;letter-spacing:.18em;margin-bottom:6px;">STEP 5 / 5</div>
        <h1 style="font-size:{FS_TITLE};font-weight:800;color:{COLOR_TEXT};
                   line-height:1.05;margin:0 0 6px 0;">Sensitivity Analysis</h1>
        <p style="font-family:'{FONT_MONO}',monospace;font-size:{FS_XS};color:{COLOR_TEXT}88;margin:0;">
          Monte Carlo — how robust is your ranking to weight uncertainty?
        </p>
      </div>
    </div>""", unsafe_allow_html=True)

    # ── Controls ──
    st.markdown("### Configuration")
    c1, c2 = st.columns(2)
    with c1:
        approaches = st.multiselect(
            "Select approaches to run",
            options=["Uniform", "Interval", "Dirichlet"],
            default=["Uniform"],
            key="sa_approaches"
        )
    with c2:
        n_sim = st.number_input(
            "Number of simulations",
            min_value=100, max_value=50000,
            value=1000, step=500,
            key="sa_nsim"
        )
        n_sim = int(n_sim)

    # Approach-specific params
    interval_pct  = 20
    concentration = 20

    if 'Uniform' in approaches:
        st.markdown(
            f'<div style="background:{COLOR_SURFACE}18;border:1px solid {COLOR_BORDER}44;border-radius:4px;'
            f'padding:10px 16px;margin-bottom:12px;"><span style="font-family:{FONT_MONO},monospace;'
            f'font-size:{FS_XS};color:{COLOR_TEXT}88;"><b>Uniform:</b> no parameters needed — samples any '
            f'valid weight combination across the full simplex.</span></div>',
            unsafe_allow_html=True)

    if 'Interval' in approaches:
        st.markdown('**Interval — width around each AHP weight**')
        interval_pct = st.radio(
            'Interval width',
            options=[5, 10, 15, 20, 25, 30, 40, 50],
            format_func=lambda v: f'±{v}%',
            index=3, horizontal=True,
            key='sa_interval', label_visibility='collapsed'
        )
        st.caption(f'Varies each weight ±{interval_pct}% around your AHP values.')

    if 'Dirichlet' in approaches:
        st.markdown('**Dirichlet — concentration around AHP weights**')
        concentration = st.radio(
            'Dirichlet concentration',
            options=[5, 10, 20, 30, 50, 75, 100],
            format_func=lambda v: f'{v}  ({"explore" if v<=10 else "moderate" if v<=30 else "tight"})',
            index=2, horizontal=True,
            key='sa_conc', label_visibility='collapsed'
        )
        st.caption(f'Concentration={concentration}. Higher = samples stay closer to your AHP weights.')

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("▶ Run Simulation", key="sa_run"):
        if not approaches:
            st.error("Select at least one approach.")
            return

        # Prepare material values matrix
        values    = MAT_DF[crits].copy().values.astype(float)
        col_means = np.nanmean(values, axis=0)
        for j in range(values.shape[1]):
            values[np.isnan(values[:, j]), j] = col_means[j]

        n_crit = len(crits)
        results = {}

        with st.spinner("Running simulations..."):
            if "Uniform" in approaches:
                w_samples = sample_weights_uniform(n_crit, n_sim)
                results["Uniform"] = run_simulation(method, w_samples, values, crits)

            if "Interval" in approaches:
                w_samples = sample_weights_interval(weights, interval_pct, n_sim)
                results["Interval"] = run_simulation(method, w_samples, values, crits)

            if "Dirichlet" in approaches:
                w_samples = sample_weights_dirichlet(weights, concentration, n_sim)
                results["Dirichlet"] = run_simulation(method, w_samples, values, crits)

        st.markdown("### Results")
        st.markdown(f"""
        <div style="font-family:'{FONT_MONO}',monospace;font-size:{FS_SM};
                    color:{COLOR_TEXT}88;margin-bottom:20px;">
          {n_sim} simulations · {method} · {n_crit} criteria · top 10 winners shown
        </div>""", unsafe_allow_html=True)

        colors = {"Uniform": "#6ec6f5", "Interval": "#f5a623", "Dirichlet": "#b8f03a"}

        if len(results) == 1:
            # Single approach — full width
            name, wins = list(results.items())[0]
            render_sensitivity_result(name, wins, mats, n_sim, colors[name])
        else:
            # Side by side comparison
            cols = st.columns(len(results))
            for col, (name, wins) in zip(cols, results.items()):
                with col:
                    render_sensitivity_result(name, wins, mats, n_sim, colors[name])

        # Robustness verdict
        st.markdown("### Robustness Verdict")
        for name, wins in results.items():
            top_pct = wins.max() / n_sim * 100
            top_mat = mats[np.argmax(wins)]
            if top_pct >= 60:
                verdict = f"✓ **Robust** — {top_mat} wins {top_pct:.1f}% of the time. Decision is stable."
                st.success(f"**{name}:** {verdict}")
            elif top_pct >= 35:
                verdict = f"~ **Moderate** — {top_mat} wins {top_pct:.1f}% of the time. Decision is somewhat sensitive to weights."
                st.warning(f"**{name}:** {verdict}")
            else:
                verdict = f"⚠ **Fragile** — {top_mat} wins only {top_pct:.1f}% of the time. No clear winner — review your priorities."
                st.error(f"**{name}:** {verdict}")

        # Download full win table
        st.markdown("<br>", unsafe_allow_html=True)
        for name, wins in results.items():
            df_out = pd.DataFrame({
                "Material": mats,
                "Win Count": wins,
                "Win %": [round(w / n_sim * 100, 2) for w in wins],
            }).sort_values("Win Count", ascending=False).reset_index(drop=True)
            df_out.insert(0, "Rank", range(1, len(mats)+1))
            csv = df_out.to_csv(index=False).encode()
            st.download_button(
                f"⬇ Download {name} results",
                data=csv,
                file_name=f"sensitivity_{name.lower()}_{method.lower()}.csv",
                mime="text/csv",
                key=f"dl_{name}"
            )

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([8, 1])
    with c1:
        if st.button("← Back to Results", key="s5back"):
            st.session_state.step = 4; st.rerun()
    with c2:
        if st.button("↺ Start Over", key="s5restart"):
            for k in list(st.session_state.keys()): del st.session_state[k]
            st.rerun()

# ── Router ─────────────────────────────────────────────────────────────────────
progress_bar(st.session_state.step)
s = st.session_state.step
if   s == 1: step1()
elif s == 2: step2()
elif s == 3: step3()
elif s == 4: step4()
elif s == 5: step5()