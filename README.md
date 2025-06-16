# 🚀 OpenAI Python Demo

Ett enkelt och roligt Python-projekt för att **interagera med OpenAI:s API** (GPT-3.5 och GPT-4) direkt i terminalen! 🧠💬

---

## ✨ Funktioner

- 🤖 Ställ frågor och få svar från OpenAI
- 🔄 Byt modell mellan `gpt-3.5-turbo` och `gpt-4`
- 🎛️ Justera svarens variation med `temperature`
- 🔒 Skydda din API-nyckel med `.env`

---

## ⚙️ Installation

1. Klona repot:
```bash
git clone https://github.com/gulcoder/openai-python-demo.git
```


2. Skapa och aktivera en virtuell miljö:
 ```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Installera beroenden:
```bash
pip install -r requirements.txt
```

4. Skapa .env fil i projektets rot med din API-nyckel.
   ```bash
   OPEN_AI_API_KEY=din-api-nyckel-här
```

5. Kör programmet:
```bash
python3 main.py
```
