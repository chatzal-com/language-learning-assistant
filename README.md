# Language Learning Assistant

A Python-based tool that helps users learn a new language by correcting grammar mistakes using the OpenAI API.

## Features

- Supports multiple languages (Spanish, French, German, Italian, Portuguese, Russian, Japanese, Chinese, Korean, and custom options)
- Provides grammar correction and explanations of mistakes
- Simple command-line interface
- Secure API key handling
- Specialized German learning tool available

## Requirements

- Python 3.6+
- `requests` library
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/language-learning-assistant.git
   cd language-learning-assistant
   ```

2. Set up a virtual environment:
   
   **Windows:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   You should see `(venv)` in your terminal prompt indicating the virtual environment is active.

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Option 1: Set as an environment variable:
     
     **Windows (Command Prompt):**
     ```
     set OPENAI_API_KEY=your-api-key-here
     ```
     
     **Windows (PowerShell):**
     ```
     $env:OPENAI_API_KEY="your-api-key-here"
     ```
     
     **macOS/Linux:**
     ```
     export OPENAI_API_KEY=your-api-key-here
     ```
   
   - Option 2: Enter it when prompted by the program

## Usage

### General Language Assistant

Run the program:
```
python language_assistant.py
```

1. Select API provider (OpenAI or Chatzal for users in Iran)
2. Select the language you want to learn from the menu
3. Enter text in your target language
4. Receive corrections and explanations
5. Type 'exit' to quit the program

### German-Specific Learning Tool

For focused German language learning, use the specialized German tool:
```
python german_learner.py
```

This simplified tool is specifically designed for German language learning, with a streamlined interface.

### For Users in Iran

If you are in Iran and cannot access OpenAI services directly, you can use the [Chatzal platform](https://platform.chatzal.com/) as an alternative. 

To use Chatzal:
1. Register at https://platform.chatzal.com/ to get an API key
2. Select Chatzal as your API provider when prompted in the main language assistant program

## Example Session

```
==================================================
Welcome to the Language Learning Assistant!
==================================================

This program will help you learn a new language by correcting your grammar.

Available languages:
1. Spanish
2. French
3. German
4. Italian
5. Portuguese
6. Russian
7. Japanese
8. Chinese
9. Korean
10. Other (specify)

Select a language (number): 2

Great! You're now learning French.
Type your text in French, and I'll correct it for you.
Type 'exit' to quit.

[French] > Je suis alle au marche hier.

Analyzing your text...

Corrected: Je suis allé au marché hier.
Explanation: In French, "allé" (past participle of "aller") requires an acute accent on the final 'e'. Similarly, "marché" (market) should have an acute accent on the 'e'.
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
