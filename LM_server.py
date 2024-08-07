from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

history = [
    {"role": "system", "content": "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability."},
]

print("AI Assistant initialized. Type your messages and press Enter. Type 'quit' to exit.")

while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        break

    history.append({"role": "user", "content": user_input})

    try:
        completion = client.chat.completions.create(
            model="Orenguteng/Llama-3.1-8B-Lexi-Uncensored-GGUF",
            messages=history,
            temperature=0.7,
            stream=True,
        )

        response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                response += content

        print()  # New line after response
        history.append({"role": "assistant", "content": response})

    except Exception as e:
        print(f"An error occurred: {e}")
        break