Perfeito, Guilherme 👏
Abaixo está o **`README.md` completo do Desafio 4 — Microsserviços Independentes**, já formatado para GitHub, com **descrição, arquitetura, endpoints, execução e testes**.
Basta copiar e colar no seu repositório ou diretório do projeto.

---

```markdown
# 🧩 Desafio 4 — Microsserviços Independentes (Docker + Flask)

## 🎯 Objetivo
Demonstrar a comunicação entre **dois microsserviços independentes** executando via **Docker**, utilizando **requisições HTTP**.

---

## 🏗️ Arquitetura da Solução

O projeto contém **dois microsserviços Flask** que se comunicam pela **rede interna do Docker Compose**:

```

+----------------------+           +----------------------+
|   Service A (API)    |  --->     |   Service B (Client) |
| Porta: 5001          |           | Porta: 5002          |
| Retorna lista JSON   |           | Consome /users de A  |
+----------------------+           +----------------------+

```

### 🔹 **Microsserviço A – `service-a`**
- Porta: **5001**
- Responsável por fornecer uma **API REST** que retorna uma lista de usuários em formato JSON.
- Endpoint principal: `/users`

### 🔹 **Microsserviço B – `service-b`**
- Porta: **5002**
- Consome a API do **Service A** via HTTP.
- Retorna mensagens combinando os dados recebidos.
- Endpoint principal: `/info`

---

## ⚙️ Estrutura do Projeto

```

desafio4/
│
├── service-a/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── service-b/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml

````

---

## 🐳 Docker Compose – Orquestração

O arquivo `docker-compose.yml` define os dois serviços e a rede interna compartilhada.

```yaml
services:
  service-a:
    build: ./service-a
    container_name: service-a
    ports:
      - "5001:5001"

  service-b:
    build: ./service-b
    container_name: service-b
    ports:
      - "5002:5002"
    depends_on:
      - service-a
````

* Ambos os containers compartilham a rede interna do Compose.
* `depends_on` garante que o **service-a** suba primeiro.
* A comunicação ocorre via `http://service-a:5001`.

---

## 🚀 Passos para Execução

### 1️⃣ Subir os containers

No terminal dentro da pasta `desafio4/`, execute:

```bash
docker compose up -d --build
```

---

### 2️⃣ Verificar containers ativos

```bash
docker ps
```

Resultado esperado:

```
CONTAINER ID   IMAGE           NAMES
xxxxxx         desafio4-service-a   service-a
yyyyyy         desafio4-service-b   service-b
```

---

### 3️⃣ Testar os Endpoints

#### 🔸 Service A (API de Usuários)

```bash
curl http://localhost:5001/users
```

**Resposta esperada:**

```json
[
  {"id": 1, "nome": "Guilherme Alencar", "ativo_desde": "2022-05-14"},
  {"id": 2, "nome": "Mariana Costa", "ativo_desde": "2023-02-01"},
  {"id": 3, "nome": "Lucas Mendes", "ativo_desde": "2024-07-22"}
]
```

---

#### 🔸 Service B (Consumidor)

```bash
curl http://localhost:5002/info
```

**Resposta esperada:**

```json
[
  "Usuário Guilherme Alencar ativo desde 2022-05-14",
  "Usuário Mariana Costa ativo desde 2023-02-01",
  "Usuário Lucas Mendes ativo desde 2024-07-22"
]
```

---

## 🔍 Explicação Técnica

* Cada microsserviço possui seu próprio **Dockerfile** e **dependências isoladas**.
* A comunicação entre eles é feita via **HTTP requests** na **rede interna** do Docker Compose.
* O **Service B** utiliza `requests` para acessar o endpoint `/users` do Service A.
* Essa abordagem reflete a **arquitetura de microsserviços desacoplados**.

---

## 📦 Comandos Úteis

🧱 **Rebuild completo**

```bash
docker compose up -d --build
```

🧹 **Parar e remover containers**

```bash
docker compose down
```

🧼 **Limpar volumes e imagens**

```bash
docker system prune -a
```

---

``
