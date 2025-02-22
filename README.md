# ElevenLabs_Worldwide_Hackathon
# Parent AI App with ElevenLabs TTS

This is a **Python** application that:
1. **Collects family details** from a parent.  
2. **Uses OpenAI’s GPT-based ChatCompletion API** to answer questions in a personalized way.  
3. **Generates voice output** via the **ElevenLabs** Text-to-Speech API.

## Table of Contents
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [How It Works](#how-it-works)  
- [Customization](#customization)  
- [License](#license)

---

## Features

- **Family Info Collection**  
  - Prompts the parent for basic family information (e.g., number of children, names, favorite activities).
  
- **Personalized Answers**  
  - Leverages the collected family data to tailor AI responses to children’s questions.

- **Natural Voice Output**  
  - Uses [ElevenLabs](https://beta.elevenlabs.io/) TTS for high-quality voice synthesis.

---

## Requirements

1. **Python 3.7+**  
2. **OpenAI Account & API Key**  
   - [Sign up](https://platform.openai.com/signup) if you don’t have an account.  
   - [Create an API key](https://platform.openai.com/account/api-keys).
3. **ElevenLabs Account & API Key**  
   - [Sign up](https://beta.elevenlabs.io/) and obtain an API key.

---

## Installation

1. **Clone the Repository (Optional)**  
   ```bash
   git clone https://github.com/your-username/parent-ai-elevenlabs.git
   cd parent-ai-elevenlabs
   ```

2. **Install Python Dependencies**  
   ```bash
   pip install openai elevenlabs
   ```

3. **Configure API Keys**  
   - In the `parent_ai_elevenlabs.py` file, replace:
     ```python
     openai.api_key = "YOUR_OPENAI_API_KEY"
     set_api_key("YOUR_ELEVENLABS_API_KEY")
     ```
     with your actual credentials.

---

## Usage

1. **Run the Application**  
   ```bash
   python parent_ai_elevenlabs.py
   ```
2. **Enter Family Details**  
   - You will be prompted for:
     - Family name  
     - Number of children  
     - Children’s names  
     - Favorite family activities  
     - Important family values  

3. **Ask Questions**  
   - After setup, you’ll enter **Kid’s Q&A mode**.  
   - Type a question and press **Enter**.  
   - The AI will respond in text and speak the answer using ElevenLabs.  
   - Type **exit** or **quit** to end the session.

---

## Configuration

- **Voice Selection**  
  - The function `speak_text(text, voice_name="Rachel", model="eleven_monolingual_v1")` lets you specify the **voice_name**.  
  - You can choose from [ElevenLabs’ supported voices](https://beta.elevenlabs.io/) or your own custom voices.  

- **ElevenLabs Model**  
  - The default model is `"eleven_monolingual_v1"`.  
  - To support multiple languages, you can switch to `"eleven_multilingual_v1"` if needed.

- **OpenAI Model**  
  - The script uses `"gpt-3.5-turbo"` by default.  
  - If you have access to GPT-4, you can change it in the `response = openai.ChatCompletion.create(...)` call.

- **Temperature & Max Tokens**  
  - You can tweak `temperature` (creativity) and `max_tokens` (response length) in the `openai.ChatCompletion.create` function to suit your needs.

---

## How It Works

1. **Collect Family Info**  
   - The parent is asked a series of questions.  
   - This data is stored in a Python dictionary.

2. **Create a Context Prompt**  
   - A system prompt is generated with the family details.  
   - This guides the AI to answer questions with the right context.

3. **Q&A Loop**  
   - The child’s question and the system context are sent to OpenAI’s ChatCompletion endpoint.  
   - The response text is printed to the console and then passed to ElevenLabs for TTS.

4. **Voice Synthesis**  
   - ElevenLabs generates an audio stream from the AI’s text response, which is played locally.

---

## Customization

- **Conversation History**  
  - To maintain context over multiple questions, you can store previous messages in the `messages` list and send them all at once to OpenAI.

- **Data Persistence**  
  - Instead of collecting family info every run, you could store it in a local file (JSON, CSV, etc.) or a database and load it on startup.

- **User Interface**  
  - Replace the console interface with a web or GUI front end to capture user inputs and play audio.  

- **Security & Privacy**  
  - Be mindful of sending sensitive family information to OpenAI. Review [OpenAI’s data usage policy](https://openai.com/policies) for details.

---

## License

You are free to use, modify, and distribute this code for your own projects. Please check the licenses for the libraries used (e.g., OpenAI, ElevenLabs) to ensure compliance with their terms.  

---

### Enjoy building your **Parent AI** that speaks with **ElevenLabs** voices!