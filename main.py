import streamlit as st
import time
from datetime import datetime
import base64
# Removido pois não estavam sendo usados no código fornecido.
# Se você tiver esses arquivos, descomente as linhas abaixo.
# from components.ai_interfaces import AI_INTERFACES
# from config import AI_LINKS

# Exemplo de AI_LINKS para o código funcionar
AI_LINKS = {
    "text_generator": [{"name": "OpenAI GPT-4", "url": "https://openai.com"}, {"name": "Google Gemini", "url": "https://gemini.google.com"}],
    "image_creator": [{"name": "Midjourney", "url": "https://www.midjourney.com"}, {"name": "Stable Diffusion", "url": "https://stablediffusionweb.com/"}],
    # Adicione outros links se necessário
}


# Configuração da página
st.set_page_config(
    page_title="Nexus - Ecossistema de IAs",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed")

# CSS customizado para criar o visual futurista do ecossistema
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(45deg, #00d4ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        font-size: 3.5rem;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.2rem;
        color: #a0a0a0;
        margin-bottom: 3rem;
    }
    .ecosystem-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        padding: 2rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    .ai-card {
        background: linear-gradient(145deg, #1e1e3f, #2a2a5a);
        border-radius: 20px;
        padding: 2rem;
        border: 2px solid transparent;
        background-clip: padding-box;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    .ai-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, #00d4ff, #00ff88, #ff6b6b, #ffd93d);
        border-radius: 20px;
        padding: 2px;
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .ai-card:hover::before {
        opacity: 1;
    }
    .ai-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 212, 255, 0.2);
    }
    .ai-icon {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #00d4ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .ai-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    .ai-description {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1rem;
        text-align: center;
        color: #b0b0b0;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    .ai-status {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.9rem;
        color: #00ff88;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #00ff88;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .floating-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    .particle {
        position: absolute;
        width: 2px;
        height: 2px;
        background: #00d4ff;
        border-radius: 50%;
        animation: float 6s infinite linear;
    }
    @keyframes float {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
    .stats-container {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin: 3rem 0;
        flex-wrap: wrap;
    }
    .stat-item {
        text-align: center;
        font-family: 'Rajdhani', sans-serif;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #00d4ff, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .stat-label {
        font-size: 1rem;
        color: #a0a0a0;
        margin-top: 0.5rem;
    }
    .stButton > button {
        background: linear-gradient(45deg, #00d4ff, #00ff88);
        color: #000;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-family: 'Orbitron', monospace;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.5);
    }
    .links-container {
        background: linear-gradient(145deg, #1e1e3f, #2a2a5a);
        border-radius: 15px;
        padding: 1.5rem;
        margin-top: 2rem;
        border: 1px solid #3a3a6a;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .links-container h4 {
        color: #00d4ff;
        font-family: 'Orbitron', monospace;
        margin-bottom: 1rem;
        text-align: center;
    }
    .link-item {
        display: flex;
        align-items: center;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        background-color: #2a2a5a;
        border-radius: 10px;
        transition: background-color 0.2s ease;
    }
    .link-item:hover {
        background-color: #3a3a6a;
    }
    .link-item a {
        color: #00ff88;
        text-decoration: none;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
        flex-grow: 1;
    }
    .link-item .icon {
        margin-right: 0.75rem;
        color: #00d4ff;
        font-size: 1.2rem;
    }
    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        padding: 2rem;
    }
    .login-card {
        background: linear-gradient(145deg, #1e1e3f, #2a2a5a);
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        text-align: center;
        max-width: 500px;
        width: 100%;
    }
    .login-card h2 {
        font-family: 'Orbitron', monospace;
        color: #00d4ff;
        margin-bottom: 1.5rem;
        font-size: 2rem;
    }
    .login-card .stTextInput > div > div > input {
        background-color: #1a1a2e;
        border: 1px solid #00d4ff;
        color: #ffffff;
        border-radius: 10px;
        padding: 0.75rem 1rem;
    }
    .login-card .stTextInput > label {
        color: #a0a0a0;
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
    }
    .login-card .stButton > button {
        width: 100%;
        margin-top: 1.5rem;
        background: linear-gradient(45deg, #00ff88, #00d4ff);
        color: #000;
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        font-size: 1.2rem;
        border-radius: 15px;
        padding: 1rem;
        transition: all 0.3s ease;
    }
    .login-card .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 255, 136, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# Função para criar partículas flutuantes
def create_particles():
    particles_html = "<div class=\"floating-particles\">"
    for i in range(20):
        delay = i * 0.3
        left = (i * 5) % 100
        particles_html += f"<div class=\"particle\" style=\"left: {left}%; animation-delay: {delay}s;\"></div>"
    particles_html += "</div>"
    st.markdown(particles_html, unsafe_allow_html=True)

# Dados das IAs disponíveis no ecossistema
AI_TOOLS = {
    "text_generator": {"icon": "✍️", "title": "Gerador de Texto", "description": "IA avançada para criação de conteúdo, artigos, e-mails e textos criativos com qualidade profissional.", "status": "Online", "category": "Criação"},
    "image_creator": {"icon": "🎨", "title": "Criador de Imagens", "description": "Gere imagens incríveis a partir de descrições textuais usando modelos de IA de última geração.", "status": "Online", "category": "Visual"},
    "code_assistant": {"icon": "💻", "title": "Assistente de Código", "description": "Auxílio inteligente para programação, debugging e otimização de código em múltiplas linguagens.", "status": "Online", "category": "Desenvolvimento"},
    "data_analyst": {"icon": "📊", "title": "Analista de Dados", "description": "Análise avançada de dados, criação de gráficos e insights automatizados para tomada de decisão.", "status": "Online", "category": "Análise"},
    "translator": {"icon": "🌍", "title": "Tradutor Universal", "description": "Tradução precisa e contextual entre mais de 100 idiomas com preservação de nuances.", "status": "Online", "category": "Comunicação"},
    "voice_synthesis": {"icon": "🎤", "title": "Síntese de Voz", "description": "Converta texto em áudio natural com vozes realistas e controle de entonação.", "status": "Online", "category": "Áudio"},
    "document_processor": {"icon": "📄", "title": "Processador de Documentos", "description": "Extraia, analise e processe informações de documentos PDF, Word e outros formatos.", "status": "Online", "category": "Produtividade"},
    "chatbot_builder": {"icon": "🤖", "title": "Construtor de Chatbots", "description": "Crie chatbots inteligentes personalizados para atendimento e automação de processos.", "status": "Online", "category": "Automação"},
    "video_editor": {"icon": "🎬", "title": "Editor de Vídeo IA", "description": "Edição automática de vídeos com cortes inteligentes, legendas e efeitos visuais.", "status": "Beta", "category": "Visual"}
}

def show_login_page():
    st.markdown("""
    <div class="login-container">
        <div class="login-card">
            <h2>Bem-vindo ao Nexus</h2>
            <p style="color: #a0a0a0; font-family: 'Rajdhani', sans-serif; margin-bottom: 1.5rem;">
                Insira seu nome e e-mail para acessar o ecossistema de IAs.
            </p>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        name = st.text_input("Nome", key="login_name")
        email = st.text_input("E-mail", key="login_email")
        submitted = st.form_submit_button("Acessar Nexus")
        if submitted:
            if name and email:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Por favor, preencha todos os campos.")
                
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_main_page():
    """Mostra a página principal do ecossistema"""
    st.markdown("<h1 class='main-header'>NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ecossistema Inteligente de IAs para Produtividade</p>", unsafe_allow_html=True)

    # Estatísticas do ecossistema
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class='stat-item'>
            <div class='stat-number'>9</div>
            <div class='stat-label'>IAs Ativas</div>
        </div>
        """, unsafe_allow_html=True)
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
            <div class='stat-number'>∞</div>
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
        
    st.markdown("<br>", unsafe_allow_html=True)

    # Container do ecossistema
    st.markdown("<div class='ecosystem-container'>", unsafe_allow_html=True)
    
    # Criar cards das IAs em grid
    cols = st.columns(3)
    for idx, (key, ai_tool) in enumerate(AI_TOOLS.items()):
        col_idx = idx % 3
        with cols[col_idx]:
            card_html = f"""
            <a href='?ai={key}' target='_self' style='text-decoration: none;'>
                <div class='ai-card'>
                    <div class='ai-icon'>{ai_tool['icon']}</div>
                    <div class='ai-title'>{ai_tool['title']}</div>
                    <div class='ai-description'>{ai_tool['description']}</div>
                    <div class='ai-status'>
                        <div class='status-dot'></div>
                        {ai_tool['status']}
                    </div>
                </div>
            </a>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
    st.markdown("</div>", unsafe_allow_html=True)

def show_ai_links_page(ai_key):
    """Mostra apenas a seção de links relacionados para a IA selecionada"""
    ai_tool = AI_TOOLS.get(ai_key)
    if not ai_tool:
        st.error("IA não encontrada.")
        return

    # Header da IA selecionada
    st.markdown(f"""
    <div style='background: linear-gradient(45deg, #00d4ff, #00ff88); padding: 1px; border-radius: 15px; margin: 2rem 0;'>
        <div style='background: #1e1e3f; padding: 2rem; border-radius: 14px;'>
            <h2 style='color: white; text-align: center; font-family: \"Orbitron\", monospace;'>
                {ai_tool['icon']} {ai_tool['title']}
            </h2>
            <p style='color: #a0a0a0; text-align: center; font-family: \"Rajdhani\", sans-serif;'>
                {ai_tool['description']}
            </p>
            <div style='text-align: center;'>
                <span style='color: #00ff88;'>● {ai_tool['status']}</span>
                <span style='color: #a0a0a0; margin-left: 2rem;'>Categoria: {ai_tool['category']}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Exibir links relacionados, se houver
    if ai_key in AI_LINKS and AI_LINKS[ai_key]:
        st.markdown("<div class='links-container'><h4>Ferramentas Relacionadas</h4>", unsafe_allow_html=True)
        for link_item in AI_LINKS[ai_key]:
            st.markdown(f"""
            <div class='link-item'>
                <span class='icon'>🔗</span>
                <a href='{link_item['url']}' target='_blank'>{link_item['name']}</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info(f"Nenhum link relacionado encontrado para {ai_tool['title']}.")

    # Botão para voltar ao ecossistema
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔙 Voltar ao Ecossistema"):
            st.query_params.clear()
            st.rerun()

def main():
    load_css()
    create_particles()
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        
    if not st.session_state.logged_in:
        show_login_page()
    else:
        query_params = st.query_params
        ai_key = query_params.get("ai")
        if ai_key and ai_key in AI_TOOLS:
            show_ai_links_page(ai_key)
        else:
            show_main_page()

if __name__ == "__main__":
    main()
