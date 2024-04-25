# Getting started

## 1. Introdução:

Agora vamos começar mostrar um pouco das funcionalidades do netboxcli,
sendo este um guia básico para começar a usar a biblioteca iremos ver como instalar, configurar e autenticar com o NetBox, 
alem de exemplos básicos de como criar, listar, atualizar e deletar sites no NetBox, como exemplos de tratamento de erros e exceções.

## 2. Configuração do Ambiente de Desenvolvimento:

Para começar a desenvolver com a biblioteca netboxcli, você precisa configurar seu ambiente de desenvolvimento. Aqui estão algumas etapas para ajudá-lo a começar: <a href="https://pypi.org/project/netboxcli/" target="_blanck">Página no PiP</a>

comando para instalar o pacote via terminal.

Windows:
<!-- termynal -->

```
> pip install netboxcli
---> 100%
Successfully installed netboxcli
```

Linux/MacOS:
<!-- termynal -->

```
$ pip install netboxcli
---> 100%
Successfully installed netboxcli
```

## 3. Autenticação com o netboxcli:

Para começar a interagir com o NetBox, você precisa autenticar seu cliente netboxcli com o servidor NetBox. 
Para isso, você precisa fornecer a URL do servidor NetBox e um token de API válido, 
mais informações sobre como conseguir o token consulte a <a href="https://docs.netbox.dev/en/stable/administration/permissions/#user-token" target="_blanck" title="Documentação Oficial">documentação oficial.</a>

Aqui está um exemplo de como fazer isso:

Acesse o NetBox e vá para a seção **Admin > API Tokens**.
Clique em **Add** para criar um novo token de API.
Digite um nome para o token e clique em **Save**.

exemplo interativo: <a href="https://demo.netbox.dev/users/tokens/" target="_black" title="Netbox Demo">Netbox Demo.</a>

!!! note
    - Credenciais de aceso:
    - username: netboxcli
    - password: netboxcli

agora vamos criar um objeto netboxcli e autenticar com o servidor NetBox.

```py linenums="1"
from netboxcli import Client

nb = Client('http://<url>:<port>', '<token>')
```
- **URL:** substitua `<url>:<port>` pelo endereço IP e porta do seu servidor NetBox.
- **Token:** substitua `<token>` pelo seu token de API.

## 4. Uso Básico:

No geral todas as funções da biblioteca seguem o mesmo padrão de uso, onde a orgem de classes a serem chamados seguem o 
padrão de disposição e nomes da inteface do Netbox para facilitar o uso.

a forma de usar os metodos são os mesmos para todas as classes, mudando somente as `fields` que são aceitos para cada classe.
para saber mais sobre as `fields` aceitos para cada classe consulte o <a href="https://demo.netbox.dev/dcim/sites/import/" target="_black" title="Netbox Demo">Netbox Demo.</a>


!!! info 
    - as informacoes sobre os `fields` pode ser encontrada na opção de import de cada classe na demo do netbox

### 1. Criando um site:

Um dos exemplos mais simples de uso da biblioteca é a criação de um novo objeto dentro do netbox como um site,
nesse exemplo vamos criar um site chamado `organization-1` com status `active`.

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

site = {
    "name": "organization-1",
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

!!! info
    - a função `create()` aceita também uma lista de dicionários para criar mais de um site por vez
    
### 2. Listando todos os sites:

Outro exemplo simples é listar todos os sites cadastrados no NetBox.

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
Data:  {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 2, 'url': 'http://localhost:8000/api/dcim/sites/2/', 'display': 'organization-1',...]}
```
O Retorno da função vem no formato de um dicionário com duas chaves, onde:

- **Status:** retorna o código de status da requisição HTTP (por exemplo, 200 para OK, 404 para não encontrado, etc.).
- **Data:** retorna um objeto JSON com os detalhes dos sites encontrados.

!!! note
    - O método `get()` sem argumentos retorna todos os sites cadastrados no NetBox em uma lista dentro da Data
    - para pegar somente a lista use `result['data']['results']`

!!! info
    - a função `get()` aceita argumentos para filtrar os resultados, como `id`, `name`, `[tags]`,`search` e `limit` 
    - mais informações sobre os argumentos podem ser encontradas na [Organization.sites](client/organization/sites.md)

### 3. Atualizando um site:

Agora vamos atualizar o site criado anteriormente, alterando o status para `planned` e adicionando uma descrição.

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

site = {
    "id": 2, # site id e obrigatorio para atualizar em todos
    "name": "organization-1",
    "slug": "organization-1",
    "status": "planned",
    "description": "This is a test site",
}

# Atualizando o site ele deve ser passado como uma lista de dicionarios pois a função aceita mais de uma alteração por vez
result = nb.organization.sites.update([site])

print('Status: ', result['status'])
print('Data: ', result['data'])
```
resultado esperado:

<!-- termynal -->

```
$ python example.py

Status:  200
Data:  [{'id': 2, 'url': 'http://localhost:8000/api/dcim/sites/2/', 'display': 'organization-1', 'name': 'organization-1', 'slug': 'organization-1',...}]
```

O Retorno da função vem no formato de um dicionário com duas chaves, onde:

- **Status:** retorna o código de status da requisição HTTP (por exemplo, 200 para OK, 404 para não encontrado, etc.).
- **Data:** retorna uma lista de objetos JSON com os detalhes dos sites atualizados.

### 4. Deletando um site:

Por fim, vamos deletar o site criado anteriormente.

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

# passamos o id do site que deseja deletar

result = nb.organization.sites.delete(1)

print('Status: ', result['status'])
print('Data: ', result['data'])
```

resultado esperado:

<!-- termynal -->

```
$ python example.py

Status:  204
Data:  
```

!!! warning
    - O método `delete()` não tem verificação de confirmação, então tenha certeza que deseja deletar o site antes de chamar a função

O Retorno da função vem no formato de um dicionário com duas chaves, onde:

- **Status:** retorna o código de status da requisição HTTP (por exemplo, 204 para deletado, 404 para não encontrado, etc.).
- **Data:** retorna um objeto JSON vazio, indicando que o site foi deletado com sucesso.

## 5. Tratamento de Erros e Exceções:

O netboxcli fornece tratamento de erros e exceções para lidar com situações inesperadas durante a interação com o NetBox, 
onde os erros são sempre retornados no formato de um dicionário com duas chaves, onde:

- **Status:** retorna o código de status da requisição HTTP (por exemplo, 400 para erro de requisição, 404 para não encontrado, etc.).
- **Data:** retorna um objeto JSON com detalhes do erro, como mensagem de erro e informações adicionais.

logo para trarar os erros basta fazer um tratamento de exceção considerando o codigo de status retornado.

Os códigos de status mais comuns são:

| Error code | nome                  | descrição                  | causa                                     |
|------------|-----------------------|----------------------------|-------------------------------------------|
| 0          | Internal error        | Erro interno da requisição | Parametro incorreto, ou tipagem diferente |
| 400        | Bad request           | erro na requisição         | Falta de argumentos                       |               
| 401        | Unauthorized          | Acesso não autorizado      | sem permisão para acesso ao endereço      |
| 403        | Forbidden             | Acesso negado              | Token invalido ou sem permisão            |
| 404        | Not found             | Recurso não encontrado     | ID ou recurso não encontrado              |
| 500        | Internal server error | Erro interno do servidor   | Erro interno do servidor                  |

Aqui temos um exemplo simples de uma tentativa de criar um device com um campo obrigatório faltando.

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

result = nb.organization.sites.create({'name': 'Site 1'})

if result['status'] != 201:
    print(f'Error: {result} : {result["data"]}')
```

resultado:

<!-- termynal -->

```
$ python example.py

Error: {'status': 400, 'data': '{"device_type":["This field is required."],"role":["This field is required."],"site":["This field is required."]}'} : {"device_type":["This field is required."],"role":["This field is required."],"site":["This field is required."]}
```

Agora um exemplo de tentativa de criar o mesmo site com um token sem permisão.

```py linenums="1"
from netboxcli import Client

nb = Client('http://localhost:8000', 'token')

result = nb.organization.sites.create({'name': 'Site 1'})

if result['status'] != 201:
    print(f'Error: {result} : {result["data"]}')
```
Resultado:

<!-- termynal -->

```
$ python example.py

Error: {'status': 403, 'data': '{"detail":"You do not have permission to perform this action."}'} : {"detail":"You do not have permission to perform this action."}
```

!!! info
    - Para mais informações sobre os códigos de status e mensagens de erro, consulte a pagina <a href="https://www.httpstatus.com.br" target="_blank" title="httpstatus">httpStatus</a>



## 6. Avançando com a Biblioteca:

Agora que você já sabe como criar, listar, atualizar e deletar sites no NetBox usando a biblioteca netboxcli, você pode explorar outras funcionalidades e classes disponíveis.
no qual pode ser encontrado na [Documetação](client/index.md)

