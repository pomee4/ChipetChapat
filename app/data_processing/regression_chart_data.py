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
kor0068.rename(columns={"Budapest": "Terület", "fõváros, régió": "Területtípus"}, inplace=True)
mez0086.rename(columns={"Budapest": "Terület", "fõváros, régió": "Területtípus"}, inplace=True)

# Függvény az adatok tisztítására: elválasztók eltávolítása, érvénytelen értékek kezelése, numerikus átalakítás
def tisztit_adatok_nelkul(df):
    tisztitott_df = df.copy()
    for oszlop in tisztitott_df.columns[2:]:  # Az első két oszlopot kihagyjuk (Terület neve és típus)
        tisztitott_df[oszlop] = (
            tisztitott_df[oszlop]
            .astype(str)  # Az összes bejegyzést stringgé alakítjuk a cseréhez
            .str.replace(r"[ ,]", "", regex=True)  # Szóközök és vesszők eltávolítása
            .str.replace(r"[^\d.-]", "", regex=True)  # Nem numerikus karakterek eltávolítása
            .replace("", "NaN")  # Üres karakterláncok cseréje "NaN"-re
            .astype(float)  # Numerikus értékké alakítás
        )
    return tisztitott_df

# Adatok tisztítása
kor0068_tisztitott = tisztit_adatok_nelkul(kor0068)
mez0086_tisztitott = tisztit_adatok_nelkul(mez0086)

# Adatok összekapcsolása a "Terület" oszlop alapján
osszekapcsolt_adatok = pd.merge(
    kor0068_tisztitott, mez0086_tisztitott, on="Terület", suffixes=('_energia', '_gyümölcs')
)

# Adatok kinyerése a legfrissebb évhez (az utolsó oszlopok)
energia_fogyasztas = osszekapcsolt_adatok.iloc[:, -2]  # Második utolsó oszlop az energia adatokhoz
gyumolcstermeles = osszekapcsolt_adatok.iloc[:, -1]  # Utolsó oszlop a gyümölcs adatokhoz

# Szórásdiagram megrajzolása
plt.figure(figsize=(10, 6))
plt.scatter(energia_fogyasztas, gyumolcstermeles, alpha=0.7)
plt.title("Szórásdiagram: Energiafogyasztás és Gyümölcstermelés kapcsolata")
plt.xlabel("Energiefogyasztás (legfrissebb év)")
plt.ylabel("Gyümölcstermelés (legfrissebb év)")
plt.grid(True)

# Kiválasztjuk a legfrissebb év adatait
energia_fogyasztas = osszekapcsolt_adatok.iloc[:, -2]  # Második utolsó oszlop az energia adatokhoz
gyumolcstermeles = osszekapcsolt_adatok.iloc[:, -1]  # Utolsó oszlop a gyümölcs adatokhoz

# Lineáris regressziós modell létrehozása
X = energia_fogyasztas.values.reshape(-1, 1)  # Energiafogyasztás mint bemenet
y = gyumolcstermeles.values  # Gyümölcstermelés mint kimenet
model = LinearRegression()
model.fit(X, y)
# Előrejelzések kiszámítása
y_pred = model.predict(X)
# Diagram elkészítése
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(energia_fogyasztas, gyumolcstermeles, color='blue', label='Eredeti Adatok')
ax.plot(energia_fogyasztas, y_pred, color='red', label='Lineáris Regresszió')
ax.set_title('Lineáris Regresszió: Energiafogyasztás és Gyümölcstermelés Kapcsolata')
ax.set_xlabel('Energiefogyasztás (legfrissebb év)')
ax.set_ylabel('Gyümölcstermelés (legfrissebb év)')
ax.legend()

### Write current dir to console
print("Current directory is: "+os.getcwd())
#Print subdirs to console
print([name for name in os.listdir('.') if os.path.isdir(name)])

# Define the path for saving the diagram
diagram_path = os.path.join('app', 'static', 'images', 'regression_chart.png')
# Create the directories if they don't exist
os.makedirs(os.path.dirname(diagram_path), exist_ok=True)
# Save the figure
fig.savefig(diagram_path)
plt.close(fig)
