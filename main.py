import streamlit as st
import time
from datetime import datetime
import base64
# Se você tiver esses arquivos, mantenha os imports. Caso contrário, pode removê-los.
# from components.ai_interfaces import AI_INTERFACES
# from config import AI_LINKS

# Configuração da página
st.set_page_config(
    page_title="Nexus - Ecossistema de IAs",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed")

# --- SEU CSS COMPLETO E DEMAIS FUNÇÕES (SEM ALTERAÇÕES) ---
# ... (Todo o seu código de CSS, create_particles, AI_TOOLS, etc., permanece aqui) ...

# Dados das IAs (exemplo, mantenha o seu)
AI_TOOLS = {
    "text_generator": {"icon": "✍️", "title": "Gerador de Texto", "description": "Descrição...", "status": "Online", "category": "Criação"},
    "image_creator": {"icon": "🎨", "title": "Criador de Imagens", "description": "Descrição...", "status": "Online", "category": "Visual"},
    # ... Suas outras ferramentas
}
# Dados de links (exemplo, mantenha o seu)
AI_LINKS = {}


# --- AJUSTE NA LÓGICA DE LOGIN E NAVEGAÇÃO ---

def show_login_page():
    """Mostra a página de login simbólico com Nome e E-mail."""
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
        submitted = st.form_submit_button("🚀 Acessar Nexus")

        if submitted:
            # Esta é a validação "simbólica": apenas verifica se os campos não estão vazios.
            if name and email:
                st.session_state['logged_in'] = True
                st.session_state['user_name'] = name # Guardamos o nome para uma mensagem de boas-vindas
                st.rerun()
            else:
                st.error("Por favor, preencha todos os campos.")
                
    st.markdown("</div></div>", unsafe_allow_html=True)

def show_main_page():
    """Mostra a página principal do ecossistema."""
    # Mensagem de boas-vindas personalizada
    if 'user_name' in st.session_state:
        st.markdown(f"### Bem-vindo, {st.session_state['user_name']}!")
        
    st.markdown("<h1 class='main-header'>NEXUS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ecossistema Inteligente de IAs para Produtividade</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='ecosystem-container'>", unsafe_allow_html=True)
    
    # Usando st.columns para criar o grid de forma mais robusta no Streamlit
    cols = st.columns(3)
    for idx, (key, ai_tool) in enumerate(AI_TOOLS.items()):
        col_idx = idx % 3
        with cols[col_idx]:
            # Mantendo seu design original com links HTML que alteram a URL
            card_html = f"""
            <a href='?ai={key}' target='_self' style='text-decoration: none;'>
                <div class='ai-card'>
                    <div class='ai-icon'>{ai_tool['icon']}</div>
                    <div class='ai-title'>{ai_tool['title']}</div>
                    <div class='ai-description'>{ai_tool['description']}</div>
                </div>
            </a>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
    st.markdown("</div>", unsafe_allow_html=True)


def show_ai_links_page(ai_key):
    """Mostra a página dedicada da ferramenta de IA."""
    ai_tool = AI_TOOLS.get(ai_key)
    if not ai_tool:
        st.error("IA não encontrada.")
        st.button("🔙 Voltar ao Ecossistema")
        return

    # Breadcrumb para navegação
    st.markdown(f"### [Ecossistema Nexus](/) > {ai_tool['title']}")
    
    # ... (Resto do código da sua página de links, que já está correto) ...
    # Exemplo: st.header(ai_tool['title'])
    
    # Botão para voltar
    if st.button("🔙 Voltar ao Ecossistema"):
        # Limpa o parâmetro da URL para voltar à página principal
        st.query_params.clear()
        st.rerun()


def main():
    # load_css() # Se tiver a função de CSS, descomente
    # create_particles() # Se tiver a função de partículas, descomente

    # --- LÓGICA CENTRAL ("O PORTEIRO") ---
    # 1. Se a "chave de acesso" não existir na memória, cria ela como False.
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # 2. Se a chave for False, mostra a tela de login.
    if not st.session_state['logged_in']:
        show_login_page()
    # 3. Se a chave for True, o usuário está dentro. Mostra o conteúdo.
    else:
        # Verifica a URL para saber qual página mostrar
        ai_key = st.query_params.get("ai")
        if ai_key:
            show_ai_links_page(ai_key)
        else:
            show_main_page()

if __name__ == "__main__":
    main()
