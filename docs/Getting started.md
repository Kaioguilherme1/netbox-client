# Getting started

- Breve visão geral do NetBox, uma plataforma open-source para gestão de infraestrutura IP.
- Explicação sobre a API RESTful do NetBox, que permite interagir com os dados e funcionalidades do NetBox programaticamente.

## 2. Configuração do Ambiente de Desenvolvimento:

- Instruções para configurar um ambiente de desenvolvimento, incluindo a instalação de Python e outras dependências necessárias.

## 3. Autenticação com o netboxcli:

- Explicação sobre os diferentes métodos de autenticação suportados pelo NetBox API (por exemplo, token de acesso, autenticação básica).
- Instruções para obter as credenciais de autenticação necessárias para interagir com a API.

## 4. Uso Básico:

- Demonstração de como realizar operações simples, como recuperar informações de dispositivos, endereços IP, VLANs, etc.
- Códigos de exemplo em Python para mostrar como fazer requisições HTTP para a API do NetBox e manipular as respostas.

### 1. Criando um site:

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

site = {
    "name": "organization-1",
    "status": "active",
}

result = nb.organization.sites.create(site)

print('Status: ', result['status'])
print('Data: ', result['data'])
```

resultado esperado:

<!-- termynal -->

```
$ python example.py

Status:  201
Data:  {"id":1,"url":"http://localhost:8000/api/dcim/sites/2/","display":"organization-1","name":"organization-1"...}

```

O Retorno da função vem no formato de um dicionário com duas chaves, onde:

- **Status:** retorna o código de status da requisição HTTP (por exemplo, 201 para criado, 404 para não encontrado, etc.).
- **Data:** retorna um objeto JSON com os detalhes do site criado.

### 2. Listando todos os sites:

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

result = nb.organization.sites.get()

print('Status: ', result['status'])
print('Data: ', result['data'])

```

resultado esperado:

<!-- termynal -->

```
$ python example.py
Status:  200
Data:  {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 2, 'url': 'http://192.168.20.3:8000/api/dcim/sites/2/', 'display': 'organization-1',...]}
```
O Retorno da função vem no formato de um dicionário com duas chaves, onde:

- **Status:** retorna o código de status da requisição HTTP (por exemplo, 200 para OK, 404 para não encontrado, etc.).
- **Data:** retorna um objeto JSON com os detalhes dos sites encontrados.

!!! note
    - O método `get()` sem argumentos retorna todos os sites cadastrados no NetBox em uma lista dentro da Data
    - para pegar somente a lista use `result['data']['results']`

!!! info
    - a função `get()` aceita argumentos para filtrar os resultados, como `id`, `name`, `[tags]`,`search` e `limit` 
    - mais informações sobre os argumentos podem ser encontradas na [Organization.sites](/Client/organization/sites/)

### 3. Atualizando um site:

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

site = {
    "id": 1, # site id e obrigatorio para atualizar
    "status": "planned",
    "description": "This is a test site",
}

result = nb.organization.sites.update()

print('Status: ', result['status'])
print('Data: ', result['data'])
```
resultado esperado:

<!-- termynal -->

```
$ python example.py




## 5. Tratamento de Erros e Exceções:

- Orientações sobre como lidar com possíveis erros e exceções que podem ocorrer durante o uso da biblioteca.
- Sugestões sobre como implementar tratamentos adequados de erros para garantir a robustez do código.

## 6. Avançando com a Biblioteca:

- Exploração de recursos avançados oferecidos pela biblioteca, como paginação, filtros e ordenação de resultados.
- Exemplos mais complexos de uso da API para realizar operações como criação, atualização e exclusão de objetos no NetBox.

## 7. Recursos Adicionais:

- Links para a documentação oficial do NetBox API para referência adicional.
- Sugestões de outros recursos, como fóruns de discussão, grupos de usuários ou comunidades online, onde os desenvolvedores podem buscar suporte e compartilhar conhecimento.

