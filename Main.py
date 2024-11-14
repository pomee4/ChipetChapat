# Modulok importálása
import sqlite3
import csv
import requests
import yaml
import os
import flask
import matplotlib

# Forrás URL-ek beolvasása
with open('forrasok.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Save path definiálása
save_path = 'raw_data'

# URL-ek beolvasása és CSV-k letöltése
for entry in data['forras']:
    file_id = entry['id']
    url = entry['url']
    filename = os.path.join(save_path, f"{file_id}.csv")  # CSV fájlok mentése a raw_data almappába

    try:
        # GET request küldése a megadott URL-re
        response = requests.get(url)

        # CSV mentése
        with open(filename, 'wb') as file:
            file.write(response.content)


        print("{filename} letöltve")
    except requests.exceptions.RequestException as e:
        print("Hiba a letöltésben innen: {url}.")

