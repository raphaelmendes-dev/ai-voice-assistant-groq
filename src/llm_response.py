import os
from groq import Groq
from datetime import datetime

class ChatGPTAssistant:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY não encontrada no .env")

        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"
        self.history = []
        
        # Garante que a pasta de logs existe
        self.log_dir = "logs"
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def _save_log(self, user_msg, bot_msg):
        """Salva a interação no arquivo de log com timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"============================================================\n"
            f"[{timestamp}]\n"
            f"👤 USUÁRIO: {user_msg}\n"
            f"🤖 JARVIS: {bot_msg}\n"
        )
        with open(os.path.join(self.log_dir, "conversa.txt"), "a", encoding="utf-8") as f:
            f.write(log_entry)

    def get_response(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        
        if len(self.history) > 10:
            self.history = self.history[-10:]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Você é o Jarvis do Homem de Ferro. Responda de forma elegante, chame o usuário de 'Senhor' e seja muito eficiente."},
                    *self.history
                ],
                max_tokens=150
            )
            bot_response = response.choices[0].message.content
            self.history.append({"role": "assistant", "content": bot_response})
            
            # Salva no log antes de retornar
            self._save_log(user_message, bot_response)
            
            return bot_response
        except Exception as e:
            return f"Erro no cérebro: {e}"