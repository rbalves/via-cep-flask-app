from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def consulta():
    return render_template('consulta.html')

@app.route("/consultar")
def consultar():
    cep = request.args.get('cep')
    resposta = requests.get('http://viacep.com.br/ws/'+cep+'/json/')

    if resposta.status_code != 200:
        return render_template('erro.html')

    dados = json.loads(resposta.content)
    return render_template('dados.html', dados=dados)