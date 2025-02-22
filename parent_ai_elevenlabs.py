import openai
from elevenlabs import generate, play, set_api_key

# 1. Configure your API keys
openai.api_key = "YOUR_OPENAI_API_KEY"
set_api_key("YOUR_ELEVENLABS_API_KEY")

def collect_family_info():
    """
    Step 1: Interactively ask the parent about the family and store the data.
    """
    family_info = {}
    
    print("Welcome to the Parent AI setup!")
    family_info['family_name'] = input("What is your family's last name? ")
    family_info['num_children'] = input("How many children do you have? ")
    family_info['children_names'] = input("What are your children's names (comma separated)? ")
    family_info['favorite_activities'] = input("What are some favorite family activities (comma separated)? ")
    family_info['important_values'] = input("What are some important values in your family (comma separated)? ")
    
    return family_info


def create_context_from_family_info(family_info):
    """
    Step 2: Turn the collected info into a context string.
    """
    context = (
        f"Family Name: {family_info['family_name']}\n"
        f"Number of Children: {family_info['num_children']}\n"
        f"Children Names: {family_info['children_names']}\n"
        f"Favorite Activities: {family_info['favorite_activities']}\n"
        f"Important Values: {family_info['important_values']}\n"
        "\n"
        "Use this family context to answer questions like a helpful, friendly family AI assistant.\n"
        "Try to give answers that reflect the family's unique details where relevant.\n"
    )
    return context


def speak_text(text, voice_name="Rachel", model="eleven_monolingual_v1"):
    """
    Uses ElevenLabs API to generate speech and play it locally.
    - You can change the 'voice_name' to any supported voice ID from your ElevenLabs dashboard.
    - 'model' can also be changed if needed.
    """
    audio = generate(
        text=text,
        voice=voice_name,
        model=model
    )
    play(audio)


def ask_kid_question(context):
    """
    Step 3: Continuously ask the user (kid) for their questions,
    get AI answers, and speak them aloud using ElevenLabs TTS.
    """
    print("\n--- Kid's Q&A mode (with ElevenLabs voice) ---")
    print("Ask your questions below. Type 'exit' or 'quit' to end.\n")
    
    while True:
        question = input("Kid: ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting Q&A mode.")
            break
        
        # Call OpenAI Chat Completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or your preferred model
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": question},
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        answer = response.choices[0].message["content"]
        
        # Print and speak the AI answer
        print(f"AI: {answer}\n")
        speak_text(answer)


def main():
    # 1. Collect family info
    family_info = collect_family_info()

    # 2. Create a context string from the info
    context = create_context_from_family_info(family_info)
    
    # 3. Start Q&A (with TTS)
    ask_kid_question(context)


if __name__ == "__main__":
    main()
