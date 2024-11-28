import subprocess
import sys
import os
import pkg_resources
import webbrowser

# Szükséges csomagok telepítése csak ha még nincsenek telepítve
requirements_utvonal = os.path.join(os.path.dirname(__file__), 'requirements.txt')
if os.path.exists(requirements_utvonal):
    print("requirements.txt megtalálva. Csomagok telepítése...")

    # Szükséges csomagok beolvasása a requirements.txt-ből
    with open(requirements_utvonal, 'r') as file:
        csomagok = file.read().splitlines()

    # Jelenleg telepített csomagok lekérdezése
    telepitett_csomagok = {pkg.key for pkg in pkg_resources.working_set}

    # Hiányzó csomagok kiválogatása
    hianyzo_csomagok = [pkg for pkg in csomagok if pkg.lower().split("==")[0] not in telepitett_csomagok]

    if hianyzo_csomagok:
        print(f"Hiányzó csomagok telepítése: {', '.join(hianyzo_csomagok)}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *hianyzo_csomagok])
    else:
        print("Minden szükséges csomag telepítve van.")
else:
    print("A requirements.txt nem található.")

# Csomagok importálása
import requests
import yaml
from flask import Flask

# Forrás URL-ek beolvasása
print("Forrás URL-ek beolvasása...")
with open('forrasok.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Mentesi utvonal definiálása
mentesi_utvonal = 'raw_data'

print("CSV fájlok letöltése...")
#CSV-k letöltése
for entry in data['forras']:
    file_id = entry['id']
    url = entry['url']
    filenev = os.path.join(mentesi_utvonal, f"{file_id}.csv")  # CSV fájlok mentése a raw_data almappába

    try:
        # GET request küldése a megadott URL-re
        valasz = requests.get(url)

        # CSV mentése
        with open(filenev, 'wb') as file:
            file.write(valasz.content)

        # Letöltés után siker- / hibaüzenet kiírása
        print(f"{filenev} letöltve")
    except requests.exceptions.RequestException as e:
        print(f"Hiba történt a {filenev} letöltésekor: {e}")

print("CSV fájlok letöltése kész.")

from app import routes  # A route-ok importálása az app könyvtárból
# Flask alkalmazás inicializálása, beállítva a static és templates mappákat
app = Flask(__name__, static_folder='app/static', template_folder='app/static/templates')
print("Flask alkalmazás inicializálva.")
# Route-ok betöltése a routes.py-ből
routes.register(app)

#A weboldal automatikus megnyitása
webbrowser.open('http://localhost:5000', new=2)  # Megnyitás új tabon

# Flask alkalmazás futtatása
if __name__ == '__main__':
    app.run()





