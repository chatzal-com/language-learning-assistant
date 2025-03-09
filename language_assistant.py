import requests
import json
import os
from getpass import getpass

def call_api(api_key, user_text, language, api_provider="openai"):
    """Call the API to correct grammar and provide feedback."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    prompt = f"""I am learning {language}. Please correct the grammar in this text and explain any mistakes:
    
Text: {user_text}

Please format your response like this:
Corrected: [corrected text]
Explanation: [explanation of mistakes]"""

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": f"You are a helpful {language} language tutor."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }
    
    # Select the appropriate API endpoint
    if api_provider.lower() == "chatzal":
        api_url = "https://api.chatzal.com/v1/chat/completions"
    else:  # Default to OpenAI
        api_url = "https://api.openai.com/v1/chat/completions"
    
    response = requests.post(
        api_url,
        headers=headers,
        data=json.dumps(payload)
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

def main():
    print("=" * 50)
    print("Welcome to the Language Learning Assistant!")
    print("=" * 50)
    print("\nThis program will help you learn a new language by correcting your grammar.")
    
    # Select API provider
    print("\nSelect API provider:")
    print("1. OpenAI (default)")
    print("2. Chatzal (for users in Iran)")
    
    api_provider = "openai"  # Default
    try:
        provider_choice = int(input("\nSelect provider (number): "))
        if provider_choice == 2:
            api_provider = "chatzal"
    except ValueError:
        print("Invalid input. Defaulting to OpenAI.")
    
    print(f"\nUsing {api_provider.upper()} API.")
    
    # Get the language the user wants to learn
    languages = ["Spanish", "French", "German", "Italian", "Portuguese", "Russian", "Japanese", "Chinese", "Korean"]
    print("\nAvailable languages:")
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")
    print(f"{len(languages) + 1}. Other (specify)")
    
    while True:
        try:
            choice = int(input("\nSelect a language (number): "))
            if 1 <= choice <= len(languages):
                language = languages[choice - 1]
                break
            elif choice == len(languages) + 1:
                language = input("Enter the language you want to learn: ")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get the API key
    api_key = os.environ.get("OPENAI_API_KEY") if api_provider == "openai" else os.environ.get("CHATZAL_API_KEY")
    if not api_key:
        print(f"\nPlease provide your {api_provider.upper()} API key.")
        api_key = getpass("API Key (input will be hidden): ")
    
    print(f"\nGreat! You're now learning {language}.")
    print(f"Type your text in {language}, and I'll correct it for you.")
    print("Type 'exit' to quit.")
    
    while True:
        user_text = input(f"\n[{language}] > ")
        
        if user_text.lower() == 'exit':
            print("\nThank you for using the Language Learning Assistant. Goodbye!")
            break
        
        if not user_text.strip():
            print("Please enter some text to correct.")
            continue
        
        print("\nAnalyzing your text...")
        response = call_api(api_key, user_text, language, api_provider)
        print("\n" + response)

if __name__ == "__main__":
    main()
