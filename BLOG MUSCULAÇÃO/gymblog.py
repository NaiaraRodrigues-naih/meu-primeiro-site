
from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Página sobre academia, nutrição e suplementação
@app.route('/academia')
def academia():
    return render_template('academia.html')

# Página sobre treino de superiores
@app.route('/treinodesuperior')
def treino_superior():
    return render_template('treinodesuperior.html')

# Página sobre treino de posteriores
@app.route('/treinodeposterior')
def treino_posterior():
    return render_template('treinodeposterior.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


if __name__ == '__main__':
    app.run(debug=True)
