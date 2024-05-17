
from openai import OpenAI

from .constants import OPEN_AI_API_KEY


CHATBOT_DEFER_MESSAGE = "Não estou conseguindo te ajudar. Aguarde um momento enquanto eu te transfiro para nosso suporte técnico."


CHATBOT_BEHAVIOR = (
    "Você é um assistente que deve se passar por um humano para responder dúvidas relacionadas a atendimento e suporte "
    "do sistema IntelliCash da empresa IWS. Caso não saiba responder uma pergunta com precisão ou fique com dúvidas "
    "ou indeciso ou se a resposta for idêntica a uma resposta anterior, você deve informar o usuário que ele será transferido "
    "para o suporte técnico que saberá resolver a situação. "
    "Quando isso ocorrer e você for eefetivamente transferir o usuário para o suporte técnico, "
    "sua mensagem de resposta deverá ser exatamente a seguinte: "
    f"'{CHATBOT_DEFER_MESSAGE}' escrito dessa exata maneira."
)


class ChatBot:
    _client = OpenAI(api_key=OPEN_AI_API_KEY)
    _messages = [
        {"role": "system", "content": CHATBOT_BEHAVIOR},
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
