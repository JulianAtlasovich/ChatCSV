import streamlit as st
import pandas as pd
import json
from agent import query_agent, create_agent
import os



def decode_response(response: str) -> dict:
    """
    Decode the response from the agent.

    Args:
        response: The response from the agent.

    Returns:
        The decoded response as a dictionary.
    """
    return 


def write_response(response_dict: dict):
    """
    Write the response from the agent.

    Args:
        response_dict: The response from the agent as a dictionary.
    """

    # Check if the response is an answer
    if "answer" in response_dict:
        st.write(response_dict["answer"])

    # Check if the response is a bar chart

    if "bar" in response_dict:
        data = response_dict["bar"]        
        df = pd.DataFrame(data)
        df.set_index("columns", inplace = True)
        st.bar_chart(df)


    # Check if the response is a table
    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)

    # Check if the response is a line chart
    if "line" in response_dict:
        data = response_dict["line"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace = True)
        st.line_chart(df)


## Interface Code
#data = st.file_uploader("Upload a CSV file", type=["csv"])
st.title("Just ask...")
query = st.text_input(" ")
df = pd.read_csv('Sales_example.csv')

if st.button("Submit", type = "primary"):
    with st.spinner('Generating response...'):        
        agent = create_agent(df)
        response = query_agent(agent = agent, query = query)
        decoded_response = json.loads(response)
        st.markdown("""---""")
        st.success('Answer:')
        write_response(decoded_response)

st.markdown("""---""")
st.table(df)