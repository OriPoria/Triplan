import yaml
import json

from groq import Groq


SYS_INSTRUCTION_FILE = "system_instructions.json"
API_KEY_FILE = "api_key.yaml"

class GroqClient:

    def __init__(self):
        with open(API_KEY_FILE) as f:
            self.grok_api_key = yaml.safe_load(f)["grok_api_key"]
        self.client = Groq(api_key=self.grok_api_key)
        self.trained_file = SYS_INSTRUCTION_FILE

    def save_sys_instructions(self, messages):
        with open(self.trained_file, 'w') as f:
            json.dump(messages, f, indent=4)

    def load_sys_instructions(self):
        try:
            with open(self.trained_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def chat(self):
        system_mode = True

        # Load previous conversation if available
        messages = self.load_sys_instructions()
        init_sys_messages = messages.copy()

        while True:
            # Get user input
            user_input = input("(User) You: ")
            if user_input == "q":
                break

            # Add user message to the conversation
            messages.append({
                "role": "user",
                "content": user_input
            })

            # Call the API with the conversation history
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192"
            )

            # Get and print the assistant's reply
            assistant_reply = chat_completion.choices[0].message.content
            print(f"Assistant: {assistant_reply}")

            # Add assistant's reply to the conversation
            messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

            if system_mode:
                system_input = input("(System) You: ('skip' to skip)")
                if system_input != "skip":
                    init_sys_messages.append({
                        "role": "system",
                        "content": system_input
                    })
            if assistant_reply.endswith("bye-bye!"):
                print("End of conversation!")
                break
        self.save_sys_instructions(init_sys_messages)
