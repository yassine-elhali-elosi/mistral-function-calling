# https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/
import requests
import pandas as pd
import json
import functools

r = requests.get("https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/")
data = r.json()["data"]
data_df = pd.DataFrame(data)

def retrieve_minimum_charging_points_number(df: data_df, nbre_pdc: int) -> object:
    results = []
    for i in range(len(df)):
        element = df.iloc[i]
        if element["nbre_pdc"] >= nbre_pdc:
            results.append(element)

    if len(results) == 0:
        return json.dumps({'error': 'No charging points found with the specified number.'})
    #print(results)
    #print(len(results))
    return json.dumps({'count': len(results)})

bornes_elec_tools = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_minimum_charging_points_number",
            "description": "Get charging points with a minimum number of charging points.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nbre_pdc": {
                        "type": "integer",
                        "description": "The minimum number of charging points.",
                    }
                },
                "required": ["nbre_pdc"],
            },
        },
    }
]

bornes_elec_names_to_functions = {
    'retrieve_minimum_charging_points_number': functools.partial(retrieve_minimum_charging_points_number, df=data_df)
}