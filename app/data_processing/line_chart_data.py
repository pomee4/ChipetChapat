import pandas as pd
import matplotlib.pyplot as plt
import os

# Projekt gyökérkönyvtárának meghatározása
projekt_gyoker = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def get_line_chart_data():
    # CSV fájl beolvasása
    file_path =  os.path.join(projekt_gyoker, 'raw_data', 'kor0068.csv')
    data = pd.read_csv(file_path, encoding='latin-1', delimiter=';', header=None)

    # Megkeressük a sorindexeket, ahol a gáz- és villamosenergia-felhasználás kezdődik
    gas_row_index = data[0].str.contains('vezetékesgáz-felhasználás', na=False).idxmax()
    electric_row_index = data[0].str.contains('villamosenergia-felhasználás', na=False).idxmax()

    # Megkeressük a gáz- és villamosenergia-felhasználás adatsorait
    gas_data = data.iloc[gas_row_index + 1, 2:].replace(',', '.', regex=True).astype(float).reset_index(drop=True)
    electric_data = data.iloc[electric_row_index + 1, 2:].replace(',', '.', regex=True).astype(float).reset_index(drop=True)

    # Megkeressük az éveket
    years = data.iloc[1, 2:].astype(int).reset_index(drop=True)

    # Visszaadjuk az éveket, a gáz- és villamosenergia-felhasználást
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # A bal y-tengelyen a villamosenergia-felhasználás
    ax1.plot(years, electric_data, label='Electric Usage', color='blue', marker='o')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Electric Usage (kWh)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # A jobb y-tengelyen a gázfelhasználás
    ax2 = ax1.twinx()
    ax2.plot(years, gas_data, label='Gas Usage', color='red', marker='x')
    ax2.set_ylabel('Gas Usage (m³)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Címkék hozzáadása
    plt.title("Budapest's Energy Usage Over the Years")
    plt.grid(True)

    # A diagram mentése
    plt.savefig('app/static/images/line_chart.png')
