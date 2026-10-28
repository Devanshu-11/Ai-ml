# Langchain is used to build applications powered by AI models like- OpenAi and Google Gemini. It helps to connect an Ai model with our data,tools,databases and other parts of your application without writing all the integration logic yourself

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Dotenv
load_dotenv();
import os;

# retrieves the value of the environment variable
api_key=os.getenv("GOOGLE_GEMINI_API_KEY");

# Creating Ai Model Object
llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

# Now sending question to LLM
response=llm.invoke("Who is Prime Minister of India");
print(response.content);

# static prompts
prompts=[
    ("system","You are a python developer"),  #(type) "system","system","user"
    ("user","How to sort the array")
]
res=llm.invoke(prompts);
print(res.content);