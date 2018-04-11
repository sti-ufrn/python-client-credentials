Esse fluxo foi implementado para ser usado por aplicações que queiram acessar os dados públicos dos sistemas da SINFO, tais como eventos, notícias, telefones, entre outros. 

Deste modo, aplicações que possuem esse fim devem seguir os passos abaixo:

1 - A aplicação faz uma requisição POST ao authorization server através da URL https://autenticacao.info.ufrn.br/authz-server/oauth/token, passando o client_id, client_secret e grant_type como QueryParam;

    Ex: POST https://autenticacao.info.ufrn.br/authz-server/oauth/token?client_id=AppId&client_secret=AppSecret&grant_type=client_credentials

2 - O authorization server retorna à aplicação um JSON contendo o access_token, token_type, refresh_token, expires_in e scope
Ex: { “access_token”: “111”, “token_type”: “bearer”, "refresh_token": "abcd" , “expires_in”: 7431095, “scope”: “read” }

3- Em posse dessas informações, a aplicação já pode acessar os dados disponibilizados pela API passando o token através do parâmetro Authorization e o x-api-key no header da requisição desejada;


4 - Os dados da API são retornados para a aplicação.
Ex:

```json
GET 
[
	{
		"idTelefone": 0,
		"localizacao": "string",
		"setor": "string",
		"descricao": "string",
		"numero": "string",
		"ramais": [
			{
				"numero": "string",
				"descricao": "string"
			}
		]
	}
]
```

![alt text](https://api.ufrn.br/images/client_credentials_ufrn.png)
