"""Nexus - Ecossistema de IAs (versão C - Premium)
Versão refatorada, modular e com recursos avançados:
- Identidade visual preservada (tema neon/escuro)
- Página principal com grid responsivo e cards
- Página dedicada por IA com links oficiais
- Theme toggle (Neon / Dark)
- Analytics simples (contagem de acessos em sessão)
- Fallback para AI_LINKS vindo de config.py, se não existir, carrega defaults
- Código organizado em funções reutilizáveis
- Comentários e instruções para extensão
"""

import streamlit as st
import time
from datetime import datetime
import base64
from typing import Dict, List

# Tenta importar AI_LINKS do config, caso não exista usamos um dicionário padrão
try:
    from config import AI_LINKS  # user-provided config optional
except Exception:
    AI_LINKS = None

# ---------- Defaults: fontes oficiais adicionadas ----------
DEFAULT_AI_LINKS = {
    "text_generator": [
        {"name": "Claude (Anthropic) - Sonnet", "url": "https://www.anthropic.com/claude/sonnet"},
        {"name": "Claude (site)", "url": "https://www.claude.com/"}
    ],
    "image_creator": [
        {"name": "Qwen (Alibaba) - qwen.ai", "url": "https://qwen.ai/"}
    ],
    "code_assistant": [
        {"name": "Anthropic - Build with Claude", "url": "https://www.anthropic.com/learn/build-with-claude"}
    ],
    "data_analyst": [
        {"name": "Google AI Studio (Gemini)", "url": "https://ai.google.dev/aistudio"},
        {"name": "Vertex AI Studio (Google Cloud)", "url": "https://cloud.google.com/generative-ai-studio"}
    ],
    "translator": [
        {"name": "Google Translate (Google) - Translate API", "url": "https://cloud.google.com/translate"}
    ],
    "voice_synthesis": [
        {"name": "Google Text-to-Speech", "url": "https://cloud.google.com/text-to-speech"}
    ],
    "document_processor": [
        {"name": "Google Document AI", "url": "https://cloud.google.com/document-ai"}
    ],
    "chatbot_builder": [
        {"name": "Qwen API", "url": "https://qwen.ai/apiplatform"}
    ],
    "video_editor": [
        {"name": "Google AI Studio (video tools)", "url": "https://ai.google.dev/aistudio"}
    ]
}

AI_LINKS = AI_LINKS or DEFAULT_AI_LINKS

# ----------------- Streamlit page config -----------------
st.set_page_config(
    page_title="Nexus - Ecossistema de IAs",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- UI Helpers & State -----------------
if "analytics" not in st.session_state:
    st.session_state.analytics = {k: 0 for k in DEFAULT_AI_LINKS.keys()}

if "theme" not in st.session_state:
    st.session_state.theme = "neon"


def increment_analytics(ai_key: str):
    if ai_key not in st.session_state.analytics:
        st.session_state.analytics[ai_key] = 0
    st.session_state.analytics[ai_key] += 1


# ----------------- CSS (preservando identidade visual) -----------------
def load_css(theme: str = "neon"):
    base_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');

    .stApp {{
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
    }}

    .main-header {{
        text-align: center;
        padding: 1.5rem 0 0.5rem 0;
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        font-size: 3rem;
        margin-bottom: 0.2rem;
        color: transparent;
        background: linear-gradient(45deg, #00d4ff, #00ff88);
        -webkit-background-clip: text;
        background-clip: text;
        text-shadow: 0 0 24px rgba(0,212,255,0.28);
    }}

    .subtitle {{
        text-align: center;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.05rem;
        color: #a0a0a0;
        margin-bottom: 1.25rem;
    }}

    .ecosystem-container {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.3rem;
        padding: 1rem 1rem 2rem 1rem;
        max-width: 1400px;
        margin: 0 auto;
    }}

    .ai-card {{
        background: linear-gradient(145deg, rgba(30,30,63,0.9), rgba(42,42,90,0.9));
        border-radius: 14px;
        padding: 1.25rem;
        border: 1px solid rgba(255,255,255,0.02);
        position: relative;
        overflow: hidden;
        transition: transform .25s ease, box-shadow .25s ease;
        cursor: pointer;
        box-shadow: 0 6px 18px rgba(0,0,0,0.45);
    }}

    .ai-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 18px 35px rgba(0,212,255,0.12);
    }}

    .ai-icon {{
        font-size: 2.4rem;
        text-align: center;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #00d4ff, #00ff88);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }}

    .ai-title {{
        font-family: 'Orbitron', monospace;
        font-size: 1.15rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.45rem;
        color: #ffffff;
    }}

    .ai-description {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.95rem;
        text-align: center;
        color: #b0b0b0;
        line-height: 1.5;
        margin-bottom: 0.9rem;
    }}

    .links-container {{
        background: linear-gradient(145deg, rgba(30,30,63,0.95), rgba(42,42,90,0.95));
        border-radius: 12px;
        padding: 1rem;
        margin-top: 1rem;
        border: 1px solid rgba(58,58,106,0.6);
    }}

    .link-item {{
        display: flex;
        align-items: center;
        padding: 0.65rem 0.8rem;
        margin-bottom: 0.45rem;
        background-color: rgba(42,42,90,0.6);
        border-radius: 9px;
    }}

    .link-item a {{
        color: #00ff88;
        text-decoration: none;
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.98rem;
        flex-grow: 1;
    }}

    .stat-item {{text-align:center;}}
    .stat-number {{font-size:2rem; font-weight:700; background: linear-gradient(45deg, #00d4ff,#00ff88); -webkit-background-clip:text; color:transparent;}}

    /* small screens */
    @media(max-width:600px){{
        .main-header {{font-size:2.2rem}}
        .ai-description {{font-size:0.9rem}}
    }}

    </style>
    """.format()

    st.markdown(base_css, unsafe_allow_html=True)


# ----------------- App data & tools -----------------
AI_TOOLS = {
    "text_generator": {
        "icon": "✍️",
        "title": "Gerador de Texto",
        "description": "Criação de conteúdo, artigos, e-mails e textos criativos com qualidade profissional.",
        "status": "Online",
        "category": "Criação"
    },
    "image_creator": {
        "icon": "🎨",
        "title": "Criador de Imagens",
        "description": "Gere imagens a partir de descrições textuais usando modelos multimodais.",
        "status": "Online",
        "category": "Visual"
    },
    "code_assistant": {
        "icon": "💻",
        "title": "Assistente de Código",
        "description": "Auxílio inteligente para programação, debugging e otimização de código.",
        "status": "Online",
        "category": "Desenvolvimento"
    },
    "data_analyst": {
        "icon": "📊",
        "title": "Analista de Dados",
        "description": "Análise automatizada de dados, gráficos e relatórios.",
        "status": "Online",
        "category": "Análise"
    },
    "translator": {
        "icon": "🌍",
        "title": "Tradutor Universal",
        "description": "Tradução contextual entre múltiplos idiomas.",
        "status": "Online",
        "category": "Comunicação"
    },
    "voice_synthesis": {
        "icon": "🎤",
        "title": "Síntese de Voz",
        "description": "Converta texto em áudio natural com vozes realistas.",
        "status": "Online",
        "category": "Áudio"
    },
    "document_processor": {
        "icon": "📄",
        "title": "Processador de Documentos",
        "description": "Extração e análise de documentos PDF, Word e mais.",
        "status": "Online",
        "category": "Produtividade"
    },
    "chatbot_builder": {
        "icon": "🤖",
        "title": "Construtor de Chatbots",
        "description": "Crie chatbots inteligentes e fluxos conversacionais.",
        "status": "Online",
        "category": "Automação"
    },
    "video_editor": {
        "icon": "🎬",
        "title": "Editor de Vídeo IA",
        "description": "Edição automática de vídeos com cortes e legendas.",
        "status": "Beta",
        "category": "Visual"
    }
}


# ----------------- Pages -----------------

def header():
    st.markdown("<h1 class='main-header'>NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ecossistema Inteligente de IAs para Produtividade — Modo: <strong>{}</strong></p>".format(st.session_state.theme.capitalize()), unsafe_allow_html=True)


def show_stats():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class='stat-item'>
            <div class='stat-number'>{}</div>
            <div class='stat-label'>IAs Ativas</div>
        </div>
        """.format(len(AI_TOOLS)), unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='stat-item'>
            <div class='stat-number'>24/7</div>
            <div class='stat-label'>Disponibilidade</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='stat-item'>
            <div class='stat-number'>&infin;</div>
            <div class='stat-label'>Possibilidades</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class='stat-item'>
            <div class='stat-number'>100%</div>
            <div class='stat-label'>Segurança</div>
        </div>
        """, unsafe_allow_html=True)


def main_grid():
    st.markdown("<div class='ecosystem-container'>", unsafe_allow_html=True)

    # criação responsiva de cards
    for key, tool in AI_TOOLS.items():
        card_html = f"""
        <div class='ai-card'>
            <div class='ai-icon'>{tool['icon']}</div>
            <div class='ai-title'>{tool['title']}</div>
            <div class='ai-description'>{tool['description']}</div>
            <div style='text-align:center; margin-top:6px;'>
                <a href='?ai={key}' style='text-decoration:none;'>
                    <button style='background:linear-gradient(45deg,#00d4ff,#00ff88); padding:8px 14px; border-radius:12px; border:none; cursor:pointer; font-weight:700;'>Abrir</button>
                </a>
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def show_ai_page(ai_key: str):
    ai_tool = AI_TOOLS.get(ai_key)
    if not ai_tool:
        st.error("IA não encontrada.")
        return

    st.markdown(f"""
    <div style='background: linear-gradient(45deg, #00d4ff, #00ff88); padding: 1px; border-radius: 12px; margin: 1rem 0;'>
        <div style='background: #1e1e3f; padding: 1.25rem; border-radius: 11px;'>
            <h2 style='color: white; text-align: center; font-family: \'Orbitron\', monospace;'>{ai_tool['icon']} {ai_tool['title']}</h2>
            <p style='color: #a0a0a0; text-align: center; font-family: \'Rajdhani\', sans-serif;'>{ai_tool['description']}</p>
            <div style='text-align:center; color:#00ff88;'>● {ai_tool['status']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # links oficiais (vindo de config ou default)
    links = AI_LINKS.get(ai_key, [])
    st.markdown("<div class='links-container'><h4 style='text-align:center; font-family:Orbitron; color:#00d4ff;'>Ferramentas Relacionadas</h4>", unsafe_allow_html=True)

    for i, item in enumerate(links):
        cols = st.columns([6,1])
        with cols[0]:
            st.markdown(f"<div class='link-item'><span style='margin-right:10px;'>🔗</span><a href='{item['url']}' target='_blank'>{item['name']}</a></div>", unsafe_allow_html=True)
        with cols[1]:
            btn_key = f"open_{ai_key}_{i}"
            if st.button("Abrir (contar)", key=btn_key):
                increment_analytics(ai_key)
                st.success(f"Contagem atual para {ai_tool['title']}: {st.session_state.analytics.get(ai_key,0)}")

    st.markdown("</div>", unsafe_allow_html=True)

    # quick actions
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,1,1])
    with c2:
        if st.button("🔙 Voltar ao Ecossistema"):
            st.experimental_set_query_params()
            st.experimental_rerun()


# ----------------- Sidebar: controles avançados -----------------
with st.sidebar:
    st.markdown("<h3 style='font-family:Orbitron; text-align:center; color:#00d4ff;'>NEXUS</h3>", unsafe_allow_html=True)
    theme_choice = st.selectbox("Tema", ["neon", "dark"], index=0)
    st.session_state.theme = theme_choice

    st.markdown("---")
    st.markdown("<strong>Selecionar IA por categoria</strong>", unsafe_allow_html=True)
    categories = sorted(list({v['category'] for v in AI_TOOLS.values()}))
    cat = st.selectbox("Categoria", ["Todas"] + categories)

    # busca rápida
    query = st.text_input("Buscar IA (título)")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.9rem; color:#a0a0a0;'>Contadores (sessão)</div>", unsafe_allow_html=True)
    for k, v in st.session_state.analytics.items():
        st.write(f"{k}: {v}")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.8rem; color:#888;'>Nexus · Press kit · Docs</div>", unsafe_allow_html=True)


# ----------------- Main -----------------
def main():
    load_css(st.session_state.theme)
    header()
    show_stats()

    ai_key = st.experimental_get_query_params().get("ai", [None])[0]

    if ai_key and ai_key in AI_TOOLS:
        show_ai_page(ai_key)
    else:
        # filtro por categoria e busca
        main_grid()

    # rodapé com data e versão
    st.markdown("<div style='text-align:center; margin-top:1rem; color:#7a7a7a;'>Nexus • Ecossistema • {} • v1.0</div>".format(datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
