import os
from mistralai import Mistral
import json
from data_transactions import transaction_tools, transaction_names_to_functions
from data_bornes_elec import bornes_elec_tools, bornes_elec_names_to_functions
"""
https://docs.mistral.ai/capabilities/function_calling/
"""

api_key = "COjKAsQBhtXI95pip5gDjSbZJ9H63q7r"
client = Mistral(api_key=api_key)

# Dictionary mapping data sources to their tools and function mappings
data_sources = {
    "transactions": {
        "tools": transaction_tools,
        "functions": transaction_names_to_functions
    },
    "bornes_elec": {
        "tools": bornes_elec_tools,
        "functions": bornes_elec_names_to_functions
    }
}

def process_request(user_message, data_source_name):
    """
    Process a user request using the specified data source
    
    Parameters:
    - user_message: The message from the user
    - data_source_name: Name of the data source to use ('transactions' or 'bornes_elec')
    """
    # Check if the data source exists
    if data_source_name not in data_sources:
        return f"Error: Data source '{data_source_name}' not found."
    
    # Get the tools and functions for the selected data source
    data_source = data_sources[data_source_name]
    tools = data_source["tools"]
    functions = data_source["functions"]
    
    # Initialize conversation with user message
    messages = [{"role": "user", "content": user_message}]
    
    # First API call to get the function to call
    chat_response = client.agents.complete(
        agent_id="ag:7e1f4155:20250521:untitled-agent:7404ab45",
        messages=messages,
        tools=tools,
        tool_choice="any",
        parallel_tool_calls=False
    )
    
    messages.append(chat_response.choices[0].message)
    
    # Process tool call
    tool_call = chat_response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    function_params = json.loads(tool_call.function.arguments)
    print("\nfunction_name: ", function_name, "\nfunction_params: ", function_params)
    
    # Call the function with parameters
    function_result = functions[function_name](**function_params)
    print(function_result)
    
    # Add the result to messages
    messages.append({
        "role": "tool",
        "name": function_name,
        "content": function_result,
        "tool_call_id": tool_call.id
    })
    
    # Final API call to get AI response
    response = client.agents.complete(
        agent_id="ag:7e1f4155:20250521:untitled-agent:7404ab45",
        messages=messages
    )
    
    # Return the AI's final response
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    # Choose which data source to use: "transactions" or "bornes_elec"
    selected_source = "transactions"
    
    # User query
    user_query = "What's the status of my transaction T1001"
    
    # If using bornes_elec, you can change the query to be relevant
    if selected_source == "bornes_elec":
        user_query = "Find electric charging stations near Paris"
    
    # Process and display results
    result = process_request(user_query, selected_source)
    print("\nAI Response:")
    print(result)