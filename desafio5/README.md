# 🚀 Desafio 5 — Microsserviços com API Gateway (Docker + Flask)

## 🎯 Objetivo
Criar uma arquitetura com **API Gateway** centralizando o acesso a dois microsserviços:
- **Service 1 (Users)** → fornece dados de usuários (`/users`)
- **Service 2 (Orders)** → fornece pedidos (`/orders`)
- **Gateway** → expõe `/users` e `/orders` e orquestra as chamadas aos serviços

Todos os serviços devem rodar em containers via **Docker Compose**.

---

## 📁 Estrutura do projeto

```

desafio5/
│
├── gateway/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── service1-users/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── service2-orders/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml

````

---

## 🧠 Arquitetura e decisões técnicas

- **API Gateway** (Flask) atua como ponto único de entrada: `/users` e `/orders`.
- **Service1 (Users)** expõe `/users` com lista de usuários (JSON).
- **Service2 (Orders)** expõe `/orders` com lista de pedidos (JSON).
- Comunicação interna entre containers pela **rede do Docker Compose** (acesso por nome de serviço: `service1:5001`, `service2:5002`).
- Cada serviço tem **Dockerfile** próprio e `requirements.txt` (isolamento de dependências).
- Gateway usa `requests` para encaminhar chamadas aos serviços internos.

---

## 🐳 docker-compose.yml (resumo)
(O arquivo já está no repositório; este é o comportamento esperado)

```yaml
services:
  service1:
    build: ./service1-users
    container_name: service1-users
    ports:
      - "5001:5001"

  service2:
    build: ./service2-orders
    container_name: service2-orders
    ports:
      - "5002:5002"

  gateway:
    build: ./gateway
    container_name: api-gateway
    ports:
      - "8080:8080"
    depends_on:
      - service1
      - service2
````
---

## 🧾 Arquivos principais (o que eles fazem)

* `service1-users/app.py` → fornece `/users` (JSON).
* `service2-orders/app.py` → fornece `/orders` (JSON).
* `gateway/app.py` → expõe `/users` e `/orders`, encaminhando para `service1` e `service2`.
* Cada pasta tem `Dockerfile` e `requirements.txt` para construir imagens locais.

---

## ▶️ Passo a passo — Como executar (MacBook / VS Code / Terminal)

1. Subir e construir tudo:

   ```bash
   docker compose up -d --build
   ```

2. Conferir containers rodando:

   ```bash
   docker ps
   ```

3. Testes via curl:

   * Gateway → Users

     ```bash
     curl http://localhost:8080/users
     ```

   * Gateway → Orders

     ```bash
     curl http://localhost:8080/orders
     ```

4. Para ver logs:

   ```bash
   docker compose logs -f
   ```

5. Parar e remover os serviços:

   ```bash
   docker compose down
   ```

---
