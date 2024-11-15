from flask import render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data for the charts
data = {'Date': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05'],
        'Value': [200, 250, 220, 270, 260]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Date_ordinal'] = df['Date'].map(pd.Timestamp.toordinal)

# Register the routes
def register(app):
    # Home route
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/form1')
    def form1():
        # Az első form tartalma
        return '''
            <style>
                a:link, a:visited {
                    background-color: black;
                    color: white;
                    padding: 10px 20px;
                    font-size: 24px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 10px;
                }
                a:hover, a:active {
                    background-color: grey;
                }
            </style>
            <h1>Első Form</h1>
            <img src="/static/images/intro_1.png" alt="Intro 1 kép"width="500" height="500">
            <p>Ez az első oldal tartalma...</p>
            <a href="/form2">Következő oldal</a>
        '''

    @app.route('/form2')
    def form2():
        # A második form tartalma
        return '''
            <style>
                a:link, a:visited {
                    background-color: black;
                    color: white;
                    padding: 10px 20px;
                    font-size: 24px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 10px;
                }
                a:hover, a:active {
                    background-color: grey;
                }
            </style>
            <h1>Második Form</h1>
            <img src="/static/images/intro_2.png" alt="Intro 2 kép">
            <p>Ez a második oldal tartalma...</p>
            <a href="/form3">Következő oldal</a>
        '''

    @app.route('/form3')
    def form3():
        # A harmadik form tartalma
        return '''
            <style>
                a:link, a:visited {
                    background-color: black;
                    color: white;
                    padding: 10px 20px;
                    font-size: 24px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 10px;
                }
                a:hover, a:active {
                    background-color: grey;
                }
            </style>
            <h1>Harmadik Form</h1>
            <div style="position: absolute; top: 24%; left: 23%; transform: translate(-50%, -50%); width: 150px; text-align: center; font-family: Arial, sans-serif; padding: 10px; border-radius: 10px;">
                <p style="font-size: 18px; margin: 0; color:black;">Nézünk fogyasztási adatokat?</p>
            </div>
            <img src="/static/images/intro_3.png" alt="Intro 3 kép">
            <p>Ez a harmadik oldal tartalma...</p>
            <!--<a href="/jump_form">Következő oldal</a>-->
            <a href="/form4">Következő oldal</a>
        '''

    # Form route for charts
    @app.route('/form4')
    def form4():
        return '''
            <style>
                a:link, a:visited {
                    background-color: black;
                    color: white;
                    padding: 10px 20px;
                    font-size: 24px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    border-radius: 10px;
                }
                a:hover, a:active {
                    background-color: grey;
                }
            </style>
            <h2>Az adatok a KSH adatbázisából valók!</h2>
            <a href="/line_chart">Vonal diagram</a>
            <a href="/bar_chart">Oszlop diagram</a>
            <a href="/regression_chart">Lineáris regresszió</a>
            <a href="/">Vissza a kezdőoldalra</a>
        '''

    @app.route('/line_chart')
    def line_chart():
        fig, ax = plt.subplots()
        ax.plot(df['Date'], df['Value'], marker='o', color='b')
        ax.set_title('Energiafelhasználás Időbeli Alakulása - Vonal Diagram')
        ax.set_xlabel('Idő')
        ax.set_ylabel('Érték')
        fig.savefig('app/static/images/line_chart.png')  # Save in app/static
        plt.close(fig)
        return '''
            <h1>Vonal diagram</h1>
            <img src="/static/images/line_chart.png" alt="Vonal diagram">  <!-- Use /static/images/... -->
            <a href="/form4">Vissza</a>
        '''

    # Bar chart route
    @app.route('/bar_chart')
    def bar_chart():
        fig, ax = plt.subplots()
        ax.bar(df['Date'].dt.strftime('%Y-%m'), df['Value'], color='skyblue')
        ax.set_title('Energiafelhasználás Időbeli Alakulása - Oszlop Diagram')
        ax.set_xlabel('Idő')
        ax.set_ylabel('Érték')
        fig.savefig('app/static/images/bar_chart.png')
        plt.close(fig)
        return '''
            <h1>Oszlop diagram</h1>
            <img src="/static/images/bar_chart.png" alt="Oszlop diagram">
            <a href="/form4">Vissza</a>
        '''

    # Regression chart route
    @app.route('/regression_chart')
    def regression_chart():
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
        return '''
            <h1>Lineáris regresszió</h1>
            <img src="/static/images/regression_chart.png" alt="Lineáris regresszió diagram">
            <a href="/form4">Vissza</a>
        '''
