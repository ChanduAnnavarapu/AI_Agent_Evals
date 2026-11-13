from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain.chat_models import init_chat_model
load_dotenv()  
import os

# model=init_chat_model(
#     model=os.getenv("MODEL_NAME"),
#     model_provider="openrouter",
#     api_key=os.getenv("API_KEY"),
#     temperature=0
# )

model = ChatOpenRouter(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("API_KEY"),
    temperature=0
)

response = model.invoke("Hello, can you tell me a joke?")
print(response.content)
