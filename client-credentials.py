# -*- coding: utf-8 -*-
import requests
import json

URL_BASE_AUTENTICACAO = 'https://autenticacao.info.ufrn.br/'
client_id = '<CLIENT_ID>'
client_secret = '<CLIENT_SECRET>'

URL_BASE = 'https://api.info.ufrn.br/'
VERSION = '<VERSION_API>'
x_api_key = '<X-API-KEY>'

#injetando parametros na url
url_token = URL_BASE_AUTENTICACAO + 'authz-server/oauth/token?client_id={0}&client_secret={1}&grant_type=client_credentials'.format(client_id, client_secret)

#efetuando uma requisicao a api passando a url como parametro
requisicao_token = requests.post(url_token)

#convertendo a resposta json em um objeto python
resposta = json.loads(requisicao_token.content)

#imprimindo resultado da requisição
print('RESPOSTA TOKEN: \n'+ str(resposta)) #é possivel acessar campos em especifico com #'resposta['campo_que_deseja']'

#salvamos o token em uma variavel pra usar em um exemplo de chamada a api
token = resposta['access_token']

#montamos a url de projetos injetando o token como parametro
URL = URL_BASE + 'curso/' + VERSION + '/modalidades-educacao'

headers = {'Authorization': 'bearer ' + token, 'x-api-key': x_api_key}


#agora como exemplo fazemos uma requisicao aos projetos de pesquisa com o token obtido
requisicao_projetos = requests.get(URL, headers=headers)


#convertemos a resposta para json
projetos = json.loads(requisicao_projetos.content)

#imprimimos o resultado da api de projetos, e possivel acessar campos em especifico com 'resposta['campo_que_deseja']'
print('PROJETOS: \n'+ str(projetos))
