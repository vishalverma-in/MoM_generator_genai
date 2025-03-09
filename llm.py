import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
 
def create_gemini_llm():
    llm_gemini = ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL"),
        temperature=0,
        max_tokens=None,
        api_key=os.getenv("GEMINI_API_KEY") # Pass the API key to the model
    )
    return llm_gemini


