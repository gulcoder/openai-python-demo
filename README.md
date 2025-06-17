# 🚀 OpenAI Python Demo

Ett enkelt och roligt Python-projekt för att **interagera med OpenAI:s API** (GPT-3.5 och GPT-4) direkt i terminalen! 🧠💬  
Perfekt för dig som vill lära dig hur AI-svar påverkas av olika parametrar som modell, temperatur och rollinstruktioner.

---

## ✨ Funktioner

- 🤖 Ställ frågor direkt till GPT-modeller från terminalen
- 🔄 Byt modell mellan `gpt-3.5-turbo` och `gpt-4`
- 🎛️ Justera svarens variation med `temperature`
- 🎭 Ange systemroller (t.ex. "poet", "coach", "komiker") för att styra stil
- 🔒 Skydda din API-nyckel med `.env` (ingår i `.gitignore`)

---

## ⚙️ Installation

### 1. Klona projektet
```bash
git clone https://github.com/gulcoder/openai-python-demo.git
cd openai-python-demo
```

### 2. Skapa och aktivera virtuell miljö i VS Code

```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Installera beroenden

```bash
pip install -r requirements.txt
```

### 4. Skapa .env fil med din API-nyckel
```bash
OPENAI_API_KEY=din-api-nyckel-här
```

### 5. Kör programmet
```bash
python3 main.py
```
