import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from main import run_pipeline

st.set_page_config(
    page_title="AutoResearch Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════
#  GLOBAL CSS — Deep Space + Neon Theme
# ══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap');

:root {
    --bg-deep:     #020818;
    --bg-card:     #0a1628;
    --bg-glass:    rgba(10, 22, 40, 0.85);
    --neon-cyan:   #00f5ff;
    --neon-purple: #bf5fff;
    --neon-pink:   #ff2d8d;
    --neon-green:  #00ff9d;
    --neon-gold:   #ffd700;
    --text-main:   #e8f4fd;
    --text-white:  white;
    --border:      rgba(0,245,255,0.2);
}

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Exo 2', sans-serif;
    background-color: var(--bg-deep) !important;
    color: var(--text-main) !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 20% 20%, rgba(0,245,255,0.06) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 80%, rgba(191,95,255,0.06) 0%, transparent 60%),
        radial-gradient(ellipse at 50% 50%, rgba(255,45,141,0.03) 0%, transparent 70%),
        #020818;
}

/* ── Hero Header ── */
.hero-header {
    text-align: center;
    padding: 60px 20px 40px;
    position: relative;
}

.hero-title {
    font-family: 'Orbitron', monospace;
    font-weight: 900;
    font-size: clamp(2.2rem, 5vw, 4rem);
    background: linear-gradient(135deg, #00f5ff 0%, #bf5fff 50%, #ff2d8d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 3px;
    margin-bottom: 8px;
    text-shadow: none;
    animation: titlePulse 3s ease-in-out infinite;
}

@keyframes titlePulse {
    0%, 100% { filter: brightness(1); }
    50% { filter: brightness(1.2); }
}

.hero-subtitle {
    font-family: 'Exo 2', sans-serif;
    font-size: 1.1rem;
    color: var(--text-dim);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.hero-badge {
    display: inline-block;
    background: linear-gradient(135deg, rgba(0,245,255,0.1), rgba(191,95,255,0.1));
    border: 1px solid var(--neon-cyan);
    border-radius: 30px;
    padding: 8px 24px;
    font-size: 0.85rem;
    color: var(--neon-cyan);
    letter-spacing: 2px;
    margin: 4px;
}

/* ── Divider ── */
.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--neon-cyan), var(--neon-purple), var(--neon-pink), transparent);
    margin: 30px 0;
    opacity: 0.6;
}

/* ── Cards ── */
.glass-card {
    background: var(--bg-glass);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 24px;
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, box-shadow 0.3s;
}

.glass-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--neon-cyan), var(--neon-purple), var(--neon-pink));
}

.glass-card:hover {
    border-color: rgba(0,245,255,0.4);
    box-shadow: 0 0 30px rgba(0,245,255,0.08);
}

.card-cyan::before   { background: linear-gradient(90deg, #00f5ff, #0080ff); }
.card-purple::before { background: linear-gradient(90deg, #bf5fff, #ff2d8d); }
.card-green::before  { background: linear-gradient(90deg, #00ff9d, #00f5ff); }
.card-gold::before   { background: linear-gradient(90deg, #ffd700, #ff8c00); }

/* ── Section Titles ── */
.section-title {
    font-family: 'Orbitron', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.title-cyan   { color: var(--neon-cyan); }
.title-purple { color: var(--neon-purple); }
.title-green  { color: var(--neon-green); }
.title-gold   { color: var(--neon-gold); }
.title-pink   { color: var(--neon-pink); }

/* ── Input Box ── */
.stTextInput > div > div > input {
    background: #0a1628 !important;      /* Darker background for the input */
    border: 1px solid #00f5ff !important; /* Neon cyan border */
    border-radius: 12px !important;
    color: #ffffff !important;           /* White text for readability */
    font-family: 'Exo 2', sans-serif !important;
    font-size: 1rem !important;
    padding: 14px 20px !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00f5ff !important;    /* Keep focus border bright */
    box-shadow: 0 0 20px rgba(0,245,255,0.3) !important;
}

.stTextInput > div > div > input::placeholder {
    color: #7a9bbf !important;           /* Slightly dim placeholder text */
}

/* ── Button ── */
.stButton > button {
    width: 100% !important;
    padding: 16px 32px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    color: #020818 !important;           /* Text inside button */
    background: linear-gradient(135deg, #00f5ff, #bf5fff) !important;
    border: none !important;
    border-radius: 12px !important;
    cursor: pointer !important;
    transition: all 0.3s !important;
    text-transform: uppercase !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #bf5fff, #ff2d8d) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(0,245,255,0.3) !important;
}
            
            
/* ── Paper Cards ── */
.paper-card {
    background: rgba(0,245,255,0.03);
    border: 1px solid rgba(0,245,255,0.12);
    border-left: 3px solid var(--neon-cyan);
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
    transition: all 0.3s;
}

.paper-card:hover {
    background: rgba(0,245,255,0.06);
    border-left-color: var(--neon-purple);
    transform: translateX(4px);
}

.paper-title {
    font-family: 'Exo 2', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    color: var(--neon-cyan);
    margin-bottom: 8px;
}

.paper-abstract {
    color: var(--text-dim);
    font-size: 0.88rem;
    line-height: 1.6;
    margin-bottom: 10px;
}

.paper-link {
    color: var(--neon-purple);
    font-size: 0.82rem;
    text-decoration: none;
    letter-spacing: 1px;
}

.paper-source {
    display: inline-block;
    font-size: 0.72rem;
    padding: 3px 10px;
    border-radius: 20px;
    margin-right: 8px;
    font-weight: 600;
    letter-spacing: 1px;
}

.source-arxiv    { background: rgba(0,245,255,0.15); color: var(--neon-cyan); }
.source-semantic { background: rgba(191,95,255,0.15); color: var(--neon-purple); }

/* ── Stats Row ── */
.stat-box {
    background: rgba(0,245,255,0.05);
    border: 1px solid rgba(0,245,255,0.2);
    border-radius: 16px;
    padding: 24px;
    text-align: center;
}

.stat-number {
    font-family: 'Orbitron', monospace;
    font-size: 2.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    color: var(--text-dim);
    font-size: 0.8rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 6px;
}




/* ── Download Button ── */
.stDownloadButton > button {
    background: linear-gradient(135deg, rgba(0,255,157,0.15), rgba(0,245,255,0.15)) !important;
    border: 1px solid var(--neon-green) !important;
    color: var(--neon-green) !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.8rem !important;
    letter-spacing: 2px !important;
    border-radius: 10px !important;
    padding: 12px 24px !important;
    width: 100% !important;
    transition: all 0.3s !important;
}

.stDownloadButton > button:hover {
    background: linear-gradient(135deg, rgba(0,255,157,0.3), rgba(0,245,255,0.3)) !important;
    box-shadow: 0 0 20px rgba(0,255,157,0.2) !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-color: var(--neon-cyan) transparent transparent transparent !important;
}

/* ── Success/Error ── */
.stSuccess {
    background: rgba(0,255,157,0.1) !important;
    border: 1px solid var(--neon-green) !important;
    border-radius: 10px !important;
    color: var(--neon-green) !important;
}

.stAlert {
    border-radius: 10px !important;
}

/* ── Pipeline Steps ── */
.pipeline-step {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 20px;
    background: rgba(0,245,255,0.04);
    border: 1px solid rgba(0,245,255,0.1);
    border-radius: 12px;
    margin-bottom: 10px;
}

.step-icon {
    font-size: 1.5rem;
    width: 40px;
    text-align: center;
}

.step-text {
    font-family: 'Exo 2', sans-serif;
    font-size: 0.9rem;
    color: #ffffff !important;   /* Bright white text */
    letter-spacing: 1px;
}
.step-active { border-color: rgba(0,245,255,0.4); color: var(--neon-cyan); }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 40px 20px;
    color: var(--text-dim);
    font-size: 0.8rem;
    letter-spacing: 2px;
}

.footer span {
    color: var(--neon-pink);
}

/* Hide streamlit defaults */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; max-width: 1200px; }
/* ── FORCE ALL GENERATED TEXT TO WHITE ── */
.review-content,
.gap-content,
.paper-abstract,
.stat-label,
p, span, li, div {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  CHART HELPERS
# ══════════════════════════════════════════════
def make_bar_chart(gap_text):
    keywords = {
        "Data": gap_text.lower().count("data"),
        "Models": gap_text.lower().count("model"),
        "Efficiency": gap_text.lower().count("effici"),
        "Scalability": gap_text.lower().count("scal"),
        "Language": gap_text.lower().count("language"),
        "Bias": gap_text.lower().count("bias"),
    }
    keywords = {k: max(v, 1) for k, v in keywords.items()}

    colors = ['#00f5ff','#bf5fff','#ff2d8d','#ffd700','#00ff9d','#ff8c00']
    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor('#0a1628')
    ax.set_facecolor('#0a1628')

    bars = ax.bar(keywords.keys(), keywords.values(), color=colors, width=0.6, zorder=3)

    for bar, color in zip(bars, colors):
        ax.bar(bar.get_x() + bar.get_width()/2, bar.get_height(),
               width=bar.get_width(), color=color, alpha=0.15, zorder=2)

    ax.set_title("Research Gap Frequency Analysis", color='#00f5ff',
                 fontsize=12, fontweight='bold', pad=15)
    ax.set_ylabel("Frequency", color='#7a9bbf', fontsize=10)
    ax.tick_params(colors='#7a9bbf', labelsize=9)
    ax.spines[['top','right','left','bottom']].set_color('#1a2a3a')
    ax.yaxis.grid(True, color='#1a2a3a', linewidth=0.8, zorder=1)
    ax.set_axisbelow(True)
    plt.xticks(rotation=20)
    plt.tight_layout()
    return fig


def make_pie_chart(gap_text):
    keywords = {
        "Data": gap_text.lower().count("data"),
        "Models": gap_text.lower().count("model"),
        "Efficiency": gap_text.lower().count("effici"),
        "Time": gap_text.lower().count("time"),
        "Language": gap_text.lower().count("language"),
    }
    keywords = {k: max(v, 1) for k, v in keywords.items()}

    colors = ['#00f5ff','#bf5fff','#ff2d8d','#ffd700','#00ff9d']
    fig, ax = plt.subplots(figsize=(6, 5))
    fig.patch.set_facecolor('#0a1628')
    ax.set_facecolor('#0a1628')

    wedges, texts, autotexts = ax.pie(
        keywords.values(),
        labels=keywords.keys(),
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        pctdistance=0.75,
        wedgeprops=dict(width=0.6, edgecolor='#020818', linewidth=2)
    )

    for text in texts:
        text.set_color('#7a9bbf')
        text.set_fontsize(9)
    for autotext in autotexts:
        autotext.set_color('#020818')
        autotext.set_fontsize(8)
        autotext.set_fontweight('bold')

    ax.set_title("Gap Distribution", color='#bf5fff',
                 fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    return fig


# ══════════════════════════════════════════════
#  HERO HEADER
# ══════════════════════════════════════════════
st.markdown("""
<div class="hero-header">
    <div class="hero-title">⚡ AUTORESEARCH AGENT</div>
    <div class="hero-subtitle">Autonomous Literature Intelligence System</div>
    <div>
        <span class="hero-badge">🤖 GROQ AI</span>
        <span class="hero-badge">📡 ARXIV</span>
        <span class="hero-badge">🔬 SEMANTIC SCHOLAR</span>
        <span class="hero-badge">🧠 LLAMA 3</span>
    </div>
</div>
<div class="neon-divider"></div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  PIPELINE OVERVIEW
# ══════════════════════════════════════════════
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    <div class="glass-card card-cyan">
        <div class="section-title title-cyan">🔍 Research Intelligence Pipeline</div>
        <div class="pipeline-step">
            <div class="step-icon">🔍</div>
            <div>
                <div style="color:#00f5ff; font-weight:600; font-size:0.9rem;">AGENT 1 — Search Agent</div>
                <div class="step-text">Scans ArXiv + Semantic Scholar simultaneously</div>
            </div>
        </div>
        <div class="pipeline-step">
            <div class="step-icon">📄</div>
            <div>
                <div style="color:#bf5fff; font-weight:600; font-size:0.9rem;">AGENT 2 — Extraction Agent</div>
                <div class="step-text">Extracts key findings using LLaMA 3 AI</div>
            </div>
        </div>
        <div class="pipeline-step">
            <div class="step-icon">🧠</div>
            <div>
                <div style="color:#ff2d8d; font-weight:600; font-size:0.9rem;">AGENT 3 — Gap Analysis Agent</div>
                <div class="step-text">Identifies research gaps & contradictions</div>
            </div>
        </div>
        <div class="pipeline-step">
            <div class="step-icon">📝</div>
            <div>
                <div style="color:#ffd700; font-weight:600; font-size:0.9rem;">AGENT 4 — Review Generator</div>
                <div class="step-text">Generates complete literature review</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card card-purple">
        <div class="section-title title-purple">⚡ Capabilities</div>
        <div style="color:#7a9bbf; font-size:0.88rem; line-height:2.2;">
            ✦ &nbsp; Multi-source paper discovery<br>
            ✦ &nbsp; AI-powered key finding extraction<br>
            ✦ &nbsp; Intelligent duplicate removal<br>
            ✦ &nbsp; Deep research gap analysis<br>
            ✦ &nbsp; Professional literature review<br>
            ✦ &nbsp; Visual gap analytics & charts<br>
            ✦ &nbsp; One-click report download<br>
            ✦ &nbsp; Covers any research domain
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  SEARCH INPUT
# ══════════════════════════════════════════════
st.markdown("""
<div class="glass-card">
    <div class="section-title title-cyan">🚀 Launch Research Pipeline</div>
""", unsafe_allow_html=True)

topic = st.text_input(
    "",
    placeholder="e.g. Agentic AI Systems, Large Language Models, RAG pipelines...",
    label_visibility="collapsed"
)

run_btn = st.button("⚡  INITIATE RESEARCH PIPELINE")

st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  RUN PIPELINE
# ══════════════════════════════════════════════
if run_btn:
    if not topic.strip():
        st.error("❌ Please enter a research topic to proceed!!")
    else:
        with st.spinner("🤖 AI Agents running... Please wait 1-2 minutes ⏳"):
            result = run_pipeline(topic)

        if not result:
            st.error("❌ Pipeline failed!! Please try again.")
        else:
            st.success("✅ Research Pipeline Completed Successfully!!")
            st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

            # ── STATS ──
            st.markdown("""
            <div class="section-title title-green" style="justify-content:center; font-size:1rem;">
                📊 PIPELINE RESULTS
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(result['papers'])}</div>
                    <div class="stat-label">Papers Found</div>
                </div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(result['extracted'])}</div>
                    <div class="stat-label">Papers Analyzed</div>
                </div>""", unsafe_allow_html=True)
            with c3:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">4</div>
                    <div class="stat-label">AI Agents Used</div>
                </div>""", unsafe_allow_html=True)
            with c4:
                word_count = len(result['review'].split())
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{word_count}</div>
                    <div class="stat-label">Words Generated</div>
                </div>""", unsafe_allow_html=True)

            st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

            # ── LITERATURE REVIEW ──
            st.markdown("""
            <div class="glass-card card-cyan">
                <div class="section-title title-cyan">📄 LITERATURE REVIEW</div>
            """, unsafe_allow_html=True)
            st.markdown(f'<div class="review-content">', unsafe_allow_html=True)
            st.markdown(result["review"])
            st.markdown('</div></div>', unsafe_allow_html=True)

            # ── GAP ANALYSIS ──
            st.markdown("""
            <div class="glass-card card-purple">
                <div class="section-title title-purple">🧠 GAP ANALYSIS</div>
            """, unsafe_allow_html=True)
            st.markdown(result["gap_analysis"])
            st.markdown('</div>', unsafe_allow_html=True)

            # ── CHARTS ──
            st.markdown("""
            <div class="glass-card card-gold">
                <div class="section-title title-gold">📈 VISUAL ANALYTICS</div>
            """, unsafe_allow_html=True)

            chart1, chart2 = st.columns(2)
            with chart1:
                fig1 = make_bar_chart(result["gap_analysis"])
                st.pyplot(fig1)
                plt.close()
            with chart2:
                fig2 = make_pie_chart(result["gap_analysis"])
                st.pyplot(fig2)
                plt.close()

            st.markdown('</div>', unsafe_allow_html=True)

            # ── PAPERS ──
            st.markdown("""
            <div class="glass-card card-green">
                <div class="section-title title-green">📚 DISCOVERED PAPERS</div>
            """, unsafe_allow_html=True)

            for i, paper in enumerate(result["papers"]):
                source = paper.get("source", "arxiv")
                source_class = "source-arxiv" if source == "arxiv" else "source-semantic"
                source_label = "ArXiv" if source == "arxiv" else "Semantic Scholar"
                abstract = paper.get("abstract", "")[:220] + "..."
                url = paper.get("url", "#")

                st.markdown(f"""
                            <div class="paper-card">
                    <div class="paper-title">{i+1}. {paper.get("title", "No Title")}</div>
                    <div class="paper-abstract">{abstract}</div>
                    <div>
                        <span class="paper-source {source_class}">{source_label}</span>
                        <a class="paper-link" href="{url}" target="_blank">Read Full Paper 🔗</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)  # Close papers card container

            # ── DOWNLOAD REVIEW BUTTON ──
            st.markdown("""
            <div class="glass-card card-cyan">
                <div class="section-title title-cyan">💾 DOWNLOAD REPORT</div>
            """, unsafe_allow_html=True)

            from io import BytesIO
            import base64

            # Combine review + gap analysis + paper list into one text file
            report_text = f"=== LITERATURE REVIEW ===\n{result['review']}\n\n"
            report_text += f"=== GAP ANALYSIS ===\n{result['gap_analysis']}\n\n"
            report_text += "=== DISCOVERED PAPERS ===\n"
            for paper in result["papers"]:
                report_text += f"- {paper.get('title','No Title')} ({paper.get('source','arxiv').capitalize()})\n"
                report_text += f"  Abstract: {paper.get('abstract','')}\n"
                report_text += f"  URL: {paper.get('url','#')}\n\n"

            report_bytes = BytesIO(report_text.encode('utf-8'))

            st.download_button(
                label="⬇️ Download Full Research Report",
                data=report_bytes,
                file_name=f"Research_Report_{topic.replace(' ','_')}.txt",
                mime="text/plain",
                key="download-report"
            )

            st.markdown('</div>', unsafe_allow_html=True)  # Close download card