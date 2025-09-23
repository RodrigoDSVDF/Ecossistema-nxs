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
    # Seu CSS completo entra aqui. Foi omitido para encurtar a resposta.
    st.markdown("""<style> ... Seu CSS completo aqui ... </style>""", unsafe_allow_html=True)


# --- DADOS E FUNÇÕES DAS PÁGINAS (Sem alterações) ---
AI_TOOLS = {
    "text_generator": {"icon": "✍️", "title": "Gerador de Texto", "description": "IA avançada para criação de conteúdo...", "status": "Online", "category": "Criação"},
    "image_creator": {"icon": "🎨", "title": "Criador de Imagens", "description": "Gere imagens incríveis a partir de descrições...", "status": "Online", "category": "Visual"},
    # ... resto das suas ferramentas
}

def show_main_page():
    """Mostra a página principal do ecossistema."""
    st.markdown("<h1 class='main-header'>NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ecossistema Inteligente de IAs para Produtividade</p>", unsafe_allow_html=True)
    # ... resto do código da sua página principal ...
    
    st.markdown("<div class='ecosystem-container'>", unsafe_allow_html=True)
    cols = st.columns(3)
    for idx, (key, ai_tool) in enumerate(AI_TOOLS.items()):
        col_idx = idx % 3
        with cols[col_idx]:
            card_html = f"""
            <a href='?ai={key}' target='_self' style='text-decoration: none;'>
                <div class='ai-card'>
                    <div class='ai-icon'>{ai_tool['icon']}</div>
                    <div class='ai-title'>{ai_tool['title']}</div>
                </div>
            </a>
            """
            st.markdown(card_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def show_ai_links_page(ai_key):
    """Mostra a página de links da IA."""
    st.title(f"Página da Ferramenta: {ai_key}")
    # ... resto do código da sua página de links ...


# --- LÓGICA DE LOGIN REFEITA ---

def login_page():
    """
    Exibe a tela de login com Nome e Senha.
    Retorna True se o login for bem-sucedido, False caso contrário.
    """
    st.markdown("""<div class="login-container"><div class="login-card">""", unsafe_allow_html=True)
    
    with st.form("credentials_form"):
        st.markdown("<h2>Bem-vindo ao Nexus</h2>", unsafe_allow_html=True)
        name = st.text_input("Nome", key="login_name")
        password = st.text_input("Senha", type="password", key="login_password")
        submitted = st.form_submit_button("Acessar Nexus")

        if submitted:
            # --- CONFIGURE SEU LOGIN E SENHA AQUI ---
            # Para segurança, use st.secrets em uma aplicação real.
            if name == "admin" and password == "12345":
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Nome de usuário ou senha incorretos.")

    st.markdown("""</div></div>""", unsafe_allow_html=True)


# --- FUNÇÃO PRINCIPAL COM A LÓGICA CORRIGIDA ---

def main():
    """Função principal que controla o fluxo da aplicação."""
    load_css()
    # create_particles() # Descomente se tiver a função create_particles

    # 1. Inicializa a variável 'logged_in' na memória da sessão se ela não existir.
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # 2. Verifica o estado do login (o "Porteiro")
    # Se o usuário NÃO estiver logado, mostra a página de login e para a execução aqui.
    if not st.session_state["logged_in"]:
        login_page()
    
    # 3. Se o usuário JÁ ESTIVER logado, mostra o conteúdo principal do aplicativo.
    else:
        query_params = st.query_params
        ai_key = query_params.get("ai")

        if ai_key and ai_key in AI_TOOLS:
            show_ai_links_page(ai_key)
        else:
            show_main_page()

if __name__ == "__main__":
    main()
