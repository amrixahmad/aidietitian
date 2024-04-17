from dotenv import load_dotenv
import os

load_dotenv()

DIETITIAN_TOKEN=os.getenv("DIETITIAN_TOKEN")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")