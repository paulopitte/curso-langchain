# Chat Model Documents: https://python.langchain.com/docs/integrations/chat/

from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM, ChatOllama

# Carregando as variaveis de '.env'
load_dotenv()

# Chama a API do modelos da Open IA.
model = OllamaLLM(model="llama3.1", base_url="http://localhost:11434", temperature=0.3)

# Executa a chamada ao modelo
result = model.invoke("Este é um teste. Se você recebeu a requisição responda 'Teste OK'.")
print(result)

 