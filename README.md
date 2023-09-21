# Netbox Client


![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
---

  O NetboxCli é um pacote Python projetado para simplificar e agilizar a interação com o NetBox, 
  uma popular plataforma de gerenciamento de infraestrutura de rede de código aberto. 
  Com este pacote, você pode facilmente interagir com as funcionalidades do NetBox, 
  como gerenciamento de endereços IP (IPAM) e virtualização.

## Índice
* [Netbox Client](#netbox-client)
* [Índice](#Índice)
* [📄Dependências](#Dependências)
* [🔧Instalação](#Instalação)
* [⚙️Uso](#uso)
* [📦Desenvolvimento](#Desenvolvimento)
* [📌Versão](#Versão)
* [👥Colaboradores](#Colaboradores)
* [✒️Autores](#Autores)
* [📑Licença](#Licença)

## 📄 Dependências 
  Lista as dependencias
  * requests
  * python 3.11 ou superior
  * [netbox](https://github.com/netbox-community/netbox)
  
## 🔧Instalação

### 📁 Acesso ao projeto

Apresentar formas de baixar seu projeto.

[Baixar projeto](https://github.com/Kaioguilherme1/netbox-client/archive/refs/heads/main.zip)
#### Baixar o pacote via terminal.
```
pip install netboxcli
```
## ⚙️ Uso

O NetboxCli é uma ferramenta poderosa para interagir com o NetBox de maneira simples e eficiente. Ele oferece classes consistentes com métodos padronizados para lidar com diversas funcionalidades, incluindo IPAM e Virtualização. Você pode navegar entre as classes da mesma forma que nas abas do NetBox. Aqui estão os passos básicos para começar a usar o NetboxCli:

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

### Personalizando e Extendendo

Além das operações básicas, você pode personalizar e estender as funcionalidades do NetboxCli de acordo com suas necessidades específicas. As classes finais oferecem uma base sólida para construir interações mais avançadas com a API do NetBox.

Lembre-se de substituir os exemplos de dados e IDs pelos valores reais correspondentes ao seu ambiente NetBox.
## 📦 Desenvolvimento

Nesta seção, você encontrará informações sobre o desenvolvimento contínuo do NetboxCli. Estamos trabalhando para expandir as funcionalidades e fornecer suporte abrangente para todas as abas disponíveis no NetBox 3.5 e versões posteriores. Atualizações e novas funcionalidades serão lançadas com o tempo, conforme o projeto evolui.

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
- [ ]  **Overlay:** Suporte para redes de sobreposição, como VPNs e túneis.
- [x]  **Virtualização:** Gerencie máquinas virtuais de maneira eficaz, desde a criação até a exclusão.
- [ ]  **Circuits:** Gerencie circuitos de rede, como conexões de fibra óptica e links externos.
- [ ]  **Power:** Acesse informações relacionadas ao fornecimento de energia e energia de seus dispositivos.
- [x]  **Extras:** Integração com plugins e extensões adicionais para funcionalidades personalizadas.

Este checklist será atualizado à medida que novas funcionalidades forem implementadas. 
Agradecemos por seu interesse e paciência enquanto trabalhamos para tornar o NetboxCli mais abrangente e útil para suas necessidades de automação e gerenciamento de rede.

## 📌 Versão 0.7.0

### **Adições na Versão 0.7.0**

- **Wireless:** Gerencie redes sem fio, pontos de acesso e configurações de Wi-Fi.



## ✒️ Autores

Mencoes dadas a todos que participaram e ajudaram no projeto desde o início

* **developer** - *Initial Work* - [Kaio Guilherme](https://github.com/Kaioguilherme1)

## 📑 Licença

Esse projeto esta sob a licença(MIT) - veja o arquivo [Licenca.md](https://github.com/Kaioguilherme1/netbox-client/blob/main/Licenca) para mais detalhes.
