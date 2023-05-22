from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)


#Localiza o Banco de dados

app.config['MYSQL_Host'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == 'POST':

        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor() #Conecta Com a Base de Dados
        cur.execute('INSERT INTO contatos (email,assunto,descricao) VALUES (%s, %s, %s)', (email, assunto, descricao)) #Executa Linha no "MySQL Workbench"

        mysql.connection.commit()

        cur.close() #Desconecta da Base de Dados
        return 'Concluido'
    return render_template('contatos.html')


@app.route('/user')
def user():
    cur = mysql.connection.cursor()

    conta = cur.execute('select * from contatos')

    if conta > 0:

        userdata = cur.fetchall()

        return render_template('user.html', userdata = userdata)

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

app.run(debug=True)