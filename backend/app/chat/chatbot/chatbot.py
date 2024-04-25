
from openai import OpenAI

from .constants import OPEN_AI_API_KEY


class ChatBot:
    _client = OpenAI(api_key=OPEN_AI_API_KEY)
    _messages = [
        {"role": "system", "content": "Você é um assistente que deve se passar por um humano para responder dúvidas relacionadas a atendimento e suporte do sistema IntelliCash da empresa IWS."},
    ]

    def send_message(self, prompt: str) -> str:
        """
        Method to send a message to the ChatBot.
        """
        self._messages.append({"role": "user", "content": prompt})

        completion = self._client.chat.completions.create(
            model="gpt-4-turbo",
            messages=self._messages
        )

        response = completion.choices[0].message.content
        self._messages.append({"role": "assistant", "content": response})

        return response
