# Azure Chatbot 🤖

Un chatbot interactivo basado en Azure OpenAI que funciona como asistente académico. El bot proporciona respuestas breves y concisas para ayudarte con tus consultas.

## Características ✨

- Integración con Azure OpenAI API
- Modelo GPT-4o-mini para respuestas inteligentes
- Interfaz de línea de comandos interactiva
- Respuestas académicas optimizadas (máx. 5 líneas)
- Fácil de usar: escribe `salir` para terminar

## Requisitos previos

- Python 3.8 o superior
- Cuenta de Azure con servicio OpenAI configurado
- Variables de configuración de Azure OpenAI

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/azure-chatbot.git
cd azure-chatbot
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:
   - **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   - **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Configuración

Necesitas configurar tus credenciales de Azure OpenAI. En el archivo `chatbot.py`, reemplaza:

- `api_key`: Tu clave API de Azure OpenAI
- `azure_endpoint`: Tu endpoint de Azure

**⚠️ Importante:** Nunca subas tus credenciales reales a GitHub. Considera usar variables de entorno.

### Opción recomendada: Usar variables de entorno

1. Crea un archivo `.env` (no se subirá a GitHub):
```
AZURE_API_KEY=tu_clave_aqui
AZURE_ENDPOINT=tu_endpoint_aqui
```

2. Instala `python-dotenv`:
```bash
pip install python-dotenv
```

## Uso

Ejecuta el chatbot:
```bash
python chatbot.py
```

Luego interactúa con el bot escribiendo tus preguntas. Escribe `salir` para salir.

## Ejemplo de conversación

```
🤖 Chatbot Azure OpenAI iniciado. Escribe 'salir' para terminar.

👤 Tú: ¿Cuál es la capital de Francia?
🤖 Bot: La capital de Francia es París. Es conocida como "La Ciudad de la Luz" y es el centro político, económico y cultural del país.

👤 Tú: salir
Chat finalizado.
```

## Licencia

Este proyecto está bajo la licencia MIT. Ver archivo `LICENSE` para más detalles.

## Autor

Creado como proyecto académico para UNIR.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o crea un pull request.
