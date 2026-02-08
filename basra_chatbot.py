import re
import requests
import json

class Basra_Chatbot:
    def __init__(self):
        self.name = "Basra ChatBot"
        print("\n*** shukar ALLAH ***")

    def get_ai_response_groq(self, user_input):

        try:
            api_key = "put your API key"
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "system",
                     "content": "GOOD JOB"},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }

            response = requests.post(url, headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                print("..!")
                result = response.json()
                return result['choices'][0]['message']['content']
        except Exception as e:
            print("  Error: {e}")

        return self.get_simple_ai_response(user_input)


    def get_question(self):
        user_input = input("Sir!: ").strip()
        return user_input

    def chat(self):
        print(f"Welcome to {self.name}!")
        greeting = "Basra Welcome's You! If u need help.\n Goodbye! if u exit"
        print(greeting)
        while True:
            try:
                user_input = self.get_question()
                if not user_input:
                    continue
                if re.search(r'\b(goodbye|good bye|Good Bye|bye bye|Goodbye|Bye Bye|exit|quit)\b', user_input.lower()):
                    print("Bye Bye....Nice to meet you!")
                    break
                print("......!")
                response = self.get_ai_response_groq(user_input)
                print(f" Basra_ChatBot: {response}\n")
            except KeyboardInterrupt:
                print("ALLAH hafiz!")
                break
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    chatbot = Basra_Chatbot()
    chatbot.chat()