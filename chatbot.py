import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Cargar variables de entorno desde .env
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT")
)

print("🤖 Chatbot Azure OpenAI iniciado. Escribe 'salir' para terminar. \n")

while True:
    user_input = input("👤 Tú: ")

    if user_input.lower() == 'salir':
        print("Chat finalizado.")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente académico claro y conciso. "
                    "Responde de forma breve y ordenada. "
                    "No excedas 5 líneas por respuesta. "
                    "Evita explicaciones largas."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.8,
        max_tokens=200,
        top_p=0.9
    )

    print("🤖 Bot:", response.choices[0].message.content, "\n")