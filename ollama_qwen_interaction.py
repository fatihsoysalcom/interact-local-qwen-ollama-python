import ollama

# This example demonstrates how to interact with a locally running Qwen model via Ollama.
# It assumes the Ollama server is running and the specified Qwen model has been pulled.

# --- Configuration ---
OLLAMA_MODEL = "qwen:7b" # Specify the Qwen model tag you have pulled (e.g., qwen:7b, qwen:14b)
PROMPT = "Bana Türkiye'nin başkenti hakkında kısa bir bilgi verir misin?" # A simple prompt in Turkish

def main():
    print(f"Connecting to Ollama and using model: {OLLAMA_MODEL}")
    print(f"Sending prompt: '{PROMPT}'")

    try:
        # Use the ollama client to send a request to the local Ollama server.
        # The 'chat' method is suitable for conversational interactions.
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {'role': 'user', 'content': PROMPT}, # The user's message to the LLM
            ],
            stream=False # Set to True for streaming responses, False for a single response
        )

        # Extract and print the content from the model's response.
        if response and 'message' in response and 'content' in response['message']:
            print("\n--- Model Response ---")
            print(response['message']['content'])
        else:
            print("Error: No valid response received from Ollama.")

    except ollama.ResponseError as e:
        print(f"Error communicating with Ollama: {e}")
        print("Please ensure the Ollama server is running and the model is available.")
        print("You might need to run: 'ollama serve' in a terminal and 'ollama pull qwen:7b'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
