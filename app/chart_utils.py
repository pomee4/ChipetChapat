from app.data_processing.line_chart_data import get_line_chart_data
from app.data_processing.bar_chart_data import get_bar_chart_data
import matplotlib.pyplot as plt
from app.data_processing.regression_chart_data import osszekapcsolt_adatok, generate_regression_chart_data_and_plot


def create_line_chart():
    df = get_line_chart_data()


def create_bar_chart():
    df = get_bar_chart_data()


def create_regression_chart():
    generate_regression_chart_data_and_plot(
        data=osszekapcsolt_adatok,
        x_col=osszekapcsolt_adatok.columns[-2],  # Energiafogyasztás column
        y_col=osszekapcsolt_adatok.columns[-1],  # Gyümölcstermelés column
        output_path='app/static/images/regression_chart.png'
    )