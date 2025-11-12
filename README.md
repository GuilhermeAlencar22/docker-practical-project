Perfeito, Guilherme 👏
Aqui está um **README profissional, atraente e técnico**, ideal para colocar na **raiz do repositório GitHub** (`README.md`) e impressionar tanto **professores** quanto **recrutadores**.
Ele apresenta seus 5 desafios de forma clara, moderna e com uma pegada de portfólio profissional — mostrando domínio em **Docker, Docker Compose, microsserviços e orquestração**.

---

# 🐳 Docker Practical Project — Desafios Completos (1 a 5)

> 🚀 Projeto prático e completo com foco em **Docker, Microsserviços e Orquestração com Compose**
> 💡 Desenvolvido por **Guilherme Alencar**

---

## 📘 Sobre o Projeto

Este repositório reúne **5 desafios práticos** que simulam cenários reais de **DevOps, backend distribuído e arquitetura de microsserviços**.
Cada desafio foi construído **do zero**, com código **100% funcional**, documentação e **containerização completa com Docker**.

O objetivo é demonstrar **competência técnica**, **organização de serviços** e **boas práticas de integração e deploy local**.

---

## 🧩 Desafios Desenvolvidos

### 🧱 **Desafio 1 — Containers e Comunicação via Rede Docker**

* Criação de **dois containers (web e client)** comunicando-se em uma **rede personalizada**.
* Uso de **scripts Bash** para automação de execução e comunicação.
* Demonstração de logs, resposta HTTP e troca de mensagens entre os containers.

🛠️ Tecnologias:
`Python`, `Flask`, `Dockerfile`, `Docker Network`, `Curl`, `Bash`

📁 Pasta: [`desafio1/`](./desafio1)

---

### 🗄️ **Desafio 2 — Banco de Dados com Docker Compose**

* Criação de um **serviço PostgreSQL** com **volume persistente**.
* Execução automática de scripts SQL de inicialização.
* Demonstração de conexão e persistência de dados em container.

🛠️ Tecnologias:
`PostgreSQL`, `Docker Compose`, `Volumes`, `SQL Init Scripts`

📁 Pasta: [`desafio2/`](./desafio2)

---

### 🔗 **Desafio 3 — Orquestração de Múltiplos Serviços**

* Uso de **Docker Compose** para orquestrar 3 serviços dependentes:

  * **Web (Flask)**
  * **DB (PostgreSQL)**
  * **Cache (Redis)**
* Configuração de variáveis de ambiente, rede interna e `depends_on`.

🛠️ Tecnologias:
`Flask`, `PostgreSQL`, `Redis`, `Docker Compose`

📁 Pasta: [`desafio3/`](./desafio3)

---

### ⚙️ **Desafio 4 — Microsserviços Independentes**

* Criação de **dois microsserviços independentes (A e B)** em Flask.
* Comunicação entre eles via **HTTP requests**.
* Containers isolados e Dockerfiles separados.

🛠️ Tecnologias:
`Flask`, `HTTP`, `Docker`, `REST API`, `Microservices`

📁 Pasta: [`desafio4/`](./desafio4)

---

### 🌐 **Desafio 5 — Microsserviços com API Gateway**

* Arquitetura com **API Gateway** centralizando dois microsserviços:

  * **Service 1:** Usuários
  * **Service 2:** Pedidos
* O **Gateway** expõe endpoints `/users` e `/orders`, integrando e orquestrando os serviços.
* Todos os serviços são executados em containers via **Docker Compose**.

🛠️ Tecnologias:
`Flask`, `Requests`, `API Gateway`, `Docker Compose`, `Microservices`

📁 Pasta: [`desafio5/`](./desafio5)

---

## 🧠 Conhecimentos Aplicados

✅ Criação e otimização de **Dockerfiles**
✅ Uso de **Docker Compose** para orquestração de múltiplos containers
✅ Configuração de **redes internas** e **variáveis de ambiente**
✅ Desenvolvimento de **microsserviços RESTful com Flask**
✅ Comunicação entre containers via **HTTP**
✅ Persistência de dados com **PostgreSQL + Volumes**
✅ Integração com **Redis (cache)**
✅ Automação de builds e execuções com scripts shell

---

## 🚀 Como Executar o Projeto

Clone o repositório:

```bash
git clone https://github.com/GuilhermeAlencar22/docker-practical-project.git
cd docker-practical-project
```

Entre em qualquer desafio e suba os serviços:

```bash
cd desafio5
docker compose up -d --build
```

Verifique os containers ativos:

```bash
docker ps
```

Teste os endpoints:

```bash
curl http://localhost:8080/users
curl http://localhost:8080/orders
```

---

## 🧩 Estrutura do Repositório

```
docker-practical-project/
│
├── desafio1/       # Comunicação entre containers (web + client)
├── desafio2/       # Banco de dados PostgreSQL com Compose
├── desafio3/       # Web + DB + Cache orquestrados
├── desafio4/       # Microsserviços independentes
├── desafio5/       # Microsserviços com API Gateway
└── README.md       # Este arquivo
```

---

## 💬 Contato

👤 **Guilherme Alencar**
📧 [guilherme@empresa.com](mailto:guilherme@empresa.com)
💼 [LinkedIn](https://www.linkedin.com/in/guilhermealencar22/)
🐙 [GitHub](https://github.com/GuilhermeAlencar22)

---

## ⭐ Reconhecimentos

Este projeto foi desenvolvido como parte de um **laboratório prático de Docker e Microsserviços**, focado em consolidar os conceitos de:

* **containerização**,
* **isolamento de serviços**,
* **orquestração** e
* **comunicação entre microsserviços**.

---

Quer que eu gere esse README em formato **markdown pronto pra colar no seu GitHub (com emojis, formatação e badges no topo)**?
Posso adicionar, por exemplo, badges de linguagem (`Python`, `Docker`, `Flask`) e um banner visual estilizado.
