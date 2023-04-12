from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

app.run(debug=True)