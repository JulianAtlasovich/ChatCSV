# Setting Agent

#from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain_community.chat_models import ChatOpenAI


API_KEY = "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"

def create_agent(df):
     """
    Create an agent that can access and use a large language model (LLM).

    Args:
        filename: The path to the CSV file that contains the data.

    Returns:
        An agent that can access and use the LLM.
    """
     

     # Creating an openai object
     #llmodel = OpenAI(openai_api_key=API_KEY,model_name=)

     # Reading the csv file uploaded by USER
     
     return create_pandas_dataframe_agent(ChatOpenAI(openai_api_key=API_KEY,temperature=0, model="gpt-4-1106-preview"), df, verbose = False)#model_name

# Query Agent

def query_agent(agent, query):
    """
    Query an agent and return the response as a string.

    Args:
        agent: The agent to query.
        query: The query to ask the agent.

    Returns:
        The response from the agent as a string.
    """

    prompt = (
        """
            Do not include markdown indicators such as "```json```" in your answer, just the json directly

            For the following query, if it requires drawing a table, reply as follows:
            {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

            If the query requires creating a bar chart, reply as follows:
            {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

            If the query requires creating a line chart, reply as follows:
            {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

            There can only be two types of chart, "bar" and "line".

            If it is just asking a question that requires neither, reply as follows:
            {"answer": "answer"}
            Example:
            {"answer": "The title with the highest rating is 'Gilead'"}

            If you do not know the answer, reply as follows:
            {"answer": "I do not know."}

            Return all output as a string.

            All strings in "columns" list and data list, should be in double quotes,

            For example: {"columns": ["title", "ratings_count"], "data": [["Gilead", 361], ["Spider's Web", 5164]]}

            Lets think step by step.

            Below is the query.
            Query: 
            """
        + query
    )

    # Run the prompt through the agent.
    response = (agent.run(prompt)).__str__()
    response = response.replace('```json', '')
    response = response.replace('```', '')
    print('----------------')
    print(query)
    print(response)
    print('----------------')
    return response