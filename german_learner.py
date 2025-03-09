import requests, os
from getpass import getpass

def correct_german(api_key, text):
    """Get German corrections from OpenAI API."""
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful German language tutor. Correct grammar errors and explain them clearly."},
                {"role": "user", "content": f"Correct this German text and explain mistakes: '{text}'. Format as: Corrected: [text] | Explanation: [details]"}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"] if response.status_code == 200 else f"Error: {response.status_code}"

def main():
    print("=== German Language Learning Assistant ===")
    api_key = os.environ.get("OPENAI_API_KEY") or getpass("Enter your OpenAI API key: ")
    
    print("\nType your German text for correction (or 'exit' to quit)")
    while True:
        user_input = input("\n[German] > ")
        if user_input.lower() == "exit": break
        if user_input.strip():
            print("\nAnalyzing...")
            print(correct_german(api_key, user_input))

if __name__ == "__main__":
    main()
