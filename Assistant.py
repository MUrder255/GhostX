import openai

class Assistant:
    def __init__(self, api_key: str):
        """
        Initialize the AI Assistant with the OpenAI API key.
        """
        self.api_key = api_key
        openai.api_key = api_key

    def get_response(self, prompt: str) -> str:
        """
        Get a response from the AI assistant based on the provided prompt.
        
        :param prompt: The user input or query.
        :return: AI-generated response as a string.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}"


# Example Usage
if __name__ == "__main__":
    api_key = "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"  # Replace with your actual API key
    assistant = Assistant(api_key)
    user_input = input("Ask me anything: ")
    print("Assistant:", assistant.get_response(user_input))
