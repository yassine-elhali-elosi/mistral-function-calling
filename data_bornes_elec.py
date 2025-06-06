# https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/
import requests
import pandas as pd
import json
import functools

r = requests.get("https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/")
data_df = r.json()["data"]
#data_df = pd.DataFrame(data)

def toto(df: data_df, nbre_pdc: int) -> object:
    results = []
    for i in range(len(df)):
        element = df[i]
        if element["nbre_pdc"] >= nbre_pdc:
            results.append({
                "station_id": element["id_station_local"],
                "nbre_pdc": element["nbre_pdc"],
            })

    if len(results) == 0:
        return json.dumps({'error': 'No charging points found with the specified number.'})
    #print(results)
    #print(len(results))
    print(results)
    return json.dumps({'data': results})

if __name__ == "__main__":
    print(toto(data_df, 8))

bornes_elec_tools = [
    {
        "type": "function",
        "function": {
            "name": "toto",
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
    'toto': functools.partial(toto, df=data_df)
}