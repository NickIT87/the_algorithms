from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# LLM
llm = ChatOllama(model="phi3")

# Embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Документы
docs = [
    Document(page_content="Python используется для backend и AI."),
    Document(page_content="Haskell — функциональный язык программирования."),
    Document(page_content="C++ часто используется в game development."),
]

# Vector DB
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)

# Вопрос
question = "Какой язык подходит для functional programming?"

# Поиск похожих документов
results = vectorstore.similarity_search(question, k=2)

# Контекст
context = "\n".join(
    [doc.page_content for doc in results]
)

# Prompt
prompt = f"""
Ответь на вопрос используя контекст.

Контекст:
{context}

Вопрос:
{question}
"""

# Ответ LLM
response = llm.invoke(prompt)

print("=== Найденный контекст ===")
print(context)

print("\n=== Ответ модели ===")
print(response.content)

# === Найденный контекст ===
# Haskell — функциональный язык программирования.
# C++ часто используется в game development.

# === Ответ модели ===
# Ответ на вопрос: Haskell является идеальным выбором для 
# программирования функциональными подходами из-за своей 
# компиляции на высоком уровне и поддержки 
# функциональных конструкций.