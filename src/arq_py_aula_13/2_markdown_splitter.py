from langchain_text_splitters import MarkdownHeaderTextSplitter


caminho = r'.\src\arq_py_aula_13\exemplo_markdown.md'

with open(caminho) as f:
    arquivo = f.read()

# Mapeamento de quebras:
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

# Instanciando o separador:
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

# Aplicando o separador:
resultado_com_split_de_cabecalho = markdown_splitter.split_text(arquivo)

i = 0
for pedaco in resultado_com_split_de_cabecalho:
    print("--" * 30)
    print(f"Chunk: {i}")
    print("--" * 30)
    print(pedaco)
    print("--" * 30)
    i += 1

# https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb
# https://python.langchain.com/docs/how_to/semantic-chunker/