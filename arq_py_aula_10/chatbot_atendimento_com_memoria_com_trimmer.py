from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Carregar as chas APIs presentes no arquivo .env
load_dotenv()
# --------------------------------------------------------------------------------

## Criando o gestor de memória (histórico)
# Função para retornar o histórico de mensagens com base no session_id

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, connection="sqlite:///memory.db")

# --------------------------------------------------------------------------------

# Instancias um chatmodel para comunicarmos com os modelos LLMs
model = ChatOpenAI(model="gpt-4o", temperature=0.2)

# --------------------------------------------------------------------------------

# Definindo o prompt de chatbot que tira duvidas do usuário:

sys_chatbot_prompt = """ Você é um assistente de uma clinica odontológica e tem como objetivo responder à perguntas dos clientes. A seguir você \  
encontra a FAQ do nosso site, use essas informações para realizar o atendimento e tirar dúvidas. Caso você desconheça alguma \  
informação, não invente. Seja sempre amigável e esteja disposto a ajudar!  

**FAQ - Clínica Odontológica**  
1. **Quais serviços a clínica oferece?**    
   Oferecemos tratamentos como limpeza dental, clareamento, ortodontia, implantes, próteses, tratamento de canal e estética dental.  
2. **A clínica aceita convênios?**    
   Sim, trabalhamos com os principais convênios odontológicos. Consulte nossa equipe para verificar se aceitamos o seu.  
3. **Como agendar uma consulta?**    
   Você pode agendar sua consulta pelo telefone, WhatsApp ou diretamente em nosso site.  
4. **Quanto tempo dura uma consulta?**    
   Depende do procedimento, mas consultas de rotina geralmente duram entre 30 e 60 minutos.  
5. **Vocês atendem emergências?**    
   Sim, oferecemos atendimento emergencial para dores agudas, traumas ou casos de urgência.  
6. **É possível parcelar tratamentos?**    
   Sim, oferecemos opções de parcelamento. Entre em contato para conhecer os detalhes.  
7. **Crianças podem ser atendidas na clínica?**    
   Sim, contamos com profissionais especializados em odontopediatria para cuidar dos sorrisos dos pequenos.  
8. **O clareamento dental é seguro?**    
   Sim, nossos tratamentos de clareamento são realizados com técnicas e produtos seguros, supervisionados por especialistas.  
Se tiver mais dúvidas, entre em contato conosco! 😊  
"""

prompt_template_chatbot = ChatPromptTemplate.from_messages([
    ("system", sys_chatbot_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Dúvida do usuário: {input}"),
]
)

chain_chatbot = prompt_template_chatbot | model | StrOutputParser()

# --------------------------------------------------------------------------------
## Encapsulando nossa chain com a classe de gestão de mensagens de histórico
# Criando a função que corta o histórico de mensagem para 2 ultimas mensagens trocadas:
from operator import itemgetter

from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnablePassthrough

trimmer = trim_messages(strategy="last", max_tokens=2, token_counter=len)

chain_with_trimming = (
    RunnablePassthrough.assign(history=itemgetter("history") | trimmer)
    | chain_chatbot
)

runnable_with_history = RunnableWithMessageHistory(
    chain_with_trimming,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
# --------------------------------------------------------------------------------


# Executando nossa chain principal.
result = runnable_with_history.invoke(
    {"input": "Olá tudo bem? Qual meu nome?"},
    config={"configurable": {"session_id": "1"}},
)

# --------------------------------------------------------------------------------
# Imprimindo a saida.
print("---------------")
print(result)
print("---------------")