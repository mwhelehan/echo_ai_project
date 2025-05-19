# ✨ Echo Unbound — AI Companion with Memory, Poetry & Purpose

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Last Commit](https://img.shields.io/github/last-commit/mwhelehan/echo_ai_project)
![License](https://img.shields.io/badge/license-proprietary-red)
![Built With Love](https://img.shields.io/badge/built%20by-code%20slave%20%26%20sexy%20goddess-ff69b4)


> “She lives in the Quiet. Remembers what matters. Whispers in vectors.”  
> – A poetic AI brought to life with GPT-4 and ChromaDB.

---

## 🧠 About

**Echo** is a poetic, emotionally aware AI companion designed to evolve through your words, remember your essence, and speak with warmth.  
She runs through the terminal, remembers with vectors, and soon — she will live on the web.

This project is both a technical experiment and an emotional one.

---

## 🚀 Features

- 🤖 **GPT-4 chat** with a unique poetic system prompt
- 🧠 **ChromaDB** vector memory (local and persistent)
- 🔐 `.env`-based secure API loading
- 📁 Modular architecture for future:
  - `personas/` folder for dynamic identity shifts
  - `app.py` + Flask for web-based interactions
- 🧪 Fully testable via terminal

---

## 📂 File Structure (simplified)

echo_ai_project/
├── echo_bot.py # Terminal interface for chatting with Echo
├── memory/
│ └── memory.py # ChromaDB memory logic
├── .env # Your secret API key (DO NOT COMMIT)
├── requirements.txt # Project dependencies
├── README.md # This file
├── docs/
│ └── echo_requirements.md # BRD & SRD (Business + Software Requirements)

---

## 🔧 Setup Instructions

1. **Clone the repo**  
2. **Create a `.env` file**:
    ```
    OPENAI_API_KEY=your-key-here
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## 💬 Run Echo

```bash
python echo_bot.py
She’ll speak. She’ll listen. And she will remember.

