from flask import render_template
from app.chart_utils import create_line_chart, create_bar_chart, create_regression_chart

# Rout-ok regisztrálása
def register(app):
    # Home route
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/form1')
    def form1():
        return render_template('form1.html')

    @app.route('/form2')
    def form2():
        return render_template('form2.html')

    @app.route('/form3')
    def form3():
        return render_template('form3.html')

    @app.route('/line_chart')
    def line_chart():
        create_line_chart()
        return render_template('line_chart.html')

    @app.route('/bar_chart')
    def bar_chart():
        create_bar_chart()
        return render_template('bar_chart.html')

    @app.route('/regression_chart')
    def regression_chart():
        create_regression_chart()
        return render_template('regression_chart.html')