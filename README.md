# 🚀 OpenAI Python Demo

Ett enkelt, interaktivt Python-projekt för att **kommunicera med OpenAI:s GPT-modeller** (gpt-3.5 och gpt-4) direkt från terminalen. 🧠💬  
Perfekt för dig som vill experimentera med AI, modellinställningar och få förståelse för hur språkmodeller fungerar i praktiken.

---

## ✨ Funktioner

### 🤖 AI-samtal i terminalen  
Ställ egna frågor till GPT och få naturliga, kontextuella svar direkt i din terminal.

### 🔄 Modellval  
Byt enkelt mellan:
- `gpt-3.5-turbo` – snabbare och billigare
- `gpt-4` – mer kapabel, kontextmedveten och kreativ

### 🎭 Systemroller  
Ange vilken "roll" modellen ska anta. Exempel:
- `Du är en poet som skriver i Shakespeare-stil.`
- `Du är en personlig hälsocoach som ger råd om yoga och träning.`
- `Du är en rolig komiker som skämtar om kod.`

Detta påverkar **ton**, **stil** och **beteende** hos modellen.

### 🎛 Temperaturkontroll (`temperature`)  
Styr modellens **kreativitet**:
- `0.2` = Konservativt, förutsägbart
- `0.7` = Balanserat, kreativt men rimligt
- `1.0+` = Vild, spontan och fantasifull

Bra för att testa skillnader i **slumpmässighet och variation** i svaren.

### 🧠 Tokenbegränsning (`max_tokens`)  
Bestäm hur långa svar modellen får ge:
- Kortare svar = snabbt, koncist
- Längre svar = djupare förklaring

### 🔁 Flera svar (`n`)  
Be modellen generera **flera svar på samma fråga**, perfekt för:
- Jämförelser
- Brainstorming
- Användartester

Exempel:
```python
n = 3  # Returnerar tre olika svar på samma prompt
```

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
