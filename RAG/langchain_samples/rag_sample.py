from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="phi3")

print(llm.invoke("Что такое RAG?").content)
