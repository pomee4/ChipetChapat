from flask import render_template

#regisztráljuk az összes útvonalat az app objektumhoz
def register(app):
    # Főoldal útvonal
    @app.route('/')
    def home():
        # Visszatérünk a home.html sablonnal
        return render_template('home.html')
