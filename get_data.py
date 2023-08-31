import requests
import pandas as pd
import os
from io import StringIO

# 1. Download the CSV
url = "https://opendata.infrabel.be/api/explore/v2.1/catalog/datasets/ruwe-gegevens-van-stiptheid-d-1/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
response = requests.get(url)
csv_content = response.text

# 2. Parse the CSV
new_data = pd.read_csv(StringIO(csv_content), delimiter=';')

# 3. Check if the CSV file exists. If not, create it. Otherwise, append the new data.
file_path = "data_trains.csv"

if os.path.exists(file_path):
    existing_data = pd.read_csv(file_path, delimiter=';')
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    combined_data.to_csv(file_path, index=False, sep=';')
else:
    new_data.to_csv(file_path, index=False, sep=';')
