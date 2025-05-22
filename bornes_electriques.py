# https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/
import requests
import pandas as pd

r = requests.get("https://tabular-api.data.gouv.fr/api/resources/eb76d20a-8501-400e-b336-d85724de5435/data/")
data = r.json()["data"]
data_df = pd.DataFrame(data)

print(data_df)