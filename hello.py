# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

# rota principal
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><h2>Disciplina PTBDSWS</h2>'

# rota com variável na URL
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

# rota de contexto de requisição
@app.route('/contextorequisicao')
def contexto_requisicao():

    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

# rota com código de status HTTP diferente
@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    # retorna uma mensagem de erro e o código HTTP 400
    return '<h1>Bad request</h1>', 400

# Rota usando objeto de resposta para criar um cookie
@app.route('/objetoresposta')
def objeto_resposta():
    # resposta personalizada para embutir um cookie
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('meu_cookie', 'valor_do_cookie')
    return response

# rota de redirecionamento
@app.route('/redirecionamento')
def redirecionamento():
    # redireciona para o site do IF
    return redirect('https://ptb.ifsp.edu.br')

# rota para abortar a requisição
@app.route('/abortar')
def abortar():
    # força um erro 404
    abort(404)