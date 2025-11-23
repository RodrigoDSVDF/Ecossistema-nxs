import streamlit as st
import time
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA (Obrigatório ser a primeira linha) ---
st.set_page_config(
    page_title="Nexus - Ecossistema de IAs",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DADOS E LINKS DO ECOSSISTEMA ---
AI_LINKS = {
    "text_generator": [
        {"name": "Claude 3.5 Sonnet", "url": "https://claude.ai", "desc": "Melhor raciocínio e escrita natural"},
        {"name": "ChatGPT-4o", "url": "https://chat.openai.com", "desc": "Multimodal e análise de dados"},
        {"name": "Gemini Advanced", "url": "https://gemini.google.com", "desc": "Ecossistema Google integrado"},
        {"name": "NotebookLM", "url": "https://notebooklm.google.com", "desc": "RAG instantâneo com seus documentos"}
    ],
    "image_creator": [
        {"name": "Midjourney", "url": "https://www.midjourney.com", "desc": "Qualidade artística superior"},
        {"name": "Leonardo.ai", "url": "https://leonardo.ai", "desc": "Controle total e assets de jogos"},
        {"name": "Ideogram", "url": "https://ideogram.ai", "desc": "Melhor para gerar textos dentro da imagem"},
        {"name": "Recraft", "url": "https://www.recraft.ai", "desc": "Design vetorial e ícones"}
    ],
    "code_assistant": [
        {"name": "Google AI Studio", "url": "https://aistudio.google.com", "desc": "Playground para Gemini 1.5 Pro/Flash"},
        {"name": "Cursor IDE", "url": "https://cursor.sh", "desc": "Editor de código nativo com IA"},
        {"name": "GitHub Copilot", "url": "https://github.com/features/copilot", "desc": "Autocomplete dentro do VS Code"},
        {"name": "V0.dev", "url": "https://v0.dev", "desc": "Geração de interface frontend (React/Tailwind)"}
    ],
    "data_analyst": [
        {"name": "Julius AI", "url": "https://julius.ai", "desc": "Data Science conversacional"},
        {"name": "DeepNote", "url": "https://deepnote.com", "desc": "Jupyter Notebook colaborativo com IA"},
        {"name": "Gingr", "url": "https://www.gingr.ai", "desc": "Visualização de dados complexos"}
    ],
    "research_search": [
        {"name": "Perplexity AI", "url": "https://www.perplexity.ai", "desc": "Busca em tempo real com citações"},
        {"name": "Consensus", "url": "https://consensus.app", "desc": "Busca em artigos científicos"},
        {"name": "Elicit", "url": "https://elicit.com", "desc": "Automação de revisão de literatura"}
    ],
    "translator": [
        {"name": "DeepL", "url": "https://www.deepl.com", "desc": "Tradução contextual precisa"},
        {"name": "ElevenLabs Dubbing", "url": "https://elevenlabs.io/dubbing", "desc": "Dublagem de vídeo automática"}
    ],
    "voice_synthesis": [
        {"name": "ElevenLabs", "url": "https://elevenlabs.io", "desc": "Vozes sintéticas indistinguíveis da real"},
        {"name": "Suno AI", "url": "https://suno.com", "desc": "Geração de músicas completas"},
        {"name": "Udio", "url": "https://www.udio.com", "desc": "Música de alta fidelidade"}
    ],
    "document_processor": [
        {"name": "ChatPDF", "url": "https://www.chatpdf.com", "desc": "Interaja com arquivos PDF"},
        {"name": "Humata", "url": "https://www.humata.ai", "desc": "Análise de contratos e papéis longos"}
    ],
    "video_editor": [
        {"name": "Runway Gen-3", "url": "https://runwayml.com", "desc": "O estado da arte em vídeo generativo"},
        {"name": "Luma Dream Machine", "url": "https://lumalabs.ai/dream-machine", "desc": "Vídeos realistas de alta qualidade"},
        {"name": "Kling AI", "url": "https://klingai.com", "desc": "Geração de vídeo com física realista"}
    ]
}

AI_TOOLS = {
    "text_generator": {"icon": "✍️", "title": "Gerador de Texto", "description": "LLMs para escrita, raciocínio e copy.", "status": "Online", "category": "Criação"},
    "code_assistant": {"icon": "💻", "title": "Dev & Código", "description": "IDEs, API Playgrounds e Autocomplete.", "status": "Online", "category": "Dev"},
    "data_analyst": {"icon": "📊", "title": "Data Science", "description": "Análise estatística e visualização.", "status": "Online", "category": "Dados"},
    "image_creator": {"icon": "🎨", "title": "Estúdio Visual", "description": "Geração de imagens e vetores.", "status": "Online", "category": "Visual"},
    "research_search": {"icon": "🔍", "title": "Pesquisa Deep", "description": "Busca conectada à web e papers.", "status": "Online", "category": "Pesquisa"},
    "voice_synthesis": {"icon": "🎧", "title": "Áudio & Música", "description": "Vozes neurais e composição musical.", "status": "Online", "category": "Áudio"},
    "video_editor": {"icon": "🎬", "title": "Vídeo Gen", "description": "Criação de vídeo a partir de texto.", "status": "Beta", "category": "Visual"},
    "document_processor": {"icon": "📄", "title": "Docs Inteligentes", "description": "RAG e análise de arquivos.", "status": "Online", "category": "Produtividade"},
    "translator": {"icon": "🌍", "title": "Tradução", "description": "Adaptação cultural e linguística.", "status": "Online", "category": "Global"}
}

# --- CSS CUSTOMIZADO (NEXUS THEME) ---
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #1a1a2e 0%, #0f0f23 100%);
        color: #e0e0e0;
    }
    
    h1, h2, h3, .ai-title { font-family: 'Orbitron', sans-serif !important; letter-spacing: 1px; }
    p, div, span, a { font-family: 'Rajdhani', sans-serif !important; }
    
    .main-header {
        text-align: center;
        padding: 3rem 0 1rem 0;
        background: linear-gradient(90deg, #00d4ff, #00ff88, #00d4ff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 5s linear infinite;
        font-weight: 900;
        font-size: 4rem;
        text-shadow: 0 0 30px rgba(0, 255, 136, 0.2);
    }
    
    @keyframes shine { to { background-position: 200% center; } }
    
    .subtitle {
        text-align: center; font-size: 1.2rem; color: #64748b;
        letter-spacing: 3px; margin-bottom: 3rem; text-transform: uppercase;
    }
    
    .ecosystem-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
        padding: 1rem 2rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .ai-card {
        background: rgba(30, 30, 50, 0.4);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 1.5rem;
        height: 100%;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .ai-card:hover {
        transform: translateY(-5px);
        background: rgba(40, 40, 70, 0.6);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 255, 136, 0.1);
        border-color: rgba(0, 255, 136, 0.3);
    }
    
    .ai-icon { font-size: 2.5rem; margin-bottom: 1rem; filter: drop-shadow(0 0 8px rgba(0, 212, 255, 0.4)); }
    .ai-title { font-size: 1.4rem; color: #fff; margin-bottom: 0.5rem; }
    .ai-description { color: #94a3b8; font-size: 1rem; line-height: 1.4; }
    
    .ai-status-wrapper {
        margin-top: 1rem; display: flex; align-items: center; justify-content: space-between;
    }
    
    .status-pill {
        display: flex; align-items: center; gap: 6px; font-size: 0.8rem;
        color: #00ff88; background: rgba(0, 255, 136, 0.05);
        padding: 4px 10px; border-radius: 12px; border: 1px solid rgba(0, 255, 136, 0.1);
    }
    
    .pulse-dot {
        width: 6px; height: 6px; background: #00ff88; border-radius: 50%;
        box-shadow: 0 0 8px #00ff88; animation: pulse 2s infinite;
    }
    
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    
    .links-wrapper { max-width: 900px; margin: 0 auto; padding: 2rem; }
    
    .link-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
        border-left: 3px solid #00d4ff; border-radius: 8px; padding: 1.5rem;
        margin-bottom: 1.2rem; display: flex; justify-content: space-between;
        align-items: center; transition: all 0.2s ease;
    }
    
    .link-card:hover {
        background: linear-gradient(145deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);
        transform: translateX(5px); box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .visit-btn {
        background: transparent; border: 1px solid #00ff88; color: #00ff88 !important;
        padding: 8px 20px; border-radius: 4px; text-decoration: none;
        font-weight: 600; text-transform: uppercase; font-size: 0.8rem;
        letter-spacing: 1px; transition: all 0.3s;
    }
    
    .visit-btn:hover {
        background: #00ff88; color: #000 !important;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.4);
    }
    
    .particle {
        position: absolute; width: 2px; height: 2px; background: #00d4ff;
        border-radius: 50%; animation: float 15s infinite linear; opacity: 0.3;
    }
    
    @keyframes float {
        0% { transform: translateY(100vh) translateX(0); opacity: 0; }
        50% { opacity: 0.5; }
        100% { transform: translateY(-100px) translateX(20px); opacity: 0; }
    }
    
    .stButton button { border-color: #333; color: #aaa; background-color: transparent; }
    .stButton button:hover { border-color: #00d4ff; color: #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

def create_particles():
    particles_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0;">'
    for i in range(30):
        left = (i * 3.5) % 100
        delay = i * 0.4
        particles_html += f'<div class="particle" style="left:{left}%; animation-delay:{delay}s;"></div>'
    particles_html += '</div>'
    st.markdown(particles_html, unsafe_allow_html=True)

def show_main_page():
    # Header e Stats
    st.markdown("<h1 class='main-header'>NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ecossistema Centralizado de Inteligência</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 4rem; margin-bottom: 3rem; flex-wrap: wrap;">
        <div style="text-align: center;"><div style="font-family: Orbitron; font-size: 1.8rem; color: #00ff88; font-weight: bold;">100%</div><div style="color: #666; font-size: 0.9rem; text-transform: uppercase;">Operacional</div></div>
        <div style="text-align: center;"><div style="font-family: Orbitron; font-size: 1.8rem; color: #00d4ff; font-weight: bold;">20+</div><div style="color: #666; font-size: 0.9rem; text-transform: uppercase;">Ferramentas</div></div>
        <div style="text-align: center;"><div style="font-family: Orbitron; font-size: 1.8rem; color: #fff; font-weight: bold;">PRO</div><div style="color: #666; font-size: 0.9rem; text-transform: uppercase;">Acesso</div></div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- CRIAÇÃO DO GRID (CORRIGIDA: REMOVIDA INDENTAÇÃO E ESPAÇOS) ---
    grid_html = "<div class='ecosystem-container'>"
    for key, tool in AI_TOOLS.items():
        # Usando f-string contínua para evitar blocos de código markdown indesejados
        grid_html += f"<a href='?ai={key}' target='_self' style='text-decoration: none; color: inherit; z-index: 1;'><div class='ai-card'><div><div class='ai-icon'>{tool['icon']}</div><div class='ai-title'>{tool['title']}</div><div class='ai-description'>{tool['description']}</div></div><div class='ai-status-wrapper'><div class='status-pill'><div class='pulse-dot'></div>{tool['status']}</div><span style='color: #444; font-size: 0.8rem;'>➔</span></div></div></a>"
    grid_html += "</div>"
    
    st.markdown(grid_html, unsafe_allow_html=True)

def show_ai_links_page(ai_key):
    ai_tool = AI_TOOLS.get(ai_key)
    if not ai_tool:
        st.error("Módulo não encontrado no servidor Nexus.")
        return

    st.markdown(f"""
    <div style='text-align: center; padding: 3rem 0; animation: fadeIn 0.5s ease;'>
        <div style='font-size: 4rem; margin-bottom: 1rem;'>{ai_tool['icon']}</div>
        <h1 style='font-family:Orbitron; font-size: 2.5rem; color: white; margin-bottom: 0.5rem;'>{ai_tool['title']}</h1>
        <p style='color: #00d4ff; font-family: Rajdhani; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase;'>/// Categoria: {ai_tool['category']}</p>
    </div>
    """, unsafe_allow_html=True)

    if ai_key in AI_LINKS:
        st.markdown("<div class='links-wrapper'>", unsafe_allow_html=True)
        for link in AI_LINKS[ai_key]:
            st.markdown(f"""
            <div class='link-card'>
                <div><h4 style='color: #fff; margin: 0; font-family: Orbitron; font-size: 1.1rem;'>{link['name']}</h4><p style='color: #889; margin: 5px 0 0 0; font-size: 0.95rem;'>{link['desc']}</p></div>
                <a href='{link['url']}' target='_blank' class='visit-btn'>Acessar</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Nenhuma ferramenta vinculada a este módulo ainda.")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 0.4, 1])
    with col2:
        if st.button("🔌 Desconectar Módulo", use_container_width=True):
            st.query_params.clear()
            st.rerun()

def main():
    load_css()
    create_particles()
    params = st.query_params
    ai_key = params.get("ai")
    
    if ai_key:
        show_ai_links_page(ai_key)
    else:
        show_main_page()

if __name__ == "__main__":
    main()
