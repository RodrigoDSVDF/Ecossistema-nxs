# Configurações do Nexus Ecosystem

# Configurações da aplicação
APP_CONFIG = {
    "title": "Nexus - Ecossistema de IAs",
    "icon": "🌐",
    "layout": "wide",
    "sidebar_state": "collapsed"
}

# Configurações visuais
VISUAL_CONFIG = {
    "primary_colors": {
        "cyan": "#00d4ff",
        "emerald": "#00ff88",
        "orange": "#ff6b6b",
        "yellow": "#ffd93d"
    },
    "background_colors": {
        "dark_primary": "#0f0f23",
        "dark_secondary": "#1a1a2e",
        "dark_tertiary": "#16213e",
        "card_primary": "#1e1e3f",
        "card_secondary": "#2a2a5a"
    },
    "fonts": {
        "primary": "Orbitron",
        "secondary": "Rajdhani"
    },
    "animations": {
        "particle_count": 20,
        "animation_duration": "6s",
        "hover_scale": 1.02,
        "hover_lift": "-10px"
    }
}

# Configurações das estatísticas
STATS_CONFIG = {
    "active_ais": 9,
    "availability": "24/7",
    "possibilities": "∞",
    "security": "100%"
}

# Configurações das IAs
AI_CATEGORIES = {
    "Criação": ["text_generator"],
    "Visual": ["image_creator", "video_editor"],
    "Desenvolvimento": ["code_assistant"],
    "Análise": ["data_analyst"],
    "Comunicação": ["translator"],
    "Áudio": ["voice_synthesis"],
    "Produtividade": ["document_processor"],
    "Automação": ["chatbot_builder"]
}

# Configurações de interface
INTERFACE_CONFIG = {
    "grid_columns": 3,
    "card_min_width": "300px",
    "card_gap": "2rem",
    "max_container_width": "1400px"
}

# Configurações de desenvolvimento
DEV_CONFIG = {
    "debug_mode": False,
    "show_performance_metrics": False,
    "enable_logging": True,
    "simulation_delay": 2  # segundos para simular processamento
}




# Configurações de links para cada IA
# config.py

# ... (outras configurações como APP_CONFIG, VISUAL_CONFIG, etc. permanecem as mesmas) ...

# Configurações das IAs (ATUALIZADO)
AI_CATEGORIES = {
    "Criação": ["text_generator", "manus_ai", "qwen_3", "baidu_ernie", "zai_glm"],
    "Visual": ["image_creator", "video_editor", "omnihuman_1", "kling_ai", "seedream_4"],
    "Desenvolvimento": ["code_assistant", "deepseek_v3"],
    "Análise": ["data_analyst"],
    "Comunicação": ["translator"],
    "Áudio": ["voice_synthesis"],
    "Produtividade": ["document_processor"],
    "Automação": ["chatbot_builder"]
}

# ... (INTERFACE_CONFIG e DEV_CONFIG permanecem as mesmas) ...

# Configurações de links para cada IA (ATUALIZADO)
AI_LINKS = {
    "text_generator": [
        {"name": "ChatGPT", "url": "https://chat.openai.com/"},
        {"name": "Google Gemini", "url": "https://gemini.google.com/"},
        {"name": "Copy.ai", "url": "https://www.copy.ai/"}
    ],
    "image_creator": [
        {"name": "Midjourney", "url": "https://www.midjourney.com/"},
        {"name": "DALL-E 3", "url": "https://openai.com/dall-e-3"},
        {"name": "Stable Diffusion", "url": "https://stability.ai/stable-diffusion"}
    ],
    "code_assistant": [
        {"name": "GitHub Copilot", "url": "https://github.com/features/copilot"},
        {"name": "Codeium", "url": "https://www.codeium.com/"},
        {"name": "Tabnine", "url": "https://www.tabnine.com/"}
    ],
    "data_analyst": [
        {"name": "Tableau", "url": "https://www.tableau.com/"},
        {"name": "Power BI", "url": "https://powerbi.microsoft.com/"},
        {"name": "Google Data Studio", "url": "https://lookerstudio.google.com/"}
    ],
    "translator": [
        {"name": "Google Translate", "url": "https://translate.google.com/"},
        {"name": "DeepL Translator", "url": "https://www.deepl.com/translator"}
    ],
    "voice_synthesis": [
        {"name": "ElevenLabs", "url": "https://elevenlabs.io/"},
        {"name": "Google Text-to-Speech", "url": "https://cloud.google.com/text-to-speech"}
    ],
    "document_processor": [
        {"name": "Adobe Acrobat AI", "url": "https://www.adobe.com/acrobat/acrobat-ai-assistant.html"},
        {"name": "DocuSign", "url": "https://www.docusign.com/"}
    ],
    "chatbot_builder": [
        {"name": "ManyChat", "url": "https://manychat.com/"},
        {"name": "Chatfuel", "url": "https://chatfuel.com/"}
    ],
    "video_editor": [
        {"name": "RunwayML", "url": "https://runwayml.com/"},
        {"name": "Descript", "url": "https://www.descript.com/"}
    ],
    # --- NOVAS FERRAMENTAS ADICIONADAS AQUI ---
    "omnihuman_1": [
        {"name": "Acessar OMNIHUMAN-1", "url": "https://omnihuman-1.com"}
    ],
    "manus_ai": [
        {"name": "Acessar MANUS AI", "url": "https://manus.im"}
    ],
    "qwen_3": [
        {"name": "Acessar QWEN 3", "url": "https://chat.qwen.ai"}
    ],
    "kling_ai": [
        {"name": "Acessar KLING AI 2.1", "url": "https://klingai.com"}
    ],
    "baidu_ernie": [
        {"name": "Acessar BAIDU ERNIE 4.5", "url": "https://huggingface.co/baidu/ERNIE-4.5-0.3B-PT"}
    ],
    "zai_glm": [
        {"name": "Acessar Z.AI GLM-4.5", "url": "https://z.ai"}
    ],
    "deepseek_v3": [
        {"name": "Acessar DEEPSEEK V3.1", "url": "https://chat.deepseek.com"}
    ],
    "seedream_4": [
        {"name": "Acessar SEEDREAM 4.0", "url": "https://seed.bytedance.com/en/seedream4_0"}
    ]
}
