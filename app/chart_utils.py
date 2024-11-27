from app.data_processing.line_chart_data import get_line_chart_data
from app.data_processing.bar_chart_data import get_bar_chart_data
import matplotlib.pyplot as plt
from app.data_processing.regression_chart_data import osszekapcsolt_adatok, generate_regression_chart_data_and_plot


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
    output_path = 'app/static/images/regression_chart.png'
    generate_regression_chart_data_and_plot(
        data=osszekapcsolt_adatok,
        x_col=osszekapcsolt_adatok.columns[-2],  # Energiafogyasztás column
        y_col=osszekapcsolt_adatok.columns[-1],  # Gyümölcstermelés column
        output_path=output_path
    )