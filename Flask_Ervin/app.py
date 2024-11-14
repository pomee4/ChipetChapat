from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Adatok beállítása (globális változóként használjuk őket)
data = {'Date': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05'],
        'Value': [200, 250, 220, 270, 260]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Date_ordinal'] = df['Date'].map(pd.Timestamp.toordinal)

@app.route('/')
def home():
    # Kezdőképernyő tartalma
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
        <h1>Chipet-Chapat projekt munka v1.0</h1>
        <p>Üdvözölünk a projektünkben!</p>
        <br>
        <h2>Csapattagok:</h2>
        <p>Balogh Léna - ECTPM2</p>
        <p>Kiss G. Ervin - H9ETGN</p>
        <p>Kovács Tamás - IYWXUK</p>
        <br>
        <a href="/form1">Következő oldal</a>
    '''

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
        <img src="/static/intro_1.png" alt="Intro 1 kép"width="500" height="500">
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
        <img src="/static/intro_2.png" alt="Intro 2 kép">
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
        <img src="/static/intro_3.png" alt="Intro 3 kép">
        <p>Ez a harmadik oldal tartalma...</p>
        <!--<a href="/jump_form">Következő oldal</a>-->
        <a href="/form4">Következő oldal</a>
    '''
"""
@app.route('/jump_form')
def jump_form():
    # Az utolsó form tartalma
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
        <h1>Utolsó Form</h1>
        <p>Ez az utolsó form tartalma...</p>
        <p><strong>Gratulálok, elérted az utolsó formot!</strong></p>
        <a href="/">Vissza a kezdőoldalra</a>
    '''
"""
# Negyedik oldal, ahol a gombok találhatók
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

# Vonal diagram oldala
@app.route('/line_chart')
def line_chart():
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Value'], marker='o', color='b')
    ax.set_title('Energiafelhasználás Időbeli Alakulása - Vonal Diagram')
    ax.set_xlabel('Idő')
    ax.set_ylabel('Érték')
    fig.savefig('static/line_chart.png')  # Mentés a static mappába
    plt.close(fig)
    return '''
        <h1>Vonal diagram</h1>
        <img src="/static/line_chart.png" alt="Vonal diagram">
        <a href="/form4">Vissza</a>
    '''

# Oszlop diagram oldala
@app.route('/bar_chart')
def bar_chart():
    fig, ax = plt.subplots()
    ax.bar(df['Date'].dt.strftime('%Y-%m'), df['Value'], color='skyblue')
    ax.set_title('Energiafelhasználás Időbeli Alakulása - Oszlop Diagram')
    ax.set_xlabel('Idő')
    ax.set_ylabel('Érték')
    fig.savefig('static/bar_chart.png')  # Mentés a static mappába
    plt.close(fig)
    return '''
        <h1>Oszlop diagram</h1>
        <img src="/static/bar_chart.png" alt="Oszlop diagram">
        <a href="/form4">Vissza</a>
    '''

# Lineáris regresszió diagram oldala
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
    fig.savefig('static/regression_chart.png')  # Mentés a static mappába
    plt.close(fig)
    return '''
        <h1>Lineáris regresszió</h1>
        <img src="/static/regression_chart.png" alt="Lineáris regresszió diagram">
        <a href="/form4">Vissza</a>
    '''


if __name__ == '__main__':
    app.run(debug=True)