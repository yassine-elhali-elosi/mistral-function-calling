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

def function_calling(dataSource):
    if dataSource == "transactions":
        messages = [{"role": "user", "content": "What's the status of my transaction T1001"}]
        tools = transaction_tools
        names_to_functions = transaction_names_to_functions
    else:
        messages = [{"role": "user", "content": "What stations have at least 5 charging points?"}]
        tools = bornes_elec_tools
        names_to_functions = bornes_elec_names_to_functions
    
    chat_response = client.agents.complete(
        agent_id="ag:7e1f4155:20250521:untitled-agent:7404ab45",
        messages=messages,
        tools=tools,
        tool_choice="any",
        parallel_tool_calls=False
    )

    messages.append(chat_response.choices[0].message)

    tool_call = chat_response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    function_params = json.loads(tool_call.function.arguments)
    print("\nfunction_name: ", function_name, "\nfunction_params: ", function_params)

    function_result = names_to_functions[function_name](**function_params)
    print(function_result)

    messages.append({
        "role": "tool",
        "name": function_name,
        "content": function_result,
        "tool_call_id": tool_call.id
    })

    response = client.agents.complete(
        agent_id="ag:7e1f4155:20250521:untitled-agent:7404ab45",
        messages=messages
    )

    print(response.choices[0].message.content)

function_calling("bornes_elec")