from langchain_community.tools import WikipediaQueryRun,  DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper
from datetime import datetime
import uuid

search = DuckDuckGoSearchRun()




@tool
def save_tool(data:str)-> str:
    """ 
    Save research output to a text file. 

    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "Research_output.txt"

    formatted_text = f"---Research Output ---\nTimestamp:{timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return formatted_text

@tool
def search_tool(query:str)->str:
    """
    Search the web for recent and factual information about a topic.
    """
    return search.run(query)


api_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=100)
wiki_api= WikipediaQueryRun(api_wrapper=api_wrapper)

@tool
def wiki_tool(query:str)->str:
    """
        Search Wikipedia for information.
        """
    return wiki_api.run(query)

