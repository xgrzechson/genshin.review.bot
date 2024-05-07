from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pobierz ocenę postaci z formularza
        rating = request.form['rating']
        # Tutaj możesz zapisać ocenę do bazy danych lub gdzieś indziej
        return 'Dziękujemy za ocenę!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)