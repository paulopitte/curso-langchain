# Curso LangChain

Bem-vindo ao repositório do Curso LangChain! a idéia é criar exemplos e implementações de tudo que for possível fazer com LLM integrado, construir chatbots RAG e automatizar tarefas com IA.

## Começando

**Q: O que é LangChain?**\
A: LangChain é um framework que simplifica o processo de criação de aplicações que utilizam modelos de linguagem.

**Q: Como configuro meu ambiente?**\
A: Siga as instruções na seção "Começando" acima. Certifique-se de ter o Python 3.11 ou superior instalado, clone o repositório, instale as dependências, renomeie o arquivo `.env.example` , ative o ambiente virtual e execute os scripts desejado.

**Q: Estou tendo problemas ao executar os exemplos, o que faço?**\
A: Verifique se todas as dependências foram instaladas corretamente e se as variáveis de ambiente estão configuradas. Se o problema persistir, mande uma mensagem para mim na comunidade do Discord ou do WhatsApp que podemos te ajudar.

### Pré-requisitos

- Sistema operacional Windows 11 ou superior.
- Python 3.12.8
- Criar um ambiente virtual e clonar o repositório
- Instalar as dependências presentes no arquivo requirements.txt

### Instalação

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

   **Atenção**: Se por acaso o comando de instalação das dependências acima não funcionar, tente executar a instalação via terminal pip:

```
pip install langchain-openai langchain langchain-core langchain-community langchain-experimental python-dotenv SQLAlchemy
```

3. Configure as variáveis de ambiente:
   - Em `.env` atualize as variáveis com seus valores.

5) Crie o ambiente virtual:

   ```
   python -m venv .venv
   ```

6) Caso o processo de download das bibliotecas demore (mensagem "This could take a while" no log de download) você utilizar os seguintes passos:

   _6.1 Instalador 'uv'_
   - Ele é um substituto do pip escrito em Rust que resolve dependências em segundos, enquanto o pip leva minutos:

   ```
   pip install uv
   ```

   _6.2 Crie o ambiente virtual_

   ```
   uv venv
   ```

   _6.3 Ativa o ambiente (Windows)_

   ```
   .\.venv\Scripts\activate
   ```

   _6.4 Instale as dependências_

   ```
   uv pip install -r requirements.txt
   ```

7) Execute os exemplos de código via interface ou via terminal, conforme sua preferência.

## Estrutura do Repositório

Veja o que você encontrará em cada pasta:

### 7.1. Chat Models

- Exemplos de como interagir com modelos de linguagem como ChatGPT e Claude utilizando o componente `Models` do LangChain.

### 7.2. Prompt Templates

- Exemplos que explicam os conceitos básicos dos tipos de templates que o langchain oferece e como usá-los.

### 3. Analisadores de Saída

- Demonstraremos os tipos mais importantes dos analisadores de saída (textual e estruturada).

### 7.4. Chains

- Como criar cadeias usando modelos de chat, prompts e outros componentes para criar integrações e aplicações que usam LLM.

### 7.5. Carregadores (Document Loaders)

- Como carregar documentos de diferentes fontes para utilizar nos seus projetos.

### 7.6. Memória

- Exploração dos conceitos de memória para interações prolongadas com modelos.

### 7.7. Chatbot

- Construindo um chatbot interativo usando LangChain.

### 7.8. RAG (Retrieval-Augmented Generation)

- Conceitos como Splitters, Embedding, Bases Vetoriais e Recuperadores.

## Documentação Completa

Cada script neste repositório contém comentários detalhados explicando o propósito e a funcionalidade do código. Isso ajudará a entender o fluxo e a lógica por trás de cada exemplo.
