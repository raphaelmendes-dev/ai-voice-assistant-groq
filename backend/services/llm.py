import os
from datetime import datetime
from groq import Groq
from config import GROQ_API_KEY

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


class LLMService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = "llama-3.3-70b-versatile"
        self.history = []
        self.system_prompt = (
            "Você é a Sofia, assistente virtual inteligente da Rs4Machine. "
            "Responda de forma clara, objetiva e sempre em português. "
            "Máximo 2 frases por resposta. Seja direta e útil."
        )

    def chat(self, user_message: str) -> str:
        """
        Recebe mensagem do usuário, retorna resposta da Sofia.
        Mantém histórico dos últimos 10 turnos.
        """
        self.history.append({"role": "user", "content": user_message})

        # Mantém janela de contexto enxuta
        if len(self.history) > 10:
            self.history = self.history[-10:]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    *self.history,
                ],
                max_tokens=300,
            )
            bot_response = response.choices[0].message.content
            self.history.append({"role": "assistant", "content": bot_response})
            self._save_log(user_message, bot_response)
            return bot_response

        except Exception as e:
            print(f"❌ Erro no LLM: {e}")
            return "Desculpe, ocorreu um erro ao processar sua mensagem."

    def _save_log(self, user_msg: str, bot_msg: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"conversa_{datetime.now().strftime('%Y-%m-%d')}.txt"
        entry = (
            f"============================================================\n"
            f"[{timestamp}]\n"
            f"👤 USUÁRIO: {user_msg}\n"
            f"🤖 SOFIA: {bot_msg}\n"
        )
        with open(os.path.join(LOG_DIR, filename), "a", encoding="utf-8") as f:
            f.write(entry)