import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    VECTOR_DB_PATH = 'vector_db'
    HF_TOKEN=os.getenv("HF_TOKEN")