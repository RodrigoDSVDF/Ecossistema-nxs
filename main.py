import streamlit as st
import time
from datetime import datetime
import base64
# A importação de AI_INTERFACES não é mais necessária aqui, mas mantemos caso queira usar no futuro
from components.ai_interfaces import AI_INTERFACES 
from config import AI_LINKS

# Configuração da página (mantida como original)
st.set_page_config(
    page_title="Nexus - Ecossistema de IAs",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado (mantido como original)
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
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
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
    
    .connection-lines {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
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
    
    .link-item a:hover {
        text-decoration: underline;
    }
    
    .link-item .icon {
        margin-right: 0.75rem;
        color: #00d4ff;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)


# Função para criar partículas flutuantes (mantida como original)
def create_particles():
    particles_html = """
    <div class="floating-particles">
    """
    for i in range(20):
        delay = i * 0.3
        left = (i * 5) % 100
        particles_html += f"""
        <div class="particle" style="left: {left}%; animation-delay: {delay}s;"></div>
        """
    particles_html += "</div>"
    st.markdown(particles_html, unsafe_allow_html=True)

# ===== ALTERAÇÃO 2: DADOS DAS IAS ATUALIZADOS COM AS 9 NOVAS FERRAMENTAS =====
AI_TOOLS = {
    "text_generator": {
        "icon": "✍️",
        "title": "Gerador de Texto",
        "description": "IA avançada para criação de conteúdo, artigos, e-mails e textos criativos com qualidade profissional.",
        "status": "Online",
        "category": "Criação"
    },
    "image_creator": {
        "icon": "🎨",
        "title": "Criador de Imagens",
        "description": "Gere imagens incríveis a partir de descrições textuais usando modelos de IA de última geração.",
        "status": "Online",
        "category": "Visual"
    },
    "code_assistant": {
        "icon": "💻",
        "title": "Assistente de Código",
        "description": "Auxílio inteligente para programação, debugging e otimização de código em múltiplas linguagens.",
        "status": "Online",
        "category": "Desenvolvimento"
    },
    "data_analyst": {
        "icon": "📊",
        "title": "Analista de Dados",
        "description": "Análise avançada de dados, criação de gráficos e insights automatizados para tomada de decisão.",
        "status": "Online",
        "category": "Análise"
    },
    "translator": {
        "icon": "🌍",
        "title": "Tradutor Universal",
        "description": "Tradução precisa e contextual entre mais de 100 idiomas com preservação de nuances.",
        "status": "Online",
        "category": "Comunicação"
    },
    "voice_synthesis": {
        "icon": "🎤",
        "title": "Síntese de Voz",
        "description": "Converta texto em áudio natural com vozes realistas e controle de entonação.",
        "status": "Online",
        "category": "Áudio"
    },
    "document_processor": {
        "icon": "📄",
        "title": "Processador de Documentos",
        "description": "Extraia, analise e processe informações de documentos PDF, Word e outros formatos.",
        "status": "Online",
        "category": "Produtividade"
    },
    "chatbot_builder": {
        "icon": "🤖",
        "title": "Construtor de Chatbots",
        "description": "Crie chatbots inteligentes personalizados para atendimento e automação de processos.",
        "status": "Online",
        "category": "Automação"
    },
    "video_editor": {
        "icon": "🎬",
        "title": "Editor de Vídeo IA",
        "description": "Edição automática de vídeos com cortes inteligentes, legendas e efeitos visuais.",
        "status": "Online",
        "category": "Visual"
    },
    # --- NOVAS FERRAMENTAS ADICIONADAS AQUI ---
    "omnihuman_1": {
        "icon": "👤",
        "title": "OMNIHUMAN-1",
        "description": "Criação de avatares e humanos digitais hiper-realistas para diversas aplicações.",
        "status": "Online",
        "category": "Visual"
    },
    "manus_ai": {
        "icon": "✍️",
        "title": "MANUS AI",
        "description": "Modelo de linguagem avançado para geração de texto complexo e criativo.",
        "status": "Online",
        "category": "Criação"
    },
    "qwen_3": {
        "icon": "🧠",
        "title": "QWEN 3",
        "description": "IA de conversação poderosa para responder perguntas, criar conteúdo e mais.",
        "status": "Online",
        "category": "Criação"
    },
    "kling_ai": {
        "icon": "🎥",
        "title": "KLING AI 2.1",
        "description": "Geração de vídeo de alta fidelidade a partir de prompts de texto.",
        "status": "Online",
        "category": "Visual"
    },
    "baidu_ernie": {
        "icon": "📖",
        "title": "BAIDU ERNIE 4.5",
        "description": "Modelo de fundação da Baidu para compreensão e geração de linguagem natural.",
        "status": "Online",
        "category": "Criação"
    },
    "zai_glm": {
        "icon": "💡",
        "title": "Z.AI GLM-4.5",
        "description": "Modelo de linguagem geral para tarefas de raciocínio e criação de conteúdo.",
        "status": "Online",
        "category": "Criação"
    },
    "deepseek_v3": {
        "icon": "🚀",
        "title": "DEEPSEEK V3.1",
        "description": "IA especializada em geração de código e conversação técnica com alta performance.",
        "status": "Online",
        "category": "Desenvolvimento"
    },
    "seedream_4": {
        "icon": "🏞️",
        "title": "SEEDREAM 4.0",
        "description": "Geração de imagens de alta qualidade com grande realismo e detalhe a partir de texto.",
        "status": "Online",
        "category": "Visual"
    }
}

# ===== ALTERAÇÃO 1: NOVA ESTRUTURA DE PÁGINAS =====

def render_ai_link_page(ai_key):
    """
    Renderiza a "página" que contém apenas as informações e os links 
    da IA selecionada.
    """
    ai_tool = AI_TOOLS[ai_key]
    
    # Header da IA selecionada
    st.markdown(f"""
    <div style="background: linear-gradient(45deg, #00d4ff, #00ff88); 
                padding: 1px; border-radius: 15px; margin: 2rem 0;">
        <div style="background: #1e1e3f; padding: 2rem; border-radius: 14px;">
            <h2 style="color: white; text-align: center; font-family: 'Orbitron', monospace;">
                {ai_tool['icon']} {ai_tool['title']}
            </h2>
            <p style="color: #a0a0a0; text-align: center; font-family: 'Rajdhani', sans-serif;">
                {ai_tool['description']}
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Exibe os links relacionados, que é o foco desta página
    if ai_key in AI_LINKS and AI_LINKS[ai_key]:
        st.markdown("""
        <div class="links-container">
            <h4>Ferramentas e Links de Acesso</h4>
        """, unsafe_allow_html=True)
        for link_item in AI_LINKS[ai_key]:
            st.markdown(f"""
            <div class="link-item">
                <span class="icon">🔗</span>
                <a href="{link_item['url']}" target="_blank">{link_item['name']}</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning(f"Nenhuma ferramenta ou link relacionado foi encontrado para {ai_tool['title']}.")

    # Botão para voltar ao ecossistema
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔙 Voltar ao Ecossistema"):
        # Limpa o estado para causar a navegação de volta para a página principal
        del st.session_state.selected_ai
        st.rerun()

def render_main_page():
    """
    Renderiza a página principal do ecossistema com a grade de IAs.
    """
    # Header principal
    st.markdown('<h1 class="main-header">NEXUS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Ecossistema Inteligente de IAs para Produtividade</p>', unsafe_allow_html=True)
    
    # Estatísticas do ecossistema
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    cols = st.columns(4)
    
    # ===== ALTERAÇÃO 3: CONTADOR DE IAS ATUALIZADO PARA 18 =====
    stats = [("18", "IAs Ativas"), ("24/7", "Disponibilidade"), ("∞", "Possibilidades"), ("100%", "Segurança")]
    
    for i, (number, label) in enumerate(stats):
        with cols[i]:
            st.markdown(f"""
            <div class="stat-item">
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Função de callback para ser usada pelos botões
    def select_ai(ai_key):
        st.session_state.selected_ai = ai_key

    # Container e grade de IAs
    st.markdown('<div class="ecosystem-container">', unsafe_allow_html=True)
    # Garante que haja colunas suficientes para todos os cards
    num_items = len(AI_TOOLS)
    cols = st.columns(3)
    
    # Itera sobre a lista de chaves para garantir a ordem
    ai_keys = list(AI_TOOLS.keys())

    for idx, key in enumerate(ai_keys):
        ai_tool = AI_TOOLS[key]
        with cols[idx % 3]:
            # O card HTML é agora apenas visual. A ação é feita pelo botão do Streamlit.
            st.markdown(f"""
            <div class="ai-card">
                <div class="ai-icon">{ai_tool['icon']}</div>
                <div class="ai-title">{ai_tool['title']}</div>
                <div class="ai-description">{ai_tool['description']}</div>
                <div class="ai-status">
                    <div class="status-dot"></div>
                    {ai_tool['status']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Botão para acessar a "página" da IA
            st.button(
                f"Acessar Ferramentas de {ai_tool['title']}", 
                key=f"btn_{key}",
                on_click=select_ai,
                args=(key,)
            )
            st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


# --- FUNÇÃO PRINCIPAL QUE ATUA COMO ROTEADOR ---

def main():
    """
    Função principal que controla qual página é exibida com base no estado da sessão.
    """
    load_css()
    create_particles()
    
    # Roteador: Verifica se uma IA foi selecionada no estado da sessão
    if 'selected_ai' in st.session_state:
        # Se sim, renderiza a página de links da IA
        render_ai_link_page(st.session_state.selected_ai)
    else:
        # Se não, renderiza a página principal do ecossistema
        render_main_page()

if __name__ == "__main__":
    main()
