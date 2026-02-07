## 🎙️ Assistente de Voz Inteligente (Groq Edition)
Este projeto é um assistente virtual conversacional capaz de ouvir, processar e responder com voz natural utilizando inteligência artificial de alta velocidade.

## 🚀 Desafio e Superação Técnica
Embora o projeto original sugerisse o uso da API da OpenAI, optei por uma migração estratégica para a Groq Cloud.

-**Por que Groq?** Utilizei a arquitetura LPU™ da Groq para garantir uma latência ultra-baixa, tornando a conversa muito mais fluida e rápida do que em modelos convencionais.

-**Economia e Acessibilidade**: Essa escolha permitiu a viabilidade do projeto em ambiente de testes sem custos de créditos iniciais, mantendo a alta performance com o modelo Llama 3.3.

## 🎭 Por que "Jarvis"?
Escolhi a persona do Jarvis (do Homem de Ferro) para demonstrar a capacidade de Engenharia de Prompt. O código foi configurado para que a IA adote uma postura elegante e eficiente, provando que o sistema pode ser facilmente adaptado para qualquer outra persona, como uma "Agente Financeira Virtual", apenas ajustando o contexto do sistema.

## 🛠️ Tecnologias
- **Groq Cloud**: Processamento de IA ultra-rápido.

- **Llama 3.3**: O "cérebro" que gera as respostas inteligentes.

-**Whisper**: Tecnologia de Reconhecimento Automático de Fala (ASR) para transcrição.

-**gTTS**: Síntese de voz do Google para as respostas faladas.

## 📂 Estrutura
- `src/`: Códigos fonte.
- `logs/`: Histórico de conversas (criada automaticamente).

## 🛠️ Como rodar o projeto
1. Instale as dependências: `pip install -r requirements.txt`
2. Configure sua chave no arquivo `.env`.
3. Rode o comando: `python src/main.py`

