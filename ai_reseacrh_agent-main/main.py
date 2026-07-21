from dotenv import load_dotenv
from pydantic import BaseModel

# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent 
from tools import search_tool, wiki_tool, save_tool
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]





llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7
    )
# llm2 = ChatAnthropic(model="claud-3-5-sonnet-20241022")
# response = llm.invoke("what is the meaning of life")
# print(response)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)


tools = [search_tool,wiki_tool, save_tool]

agent = create_agent(
    model = llm,
    tools=tools,
)


query = input("What can i help you research?")


response= agent.invoke({
        "messages": [
            ("user",query),
            ("system","""
You are a research assistant.

You MUST return output ONLY in valid JSON format.

Format:
{
  "topic": "...",
  "summary": "...",
  "sources": ["...", "..."],
  "tools_used": ["..."]
}
"""),
            ]
    })


content= response["messages"][-1].content

if isinstance(content,list):
    final_text = content[0]["text"]
else:
    final_text= content

try:
    structured =parser.parse(final_text)
    print(structured)
except Exception as e:
    print("Parsing failed, raw output:\n")
    print(final_text)