from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load Dotenv
load_dotenv();
import os;

# retrieves the value of the environment variable
api_key=os.getenv("GOOGLE_GEMINI_API_KEY");
out=StrOutputParser();

# Creating Ai Model Object
llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

prompts=[
    {"role":"system","content":"You are a Javascript Developer"},
    {"role":"user","content":"Difference between Map and Filter"},
]
res=llm.invoke(prompts);
print(res.content);

# Dynamic Prompts
prompts=ChatPromptTemplate.from_messages([
    {"role":"system","content":"You are a Translator and translate input in {language}"},
    {"role":"user","content": "{query}"}
])
final_prompts=prompts.format_messages(language="Hinglish",query="I love python and js")
res=llm.invoke(final_prompts);
print(res.content);

# Chains
res=llm.invoke(prompts.invoke({"language":"Hinglish","query":"Hi,How are you"}));
print(res.content);

chains=prompts|llm|out;
res=chains.invoke({"language":"Hinglish","query":"Hi,How are you"});
print(res);