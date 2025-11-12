# 🚀 Desafio 3 — Docker Compose Orquestrando Serviços

## 🧠 1. Descrição da solução, arquitetura e decisões técnicas

### 🎯 Objetivo
Demonstrar a **orquestração de múltiplos serviços dependentes** (Web + Banco de Dados + Cache) utilizando **Docker Compose**, simulando um ambiente de microsserviços com comunicação interna e gerenciamento centralizado.

### 🧩 Arquitetura dos serviços

- **`web` (Flask App)**  
  Serviço principal da aplicação.  
  - Linguagem: Python (Flask)  
  - Porta exposta: `5000`  
  - Se comunica com:
    - PostgreSQL (`db`)
    - Redis (`cache`)

- **`db` (PostgreSQL)**  
  Banco de dados relacional para armazenamento de dados persistentes.  
  - Porta interna: `5432`
  - Volume: `pgdata` (para garantir persistência)

- **`cache` (Redis)**  
  Sistema de cache em memória para simular uso de dados temporários.  
  - Porta interna: `6379`

---

## ⚙️ 2. Decisões técnicas

| Componente | Decisão | Justificativa |
|-------------|----------|----------------|
| **Flask** | Framework simples e rápido | Ideal para demonstrações e microserviços |
| **PostgreSQL** | Banco relacional completo | Mostra integração real com um serviço de banco |
| **Redis** | Cache leve e popular | Demonstra comunicação entre múltiplos containers |
| **Docker Compose** | Orquestração declarativa | Facilita subir todos os serviços de forma integrada |
| **Volumes** | Persistência do banco | Evita perda de dados ao remover containers |
| **depends_on** | Garantir ordem de inicialização | Evita erros de conexão durante o boot da aplicação |

---

## 🧰 3. Instruções de execução passo a passo

### 1️⃣ Subir os serviços com Docker Compose

```bash
docker compose up -d --build
```

### 2️⃣ Verificar containers ativos

```bash
docker ps
```

---

### 3️⃣ Testar a aplicação

Acesse no navegador:
👉 [http://localhost:5000](http://localhost:5000)

Você verá uma mensagem retornada pela aplicação Flask confirmando a comunicação com:

* O **banco PostgreSQL**
* O **cache Redis**

---

### 4️⃣ Conferir logs em tempo real

```bash
docker compose logs -f
```

---

### 5️⃣ Encerrar e limpar o ambiente

```bash
docker compose down
```

---

## 📦 5. docker-compose.yml 

```yaml
services:
  web:
    build: ./web
    container_name: web_app
    ports:
      - "5000:5000"
    depends_on:
      - db
      - cache
    environment:
      - DATABASE_HOST=db
      - DATABASE_USER=admin
      - DATABASE_PASSWORD=admin
      - REDIS_HOST=cache
    networks:
      - backend

  db:
    image: postgres:15
    container_name: postgres_db
    environment:
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin
      - POSTGRES_DB=empresa
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - backend

  cache:
    image: redis:7
    container_name: redis_cache
    networks:
      - backend

volumes:
  pgdata:

networks:
  backend:
```

---
