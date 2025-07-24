import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
from backend.vectordb import get_vectorstore
# System prompt
groq_prompt = ChatPromptTemplate.from_template("""
You are very smart at everything, you always give the best, 
the most accurate and most precise answers. Answer the following Question: {user_prompt}.
Start the answer directly. No small talk please.
""")

model = "llama3-8b-8192"

groq_chat = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model_name=model
)

def get_answer(prompt: str) -> str:
    vectorstore = get_vectorstore()
    chain = RetrievalQA.from_chain_type(
        llm=groq_chat,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    result = chain({"query": prompt})
    return result["result"]
