import subprocess
import sys
import os
import pkg_resources
import webbrowser

# Szükséges csomagok telepítése csak ha még nincsenek telepítve
requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
if os.path.exists(requirements_path):
    print("requirements.txt megtalálva. Csomagok telepítése...")

    # Szükséges csomagok beolvasása a requirements.txt-ből
    with open(requirements_path, 'r') as file:
        packages = file.read().splitlines()

    # Jelenleg telepített csomagok lekérdezése
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}

    # Filter out packages that are already installed
    missing_packages = [pkg for pkg in packages if pkg.lower().split("==")[0] not in installed_packages]

    if missing_packages:
        print(f"Hiányzó csomagok telepítése: {', '.join(missing_packages)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_packages])
    else:
        print("Minden szükséges csomag telepítve van.")
else:
    print("A requirements.txt nem található.")

# Csomagok importálása
import requests
import yaml
from flask import Flask
from app import routes  # A route-ok importálása az app könyvtárból

# Forrás URL-ek beolvasása
with open('forrasok.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Save path definiálása
save_path = 'raw_data'

#CSV-k letöltése
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

        # Letöltés után siker- / hibaüzenet kiírása
        print(f"{filename} letöltve")
    except requests.exceptions.RequestException as e:
        print(f"Hiba történt a {filename} letöltésekor: {e}")

# Flask alkalmazás inicializálása, beállítva a static és templates mappákat
app = Flask(__name__, static_folder='app/static', template_folder='app/static/templates')

# Route-ok betöltése a routes.py-ből
routes.register(app)

#A weboldal automatikus megnyitása
webbrowser.open('http://localhost:5000', new=2)  # Open in new tab

# Flask alkalmazás futtatása
if __name__ == '__main__':
    app.run()





