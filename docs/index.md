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
* [⚙️Getting started]('Getting started.md')
* [📦Desenvolvimento](#Desenvolvimento)
* [📌Versão](#Versão)
* [👥Colaboradores](#Colaboradores)
* [✒️Autores](#Autores)
* [📑Licença](#Licença)



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

- **Atualização do Documetação:** Atualização da documentação usando docstrings.
- **Adicionando CI no repositorio com github Actions:** Adicionando CI no repositorio com github Actions.
## ✒️ Autores

* **developer** - *Initial Work* - [Kaio Guilherme](https://github.com/Kaioguilherme1)

## 📑 Licença

Esse projeto esta sob a licença(MIT) - veja o arquivo [Licenca.md](https://github.com/Kaioguilherme1/netbox-client/blob/main/Licenca) para mais detalhes.
