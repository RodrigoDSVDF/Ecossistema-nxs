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

# Configurações de links para cada IA (LISTA ATUALIZADA)
AI_LINKS = {
    "text_generator": [
        {"name": "ChatGPT", "url": "https://chat.openai.com/"},
        {"name": "Google Gemini", "url": "https://gemini.google.com/"},
        {"name": "Perplexity AI", "url": "https://www.perplexity.ai/"}, # NOVO
        {"name": "Claude", "url": "https://claude.ai/"}, # NOVO
        {"name": "Copy.ai", "url": "https://www.copy.ai/"}
    ],
    "image_creator": [
        {"name": "Midjourney", "url": "https://www.midjourney.com/"},
        {"name": "DALL-E 3", "url": "https://openai.com/dall-e-3"},
        {"name": "Leonardo.Ai", "url": "https://leonardo.ai/"}, # NOVO
        {"name": "Adobe Firefly", "url": "https://www.adobe.com/br/products/firefly.html"}, # NOVO
        {"name": "Stable Diffusion", "url": "https://stability.ai/stable-diffusion"}
    ],
    "code_assistant": [
        {"name": "GitHub Copilot", "url": "https://github.com/features/copilot"},
        {"name": "Codeium", "url": "https://www.codeium.com/"},
        {"name": "Amazon CodeWhisperer", "url": "https://aws.amazon.com/codewhisperer/"}, # NOVO
        {"name": "Tabnine", "url": "https://www.tabnine.com/"}
    ],
    "data_analyst": [
        {"name": "Tableau", "url": "https://www.tableau.com/"},
        {"name": "Power BI", "url": "https://powerbi.microsoft.com/"},
        {"name": "Google Looker Studio", "url": "https://lookerstudio.google.com/"}
    ],
    "translator": [
        {"name": "Google Translate", "url": "https://translate.google.com/"},
        {"name": "DeepL Translator", "url": "https://www.deepl.com/translator"},
        {"name": "Microsoft Translator", "url": "https://www.bing.com/translator"} # NOVO
    ],
    "voice_synthesis": [
        {"name": "ElevenLabs", "url": "https://elevenlabs.io/"},
        {"name": "PlayHT", "url": "https://play.ht/"}, # NOVO
        {"name": "Google Text-to-Speech", "url": "https://cloud.google.com/text-to-speech"}
    ],
    "document_processor": [
        {"name": "NotebookLM", "url": "https://notebooklm.google.com/"}, # NOVO
        {"name": "ChatPDF", "url": "https://www.chatpdf.com/"}, # NOVO
        {"name": "Adobe Acrobat AI", "url": "https://www.adobe.com/acrobat/acrobat-ai-assistant.html"},
        {"name": "DocuSign", "url": "https://www.docusign.com/"}
    ],
    "chatbot_builder": [
        {"name": "ManyChat", "url": "https://manychat.com/"},
        {"name": "Google Dialogflow", "url": "https://cloud.google.com/dialogflow"}, # NOVO
        {"name": "Chatfuel", "url": "https://chatfuel.com/"}
    ],
    "video_editor": [
        {"name": "RunwayML", "url": "https://runwayml.com/"},
        {"name": "Pika", "url": "https://pika.art/"}, # NOVO
        {"name": "Synthesia", "url": "https://www.synthesia.io/"}, # NOVO
        {"name": "Descript", "url": "https://www.descript.com/"}
    ]
}
