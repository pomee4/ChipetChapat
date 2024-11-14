import subprocess
import sys
import os
import pkg_resources

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



# Modulok importálása
import requests
import yaml
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

        # Sikeres letöltés esetén üzenet kiírása
        print(f"{filename} letöltve")
    except requests.exceptions.RequestException as e:
        print(f"Hiba történt a {filename} letöltésekor: {e}")


