# Netbox Client


[![Documentation Status](https://readthedocs.org/projects/netboxcli/badge/?version=latest)](https://netboxcli.readthedocs.io/pt/latest/?badge=latest)
[![pipeline](https://github.com/Kaioguilherme1/netbox-client/actions/workflows/pipeline.yml/badge.svg?branch=main)](https://github.com/Kaioguilherme1/netbox-client/actions/workflows/pipeline.yml)
[![codecov](https://codecov.io/gh/Kaioguilherme1/netbox-client/graph/badge.svg?token=LMD2ILTE1N)](https://codecov.io/gh/Kaioguilherme1/netbox-client)
[![PyPI version](https://badge.fury.io/py/netboxcli.svg)](https://badge.fury.io/py/netboxcli)
---

  O NetboxCli é um pacote Python projetado para simplificar e agilizar a interação com o NetBox, 
  uma popular plataforma de gerenciamento de infraestrutura de rede de código aberto. 
  Com este pacote, você pode facilmente interagir com as funcionalidades do NetBox, 
  como gerenciamento de endereços IP (IPAM) e virtualização.

## Índice
* [Netbox Client](#netbox-client)
* [📄Dependências](#Dependências)
* [🔧Instalação](#Instalação)
* [🚀 Getting Started](https://netboxcli.readthedocs.io/pt/latest/Getting%20started/)
* [📝Documentação](https://netboxcli.readthedocs.io/pt/latest/)
* [⚙️Uso](#uso)
* [📦Desenvolvimento](#Desenvolvimento)
* [📌Versão](#Versão)
* [👥Colaboradores](#Colaboradores)
* [✒️Autores](#Autores)
* [📑Licença](#Licença)

### Documentação Disponível [aqui](https://netboxcli.readthedocs.io/pt/latest/)
  
## 📄 Dependências 
  Lista as dependencias
  * requests
  * python 3.12 ou superior
  * [netbox >=3.7.5](https://github.com/netbox-community/netbox)

## 🔧 Instalação

```
pip install netboxcli
```

## ⚙️ uso

### Importando o Módulo e Preparando a Conexão

Antes de começar a interagir com o NetBox, você precisa importar o módulo `netboxcli` e criar um objeto NetBox para estabelecer a conexão com o servidor. Substitua `'sua_url_aqui'` pelo endereço IP e porta do seu servidor NetBox e `'seu_token_aqui'` pelo seu token de API.

```python
import netboxcli as nb
import json

def printj(data):
    print(json.dumps(data, indent=4))

# Criar um objeto NetBox
nb_client = nb.Client('sua_url_aqui', 'seu_token_aqui')

```

### Utilizando Classes Finais Padrão

Todas as classes finais no NetboxCli têm os mesmos nomes que as classes do NetBox por padrão. Isso facilita a navegação e a familiarização com a estrutura. Aqui estão alguns exemplos de como você pode usar essas classes e seus métodos padronizados:

### Exemplo de IPAM: Criar um Novo Bloco de Endereços IP

```python
# Exemplo de criação de um novo bloco de endereços IP
ip_block_data = {
    "prefix": "192.168.10.0/24",
    "description": "Bloco de IPs para Servidores",
    "vlan": 100
}

new_ip_block = nb_client.ipam.prefixes.create(ip_block_data)

```

### Exemplo de Virtualização: Obter uma Máquina Virtual por ID

```python
# Exemplo de obtenção de uma máquina virtual por ID
vm_by_id = nb_client.virtualization.virtual_machines.get(id=1)

```

### Exemplo de IPAM: Atualizar um Bloco de Endereços IP

```python
# Exemplo de atualização de um bloco de endereços IP
updated_ip_block_data = {
    "id": 1,
    "description": "Novo Descrição para o Bloco de IPs"
}

updated_ip_block = nb_client.ipam.prefixes.update(updated_ip_block_data)

```

### Exemplo de Virtualização: Excluir uma Máquina Virtual

```python
# Exemplo de exclusão de uma máquina virtual pelo ID
deleted_vm_id = nb_client.virtualization.virtual_machines.delete(id=1)

```
para mais exemplos de uso acesse a [documentação](https://netboxcli.readthedocs.io/pt/latest/Getting%20started/)

### Personalizando e Extendendo

Além das operações básicas, você pode personalizar e estender as funcionalidades do NetboxCli de acordo com suas necessidades específicas. As classes finais oferecem uma base sólida para construir interações mais avançadas com a API do NetBox.

Lembre-se de substituir os exemplos de dados e IDs pelos valores reais correspondentes ao seu ambiente NetBox.

### Objetivo

O objetivo do projeto NetboxCli é fornecer uma interface Python simples e eficiente para interagir com o NetBox. 
oferecendo uma alternativa conveniente para os administradores de rede que desejam automatizar tarefas e gerenciar recursos de infraestrutura de maneira mais fácil.

## Checklist de Desenvolvimento

Aqui está um checklist do que está atualmente disponível no NetboxCli e do que será adicionado no futuro:

- [x]  **Organization:** Gerencie informações sobre organizações e empresas associadas aos seus recursos de rede.
- [x]  **Devices:** Acesse e gerencie dispositivos de rede, incluindo servidores, roteadores e switches.
- [x]  **Connections:** Interaja com conexões físicas e lógicas entre dispositivos de rede.
- [x]  **Wireless:** Gerencie redes sem fio, pontos de acesso e configurações de Wi-Fi.
- [x]  **IPAM:** Simplifique a gestão de blocos de endereços IP, facilitando a adição, recuperação e atualização.
- [x]  **Vpn:** Suporte para redes de sobreposição, como VPNs e túneis.
- [x]  **Virtualização:** Gerencie máquinas virtuais de maneira eficaz, desde a criação até a exclusão.
- [x]  **Circuits:** Gerencie circuitos de rede, como conexões de fibra óptica e links externos.
- [x]  **Power:** Acesse informações relacionadas ao fornecimento de energia e energia de seus dispositivos.
- [x]  **Provisioning:** Suporte para provisionamento de rede, incluindo configurações de DHCP e DNS.
- [x]  **Customization:** Gerencie modelos e configurações personalizadas para seus dispositivos de rede.
- [x]  **Operations:** Acesse e gerencie informações sobre operações de rede, como manutenção e atualizações.
- [x]  **Extras:** Integração com plugins e extensões adicionais para funcionalidades personalizadas.

Este checklist será atualizado à medida que novas funcionalidades forem implementadas. 
Agradecemos por seu interesse e paciência enquanto trabalhamos para tornar o NetboxCli mais abrangente e útil para suas necessidades de automação e gerenciamento de rede.

## 📌 Versão 1.2.0

### **Adições na Versão 1.2.0**

- **Criação de nova feature:** Criação de nova funcionalidade no metodo get que permite passar querys ultilizadas na pagína de filtro

## ✒️ Autores

* **developer** - *Initial Work* - [Kaio Guilherme](https://github.com/Kaioguilherme1)

## 📑 Licença

Esse projeto esta sob a licença(MIT) - veja o arquivo [Licenca.md](https://github.com/Kaioguilherme1/netbox-client/blob/main/Licenca) para mais detalhes.
