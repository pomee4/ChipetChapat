from app.data_processing.line_chart_data import get_line_chart_data
from app.data_processing.bar_chart_data import get_bar_chart_data
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from app.data_processing.regression_chart_data import osszekapcsolt_adatok


def create_line_chart():
    df = get_line_chart_data()
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Value'], marker='o', color='b')
    ax.set_title('Energiafelhasználás Időbeli Alakulása - Vonal Diagram')
    ax.set_xlabel('Idő')
    ax.set_ylabel('Érték')
    fig.savefig('app/static/images/line_chart.png')
    plt.close(fig)

def create_bar_chart():
    df = get_bar_chart_data()
    fig, ax = plt.subplots()
    ax.bar(df['Date'].dt.strftime('%Y-%m'), df['Value'], color='skyblue')
    ax.set_title('Energiafelhasználás Időbeli Alakulása - Oszlop Diagram')
    ax.set_xlabel('Idő')
    ax.set_ylabel('Érték')
    fig.savefig('app/static/images/bar_chart.png')
    plt.close(fig)

def create_regression_chart():
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

    # Diagram mentése
    fig.savefig('app/static/images/regression_chart.png')
    plt.close(fig)