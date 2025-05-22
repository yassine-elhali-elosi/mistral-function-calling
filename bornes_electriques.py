# https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/
import requests
import pandas as pd
import json
import functools

r = requests.get("https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/")
data = r.json()["data"]
data_df = pd.DataFrame(data)

def retrieve_minimum_charging_points_number(df: data_df, nb: int) -> object:
    results = []
    for i in range(len(data_df)):
        element = data_df.iloc[i]
        if element["nbre_pdc"] >= nb:
            results.append(element)

    if len(results) == 0:
        return json.dumps({'error': 'No charging points found with the specified number.'})
    print(results)
    print(len(results))
    return results

retrieve_minimum_charging_points_number(data_df, 8)

names_to_functions = {
    'retrieve_minimum_charging_points_number': functools.partial(retrieve_minimum_charging_points_number, df=data_df)
}