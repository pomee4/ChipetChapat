# A megadott struktúra igazítása a kért diagramhoz és használati esethez
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import numpy as np  # Új import a LOG megjelenítéshez
from sklearn.linear_model import LinearRegression

# Projekt gyökérkönyvtárának meghatározása
projekt_gyoker = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Adatfájlok elérési útvonalainak beállítása
kor0068_utvonal = os.path.join(projekt_gyoker, 'raw_data', 'kor0068.csv')
mez0086_utvonal = os.path.join(projekt_gyoker, 'raw_data', 'mez0086.csv')

kor0068 = pd.read_csv(kor0068_utvonal, encoding='Windows-1252', delimiter=';', skiprows=3)
mez0086 = pd.read_csv(mez0086_utvonal, encoding='ISO-8859-1', delimiter=';', skiprows=3)


# Oszlopnevek átnevezése az egyértelműség érdekében
def rename_columns(df):
    df.rename(columns={"Budapest": "Régió", "fõváros, régió": "Típus"}, inplace=True)
    return df


kor0068 = rename_columns(kor0068)
mez0086 = rename_columns(mez0086)


# Függvény az adatok tisztítására: elválasztók eltávolítása, érvénytelen értékek kezelése, numerikus átalakítás
def tisztit_adatok_nelkul(df):
    tisztitott_df = df.copy()
    for oszlop in tisztitott_df.columns[2:]:  # Az első két oszlopot kihagyjuk (Terület neve és típus)
        tisztitott_df[oszlop] = (
            tisztitott_df[oszlop]
            .astype(str)
            .str.replace(r"[ ,]", "", regex=True)
            .str.replace(r"[^\d.-]", "", regex=True)
            .replace("", "NaN")
            .astype(float)
        )
    return tisztitott_df


kor0068_tisztitott = tisztit_adatok_nelkul(kor0068)
mez0086_tisztitott = tisztit_adatok_nelkul(mez0086)

# Adatok összekapcsolása a "Régió" oszlop alapján
osszekapcsolt_adatok = pd.merge(
    kor0068_tisztitott.iloc[:, [0, -1]].rename(columns={kor0068_tisztitott.columns[-1]: 'Éves energiafogyasztás'}),
    mez0086_tisztitott.iloc[:, [0, -1]].rename(columns={mez0086_tisztitott.columns[-1]: 'Éves gyümölcstermelés'}),
    on="Régió"
)

# Megyékhez tartozó színek és markerek beállítása
megyek = {
    # Kör piktogram
    "Budapest": {"color": "aqua", "marker": "o"},
    "Pest": {"color": "darkblue", "marker": "o"},
    "Közép-Magyarország": {"color": "blueviolet", "marker": "o"},
    "Fejér": {"color": "brown", "marker": "o"},
    "Komárom-Esztergom": {"color": "chocolate", "marker": "o"},
    "Veszprém": {"color": "darkorange", "marker": "o"},
    "Közép-Dunántúl": {"color": "darkred", "marker": "o"},
    "Győr-Moson-Sopron": {"color": "darkgreen", "marker": "o"},
    "Vas": {"color": "silver", "marker": "o"},
    # Háromszög pikrotgram
    "Zala": {"color": "aqua", "marker": "^"},
    "Nyugat-Dunántúl": {"color": "darkblue", "marker": "^"},
    "Baranya": {"color": "blueviolet", "marker": "^"},
    "Somogy": {"color": "brown", "marker": "^"},
    "Tolna": {"color": "chocolate", "marker": "^"},
    "Dél-Dunántúl": {"color": "darkorange", "marker": "^"},
    "Dunántúl": {"color": "darkred", "marker": "^"},
    "Borsod-Abaúj-Zemplén": {"color": "darkgreen", "marker": "^"},
    "Heves": {"color": "silver", "marker": "^"},
    # Négyzet piktorgram
    "Nógrád": {"color": "aqua", "marker": "s"},
    "Észak-Magyarország": {"color": "darkblue", "marker": "s"},
    "Hajdú-Bihar": {"color": "blueviolet", "marker": "s"},
    "Jász-Nagykun-Szolnok": {"color": "brown", "marker": "s"},
    "Szabolcs-Szatmár-Bereg": {"color": "chocolate", "marker": "s"},
    "Észak-Alföld": {"color": "darkorange", "marker": "s"},
    "Bács-Kiskun": {"color": "darkred", "marker": "s"},
    "Békés": {"color": "yellow", "marker": "s"},
    "Csongrád-Csanád": {"color": "darkgreen", "marker": "s"},
    "Dél-Alföld": {"color": "silver", "marker": "s"},
    "Alföld és Észak": {"color": "lime", "marker": "s"},
    # További megyék hozzáadása itt...
}

# Alapértelmezett szín és marker a nem definiált megyékhez
default_style = {"color": "magenta", "marker": "x"}


# Diagram generálás és regressziós modell funkció logaritmikus Y skálával
def generate_regression_chart_data_and_plot(data, x_col, y_col, output_path):
    x_data = data[x_col].values.reshape(-1, 1)
    y_data = data[y_col].values

    # Lineáris regressziós modell létrehozása
    model = LinearRegression()
    model.fit(x_data, y_data)

    # Előrejelzések kiszámítása
    y_pred = model.predict(x_data)

    # Logaritmikus megjelenítéshez: kis értékek lecserélése 1-re
    y_data = np.where(y_data <= 0, 1, y_data)  # Negatív vagy 0 értékeket lecseréljük 1-re
    y_pred = np.where(y_pred <= 0, 1, y_pred)

    # Diagram létrehozása - mérete-
    fig, ax = plt.subplots(figsize=(15, 9))

    # Hozz létre egy kezdeti, láthatatlan jelmagyarázati elemet, hogy legyen legend
    ax.plot([], [], color='none', label='')

    # Ciklus az adatokhoz
    for i in range(len(data)):
        regio = data["Régió"].iloc[i]
        style = megyek.get(regio, default_style)

        # Ellenőrizze, hogy a címke már szerepel-e a jelmagyarázatban
        legend = ax.get_legend()
        if legend is None or not any(label.get_text() == regio for label in legend.get_texts()):

            ax.scatter(x_data[i], y_data[i], color=style["color"], marker=style["marker"], s=100, label=regio)
        else:
            ax.scatter(x_data[i], y_data[i], color=style["color"], marker=style["marker"], s=100)

    # Regressziós vonal hozzáadása
    ax.plot(x_data, y_pred, color='red', label='Linear Regression', linewidth=2)

    # Y tengely logaritmikus skálára állítása
    ax.set_yscale('log')
    ax.set_title('Az energiafogyasztás és a gyümölcstermelés kapcsolata', fontsize=16, fontweight='bold')
    ax.set_xlabel('Átlagos energiafogyasztás (kWh)', fontsize=14)
    ax.set_ylabel('Átlagos gyümölcstermés (tonna)', fontsize=14)

    # Egyedi jelmagyarázat hozzáadása
    handles, labels = ax.get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))  # Egyedi címkék kiszűrése
    ax.legend(unique_labels.values(), unique_labels.keys(), loc='upper right', fontsize=10, frameon=True)

    # Diagram mentése
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close(fig)


# Save the regression chart
diagram_path = os.path.join('app', 'static', 'images', 'regression_chart.png')
generate_regression_chart_data_and_plot(
    data=osszekapcsolt_adatok,
    x_col='Éves energiafogyasztás',
    y_col='Éves gyümölcstermelés',
    output_path=diagram_path
)
