import os
from dotenv import load_dotenv
from openai import OpenAI

# Ladda miljövariabler från .env-filen
load_dotenv()

# Skapa OpenAI-klienten med nyckeln från .env
client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

def ask_openai(prompt: str, model="gpt-3.5-turbo", max_tokens=500) -> list[str]:
    """Skickar en prompt till OpenAI:s API och får tillbaka ett svar."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            n=1,
            max_tokens=max_tokens
        )
        return [choice.message.content.strip() for choice in response.choices]

    except Exception as e:
        return [f"Ett fel uppstod: {e}"]

if __name__ == "__main__":
    # Välj modell via användarinmatning
    model = input("Vilken modell vill du använda? (gpt-3.5-turbo / gpt-4): ").strip()

    # Validera modellvalet
    if model not in ["gpt-3.5-turbo", "gpt-4"]:
        print("Ogiltigt modellnamn. Standard: gpt-3.5-turbo används.")
        model = "gpt-3.5-turbo"

    # Prompt från användaren
    prompt = input("Skriv din prompt till OpenAI: ")

    # Skicka prompten
    svar = ask_openai(prompt, model=model)

    # Skriv ut svaret
    for i, val in enumerate(svar, start=1):
        print(f"\nSvar {i} ({model}):\n{val}")
