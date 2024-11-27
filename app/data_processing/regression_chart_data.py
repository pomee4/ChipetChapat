# Adjusting the provided structure to match the requested chart and use case
import pandas as pd
import matplotlib.pyplot as plt
import os
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

# Diagram generálás és regressziós modell funkció
def generate_regression_chart_data_and_plot(data, x_col, y_col, output_path):
    x_data = data[x_col].values.reshape(-1, 1)
    y_data = data[y_col].values

    # Lineáris regressziós modell létrehozása
    model = LinearRegression()
    model.fit(x_data, y_data)

    # Előrejelzések kiszámítása
    y_pred = model.predict(x_data)

    # Diagram létrehozása
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(x_data, y_data, color='blue', s=100, label='Original Data', alpha=0.6, edgecolors='w', linewidth=0.5)
    for i in range(len(data)):
        ax.text(x_data[i], y_data[i], data["Régió"].iloc[i], fontsize=10, color='black', ha='right')
    ax.plot(x_data, y_pred, color='red', label='Linear Regression', linewidth=2)

    # Diagram formázása
    ax.set_title('Relationship between Energy Consumption and Fruit Production', fontsize=16, fontweight='bold')
    ax.set_xlabel('Average Energy Consumption (kWh)', fontsize=14)
    ax.set_ylabel('Average Fruit Production (tons)', fontsize=14)
    ax.legend()

    # Diagram mentése
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close(fig)

# Regressziós diagram generálása és mentése
diagram_path = os.path.join('app', 'static', 'images', 'regression_chart.png')
generate_regression_chart_data_and_plot(
    data=osszekapcsolt_adatok,
    x_col='Éves energiafogyasztás',
    y_col='Éves gyümölcstermelés',
    output_path=diagram_path
)
