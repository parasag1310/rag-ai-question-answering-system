from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_ollama import OllamaLLM


with open("data/knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()


text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = text_splitter.split_text(text)

print("Chunks:", chunks)
print("Total Chunks:", len(chunks))


documents = [Document(page_content=chunk) for chunk in chunks]


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = FAISS.from_documents(
    documents,
    embedding_model
)

print("\nFAISS Vector Store Created Successfully!")


llm = OllamaLLM(model="llama3")


while True:

    query = input("\nAsk Question: ")

    if query.lower() == "exit":
        print("Exiting...")
        break

    docs = vectorstore.similarity_search(query, k=2)

    print("\nRelevant Chunks:\n")

    for doc in docs:
        print(doc.page_content)
        print("-" * 50)

    context = "\n".join([doc.page_content for doc in docs])

    final_prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(final_prompt)

    print("\nAI Generated Answer:\n")
    print(response)