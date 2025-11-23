import streamlit as st
import time
from datetime import datetime

# --- DADOS E LINKS DO ECOSSISTEMA (Atualizado com Ferramentas de Mercado) ---
AI_LINKS = {
    "text_generator": [
        {"name": "Claude 3.5 Sonnet (Anthropic)", "url": "https://claude.ai", "desc": "Melhor para nuance e codificação"},
        {"name": "ChatGPT-4o (OpenAI)", "url": "https://chat.openai.com", "desc": "O padrão da indústria, multimodal"},
        {"name": "Gemini Advanced (Google)", "url": "https://gemini.google.com", "desc": "Integração nativa com ecossistema Google"},
        {"name": "Jasper AI", "url": "https://www.jasper.ai", "desc": "Focado em marketing e copywriting"}
    ],
    "image_creator": [
        {"name": "Midjourney", "url": "https://www.midjourney.com", "desc": "Qualidade artística superior"},
        {"name": "DALL-E 3", "url": "https://openai.com/dall-e-3", "desc": "Fácil uso via ChatGPT"},
        {"name": "Leonardo.ai", "url": "https://leonardo.ai", "desc": "Ótimo para assets de jogos e controle"},
        {"name": "Ideogram", "url": "https://ideogram.ai", "desc": "Excelente para tipografia em imagens"}
    ],
    "code_assistant": [
        {"name": "GitHub Copilot", "url": "https://github.com/features/copilot", "desc": "Autocomplete inteligente na IDE"},
        {"name": "Cursor", "url": "https://cursor.sh", "desc": "IDE focada em IA (Fork do VS Code)"},
        {"name": "Replit Ghostwriter", "url": "https://replit.com", "desc": "Codificação colaborativa na nuvem"},
        {"name": "V0.dev (Vercel)", "url": "https://v0.dev", "desc": "Geração de UI/Frontend React"}
    ],
    "data_analyst": [
        {"name": "Julius AI", "url": "https://julius.ai", "desc": "Análise de dados conversacional"},
        {"name": "PandasAI", "url": "https://github.com/gventuri/pandas-ai", "desc": "Biblioteca Python para IA em Dataframes"},
        {"name": "Tableau AI", "url": "https://www.tableau.com", "desc": "Analytics visual empresarial"}
    ],
    "translator": [
        {"name": "DeepL", "url": "https://www.deepl.com", "desc": "Tradução mais natural do mercado"},
        {"name": "Google Translate", "url": "https://translate.google.com", "desc": "Versatilidade e quantidade de idiomas"}
    ],
    "voice_synthesis": [
        {"name": "ElevenLabs", "url": "https://elevenlabs.io", "desc": "Vozes ultra-realistas e clonagem"},
        {"name": "Murf.ai", "url": "https://murf.ai", "desc": "Estúdio de voz profissional"}
    ],
    "document_processor": [
        {"name": "ChatPDF", "url": "https://www.chatpdf.com", "desc": "Converse com seus PDFs"},
        {"name": "Humata", "url": "https://www.humata.ai", "desc": "Análise técnica de documentos longos"}
    ],
    "video_editor": [
        {"name": "Runway Gen-2", "url": "https://runwayml.com", "desc": "Geração e edição de vídeo generativa"},
        {"name": "HeyGen", "url": "https://www.heygen.com", "desc": "Avatares falantes para apresentações"},
        {"name": "Pika Labs", "url": "https://pika.art", "desc": "Animação de vídeo criativa"}
    ],
    "research_search": [ # Nova Categoria Adicionada
        {"name": "Perplexity AI", "url": "https://www.perplexity.ai", "desc": "Pesquisa em tempo real com fontes"},
        {"name": "Consensus", "url": "https://consensus.app", "desc": "Pesquisa científica baseada em papers"}
    ]
}

AI_TOOLS = {
    "text_generator": {"icon": "✍️", "title": "Gerador de Texto", "description": "IA avançada para criação de conteúdo, artigos e copy.", "status": "Online", "category": "Criação"},
    "image_creator": {"icon": "🎨", "title": "Criador de Imagens", "description": "Gere visuais artísticos e realistas via prompt.", "status": "Online", "category": "Visual"},
    "code_assistant": {"icon": "💻", "title": "Assistente de Código", "description": "Auxílio para dev, debugging e arquitetura.", "status": "Online", "category": "Dev"},
    "data_analyst": {"icon": "📊", "title": "Analista de Dados", "description": "Insights automatizados e visualização de dados.", "status": "Online", "category": "Análise"},
    "research_search": {"icon": "🔍", "title": "Pesquisa & Busca", "description": "Motores de busca baseados em LLMs e ciência.", "status": "Online", "category": "Pesquisa"},
    "translator": {"icon": "🌍", "title": "Tradutor Neural", "description": "Tradução contextual de alta precisão.", "status": "Online", "category": "Comunicação"},
    "voice_synthesis": {"icon": "🎤", "title": "Síntese de Voz", "description": "Text-to-Speech ultra realista.", "status": "Online", "category": "Áudio"},
    "document_processor": {"icon": "📄", "title": "Docs & PDF", "description": "Extração e chat com documentos.", "status": "Online", "category": "Produtividade"},
    "video_editor": {"icon": "🎬", "title": "Vídeo IA", "description": "Geração e edição generativa de vídeos.", "status": "Beta", "category": "Visual"}
}

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Nexus - Ecossistema de IAs",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS FUTURISTA (DARK EMERALD THEME) ---
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    /* Base Theme */
    .stApp {
        background: radial-gradient(circle at center, #1a1a2e 0%, #0f0f23 100%);
        color: #e0e0e0;
    }
    
    /* Typography */
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; letter-spacing: 2px; }
    p, div, span, a { font-family: 'Rajdhani', sans-serif; }
    
    /* Nexus Header */
    .main-header {
        text-align: center;
        padding: 3rem 0 1rem 0;
        background: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 5s linear infinite;
        font-weight: 900;
        font-size: 4.5rem;
        text-shadow: 0 0 40px rgba(0, 255, 136, 0.3);
    }
    
    @keyframes shine {
        to { background-position: 200% center; }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #64748b;
        letter-spacing: 4px;
        margin-bottom: 4rem;
        text-transform: uppercase;
    }
    
    /* Grid Layout */
    .ecosystem-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 2rem;
        padding: 1rem 4rem;
        max-width: 1600px;
        margin: 0 auto;
    }
    
    /* Glassmorphism Cards */
    .ai-card {
        background: rgba(30, 30, 50, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 2rem;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    /* Hover Effects */
    .ai-card:hover {
        transform: translateY(-8px) scale(1.02);
        background: rgba(30, 30, 60, 0.6);
        border-color: rgba(0, 255, 136, 0.3);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 
                    0 0 30px rgba(0, 255, 136, 0.1);
    }
    
    .ai-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        filter: drop-shadow(0 0 10px rgba(0, 212, 255, 0.3));
    }
    
    .ai-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #fff;
        margin-bottom: 0.8rem;
    }
    
    .ai-description {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }
    
    /* Status Badge */
    .ai-status-badge {
        display: inline-flex;
        align-items: center;
        background: rgba(0, 255, 136, 0.1);
        border: 1px solid rgba(0, 255, 136, 0.2);
        border-radius: 20px;
        padding: 0.4rem 1rem;
        font-size: 0.85rem;
        color: #00ff88;
        width: fit-content;
    }
    
    .status-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #00ff88;
        margin-right: 8px;
        box-shadow: 0 0 10px #00ff88;
        animation: pulse 2s infinite;
    }
    
    /* Link Page Styles */
    .links-wrapper {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .link-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.3s ease;
    }
    
    .link-card:hover {
        background: rgba(255, 255, 255, 0.07);
        border-color: #00d4ff;
        transform: translateX(5px);
    }
    
    .link-info h4 { margin: 0; color: #fff; font-size: 1.2rem; }
    .link-info p { margin: 5px 0 0 0; color: #94a3b8; font-size: 0.9rem; }
    
    .visit-btn {
        background: linear-gradient(45deg, #00d4ff, #0055ff);
        color: white !important;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }
    
    .visit-btn:hover { box-shadow: 0 0 15px rgba(0, 212, 255, 0.5); }
    
    /* Particles */
    .particle {
        position: absolute;
        width: 3px;
        height: 3px;
        background: rgba(0, 212, 255, 0.5);
        border-radius: 50%;
        animation: float-up 10s infinite linear;
    }
    
    @keyframes float-up {
        0% { transform: translateY(100vh) scale(0); opacity: 0; }
        50% { opacity: 0.8; }
        100% { transform: translateY(-10vh) scale(1); opacity: 0; }
    }
    
    /* Custom Button Overrides */
    .stButton > button {
        background: transparent;
        border: 1px solid #00d4ff;
        color: #00d4ff;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background: rgba(0, 212, 255, 0.1);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

def create_particles():
    particles_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:-1;">'
    for i in range(25):
        left = (i * 4) % 100
        delay = i * 0.5
        particles_html += f'<div class="particle" style="left:{left}%; animation-delay:{delay}s;"></div>'
    particles_html += '</div>'
    st.markdown(particles_html, unsafe_allow_html=True)

def show_main_page():
    # Header Principal
    st.markdown("<h1 class='main-header'>NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ecossistema de Inteligência Artificial</p>", unsafe_allow_html=True)
    
    # KPIs Rápidos
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown("<div style='text-align:center; color:#00ff88; font-size:2rem; font-weight:bold;'>9+</div><div style='text-align:center; color:#666;'>Categorias</div>", unsafe_allow_html=True)
    with col2: st.markdown("<div style='text-align:center; color:#00d4ff; font-size:2rem; font-weight:bold;'>PRO</div><div style='text-align:center; color:#666;'>Nível de Acesso</div>", unsafe_allow_html=True)
    with col3: st.markdown("<div style='text-align:center; color:#fff; font-size:2rem; font-weight:bold;'>v2.0</div><div style='text-align:center; color:#666;'>System Core</div>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Grid de Apps
    st.markdown("<div class='ecosystem-container'>", unsafe_allow_html=True)
    
    cols = st.columns(3) # Layout apenas para controle de fluxo do Streamlit
    
    # Iterando e criando o Grid Manualmente via HTML para controle total do CSS
    html_grid = ""
    for key, tool in AI_TOOLS.items():
        html_grid += f"""
        <a href='?ai={key}' target='_self' style='text-decoration: none; color: inherit;'>
            <div class='ai-card'>
                <div>
                    <div class='ai-icon'>{tool['icon']}</div>
                    <div class='ai-title'>{tool['title']}</div>
                    <div class='ai-description'>{tool['description']}</div>
                </div>
                <div class='ai-status-badge'>
                    <div class='status-dot'></div>
                    {tool['status']}
                </div>
            </div>
        </a>
        """
    
    # Renderizando o grid CSS customizado
    st.markdown(f"<div class='ecosystem-container'>{html_grid}</div>", unsafe_allow_html=True)

def show_ai_links_page(ai_key):
    ai_tool = AI_TOOLS.get(ai_key)
    if not ai_tool:
        st.error("Módulo não encontrado.")
        return

    # Header da Sub-página
    st.markdown(f"""
    <div style='text-align: center; padding: 4rem 0 2rem 0;'>
        <div style='font-size: 5rem; margin-bottom: 1rem;'>{ai_tool['icon']}</div>
        <h1 style='font-family:Orbitron; font-size: 3rem; background: linear-gradient(to right, #fff, #a5a5a5); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            {ai_tool['title']}
        </h1>
        <p style='color: #00ff88; font-family: Rajdhani; font-size: 1.2rem; letter-spacing: 2px;'>
            /// MÓDULO {ai_tool['category'].upper()} ATIVADO
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Lista de Links
    if ai_key in AI_LINKS:
        st.markdown("<div class='links-wrapper'>", unsafe_allow_html=True)
        for link in AI_LINKS[ai_key]:
            st.markdown(f"""
            <div class='link-card'>
                <div class='link-info'>
                    <h4>{link['name']}</h4>
                    <p>{link['desc']}</p>
                </div>
                <a href='{link['url']}' target='_blank' class='visit-btn'>ACESSAR ↗</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Nenhum link cadastrado para esta categoria ainda.")

    # Botão Voltar
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 0.5, 1])
    with c2:
        if st.button("⏪ RETORNAR AO NEXUS", use_container_width=True):
            st.query_params.clear()
            st.rerun()

def main():
    load_css()
    create_particles()
    
    # Router Simples
    ai_key = st.query_params.get("ai")
    
    if ai_key:
        show_ai_links_page(ai_key)
    else:
        show_main_page()

if __name__ == "__main__":
    main()
