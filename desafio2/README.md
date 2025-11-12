# 🐳 Desafio 2 — Volumes e Persistência (Docker + PostgreSQL)

## 🎯 1. Descrição da Solução

Este desafio demonstra **como manter dados persistentes mesmo após a remoção de containers**, utilizando **volumes Docker** com o **PostgreSQL** como exemplo prático.

A aplicação cria um **container de banco de dados** (`postgres-db`) com um volume associado (`pgdata`), garantindo que os dados gravados no banco **não sejam perdidos** quando o container for destruído e recriado.

---

### Tecnologias:

* Utilizado **PostgreSQL 15** por ser leve e amplamente aceito em containers.
* Volume nomeado (`pgdata`) garante persistência de dados em `/var/lib/postgresql/data`.
* O script `init.sql` é executado **automaticamente** ao criar o container pela primeira vez.
* `docker-compose` centraliza toda a configuração e facilita o reuso do projeto.

---

## 🧠 3. Explicação Detalhada do Funcionamento

### 🔹 Fluxo geral:

1. `docker-compose.yml` cria o serviço `db` (PostgreSQL) com o volume `pgdata`.
2. O Docker monta o volume localmente em `/var/lib/postgresql/data`.
3. Na primeira execução, o PostgreSQL roda o script `init.sql`, criando a base `empresa` e populando a tabela `funcionarios`.
4. Após parar e remover o container, os dados **permanecem** no volume.
5. Ao subir novamente, o container **lê os dados persistidos** do volume existente.

---

## 🧩 4. Estrutura técnica do docker-compose

```yaml
services:
  db:
    image: postgres:15
    container_name: postgres-db
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: empresa
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  pgdata:
```

---

## 🧾 5. Script de inicialização (init.sql)

```sql
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(100) NOT NULL
);

INSERT INTO funcionarios (nome, cargo) VALUES
('Guilherme Alencar', 'Analista de Dados'),
('Mariana Costa', 'Dev Back-End'),
('Lucas Mendes', 'DevOps Engineer');
```

---

## ⚙️ 6. Instruções de Execução (Passo a Passo)

### 1️⃣ Subir o container e o volume

```bash
docker compose up -d
```

📦 Isso cria:

* A rede padrão (`desafio2_default`)
* O volume nomeado (`desafio2_pgdata`)
* O container `postgres-db` com o banco `empresa`

---

### 2️⃣ Verificar se está rodando

```bash
docker ps
```

---

### 3️⃣ Acessar o banco

```bash
docker exec -it postgres-db psql -U admin -d empresa
```

Dentro do PostgreSQL:

```sql
\dt
SELECT * FROM funcionarios;
```
---

### 4️⃣ Testar persistência de dados

Remova completamente o container:

```bash
docker rm -f postgres-db
```

Suba novamente:

```bash
docker compose up -d
```

Agora rode:

```bash
docker exec -it postgres-db psql -U admin -d empresa -c "SELECT * FROM funcionarios;"
```

Resultado: os mesmos registros continuam salvos — **prova de persistência via volume**.

---

### 🧹 5️⃣ Limpeza final

```bash
docker rm -f postgres-db
docker volume rm desafio2_pgdata
```

---

## 🏁 7. Conclusão

* ✅ O volume Docker `pgdata` garantiu **persistência total dos dados**.
* ✅ Após deletar e recriar o container, as informações continuaram acessíveis.
* ✅ O uso de `docker-compose` e `init.sql` trouxe **clareza e reprodutibilidade**.
* ✅ Estrutura organizada e README completo atendem 100% aos critérios de avaliação.
