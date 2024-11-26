import matplotlib.pyplot as plt
from app.data_processing.line_chart_data import get_line_chart_data
from app.data_processing.bar_chart_data import get_bar_chart_data
from app.data_processing.regression_chart_data import get_regression_chart_data
from sklearn.linear_model import LinearRegression

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
    df = get_regression_chart_data()
    X = df[['Date_ordinal']]
    y = df['Value']
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(df['Date'], df['Value'], color='blue', label='Eredeti Adatok')
    ax.plot(df['Date'], y_pred, color='red', label='Lineáris Regresszió')
    ax.set_title('Lineáris Regresszió az Energiafelhasználás Időbeli Alakulására')
    ax.set_xlabel('Idő')
    ax.set_ylabel('Érték')
    ax.legend()
    fig.savefig('app/static/images/regression_chart.png')
    plt.close(fig)