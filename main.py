import streamlit as st
import time
from datetime import datetime
import base64

# Exemplo de AI_LINKS para o código funcionar
AI_LINKS = {
    "text_generator": [{"name": "OpenAI GPT-4", "url": "https://openai.com"}, {"name": "Google Gemini", "url": "https://gemini.google.com"}],
    "image_creator": [{"name": "Midjourney", "url": "https://www.midjourney.com"}, {"name": "Stable Diffusion", "url": "https://stablediffusionweb.com/"}],
}

# --- CONFIGURAÇÕES E ESTILOS (Sem alterações) ---
st.set_page_config(
    page_title="Nexus - Ecossistema de IAs",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed")

def load_css():
    st.markdown("""
    <style>
    /* SEU CSS COMPLETO VAI AQUI (mantido igual ao original) */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
    }
    .main-header {
        text-align: center; padding: 2rem 0; background: linear-gradient(45deg, #00d4ff, #00ff88);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
        font-family: 'Orbitron', monospace; font-weight: 900; font-size: 3.5rem;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.5); margin-bottom: 1rem;
    }
    .subtitle { text-align: center; font-family: 'Rajdhani', sans-serif; font-size: 1.2rem; color: #a0a0a0; margin-bottom: 3rem; }
    .ecosystem-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; padding: 2rem; max-width: 1400px; margin: 0 auto; }
    .ai-card { background: linear-gradient(145deg, #1e1e3f, #2a2a5a); border-radius: 20px; padding: 2rem; border: 2px solid transparent; background-clip: padding-box; position: relative; overflow: hidden; transition: all 0.3s ease; cursor: pointer; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3); }
    .ai-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(45deg, #00d4ff, #00ff88, #ff6b6b, #ffd93d); border-radius: 20px; padding: 2px; mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); mask-composite: exclude; opacity: 0; transition: opacity 0.3s ease; }
    .ai-card:hover::before { opacity: 1; }
    .ai-card:hover { transform: translateY(-10px) scale(1.02); box-shadow: 0 20px 40px rgba(0, 212, 255, 0.2); }
    .ai-icon { font-size: 3rem; text-align: center; margin-bottom: 1rem; background: linear-gradient(45deg, #00d4ff, #00ff88); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .ai-title { font-family: 'Orbitron', monospace; font-size: 1.5rem; font-weight: 700; text-align: center; margin-bottom: 1rem; color: #ffffff; }
    .ai-description { font-family: 'Rajdhani', sans-serif; font-size: 1rem; text-align: center; color: #b0b0b0; line-height: 1.6; margin-bottom: 1.5rem; }
    .ai-status { display: flex; align-items: center; justify-content: center; gap: 0.5rem; font-family: 'Rajdhani', sans-serif; font-size: 0.9rem; color: #00ff88; }
    .status-dot { width: 8px; height: 8px; border-radius: 50%; background: #00ff88; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    .login-container { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 80vh; padding: 2rem; }
    .login-card { background: linear-gradient(145deg, #1e1e3f, #2a2a5a); border-radius: 20px; padding: 3rem; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5); text-align: center; max-width: 500px; width: 100%; }
    .login-card h2 { font-family: 'Orbitron', monospace; color: #00d4ff; margin-bottom: 1.5rem; font-size: 2rem; }
    .login-card .stTextInput > div > div > input { background-color: #1a1a2e; border: 1px solid #00d4ff; color: #ffffff; border-radius: 10px; padding: 0.75rem 1rem; }
    .login-card .stButton > button { width: 100%; margin-top: 1.5rem; background: linear-gradient(45deg, #00ff88, #00d4ff); color: #000; font-family: 'Orbitron', monospace; font-weight: 700; font-size: 1.2rem; border-radius: 15px; padding: 1rem; transition: all 0.3s ease; }
    </style>
    """, unsafe_allow_html=True)

# --- DADOS E FUNÇÕES DAS PÁGINAS (Sem alterações) ---
AI_TOOLS = {
    "text_generator": {"icon": "✍️", "title": "Gerador de Texto", "description": "IA avançada para criação de conteúdo, artigos, e-mails e textos criativos com qualidade profissional.", "status": "Online", "category": "Criação"},
    "image_creator": {"icon": "🎨", "title": "Criador de Imagens", "description": "Gere imagens incríveis a partir de descrições textuais usando modelos de IA de última geração.", "status": "Online", "category": "Visual"},
    # ... resto das ferramentas
}

def show_main_page():
    """Mostra a página principal do ecossistema (mantida igual)"""
    st.markdown("<h1 class='main-header'>NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ecossistema Inteligente de IAs para Produtividade</p>", unsafe_allow_html=True)
    # ... resto do código da página principal

def show_ai_links_page(ai_key):
    """Mostra a página de links da IA (mantida igual)"""
    # ... código da página de links

# --- NOVA LÓGICA DE LOGIN ---

def login_page():
    """Exibe a tela de login e processa a senha."""
    st.markdown("""
    <div class="login-container">
        <div class="login-card">
            <h2>Bem-vindo ao Nexus</h2>
            <p style="color: #a0a0a0; font-family: 'Rajdhani', sans-serif; margin-bottom: 1.5rem;">
                Insira a senha para acessar o ecossistema de IAs.
            </p>
    """, unsafe_allow_html=True)

    # Use um formulário para agrupar o campo de senha e o botão
    with st.form("login_form"):
        password = st.text_input("Senha", type="password", key="password")
        submitted = st.form_submit_button("Acessar Nexus")

        # Verifica a senha SOMENTE quando o botão é pressionado
        if submitted:
            # Substitua "SUA_SENHA_SECRETA" pela senha que você desejar
            if password == "SUA_SENHA_SECRETA":
                st.session_state["logged_in"] = True
                st.rerun()  # Roda o script novamente para mostrar a página principal
            else:
                st.error("Senha incorreta. Tente novamente.")
    
    st.markdown("</div></div>", unsafe_allow_html=True)


# --- FUNÇÃO PRINCIPAL COM A LÓGICA CORRIGIDA ---

def main():
    """Função principal que controla o fluxo da aplicação."""
    load_css()
    # create_particles() # Descomente se tiver a função create_particles

    # 1. Inicializa a variável de estado de login se ela não existir
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # 2. Verifica o estado do login
    # Se o usuário NÃO estiver logado, mostra a página de login
    if not st.session_state["logged_in"]:
        login_page()
    
    # Se o usuário ESTIVER logado, mostra o conteúdo principal
    else:
        query_params = st.query_params
        ai_key = query_params.get("ai")

        if ai_key and ai_key in AI_TOOLS:
            show_ai_links_page(ai_key)
        else:
            show_main_page()

if __name__ == "__main__":
    main()
