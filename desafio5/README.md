Perfeito, Guilherme — aqui está o **README.md pronto e finalizado** para o **Desafio 5 — Microsserviços com API Gateway**, formatado para colar direto na pasta `desafio5/README.md`.

Copie e cole tudo abaixo no arquivo.

```markdown
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

> Observação: se alguma porta (5001/5002/8080) já estiver ocupada no host, altere o mapeamento em `ports` (por ex. `5051:5001`) — as chamadas internas entre serviços continuam usando as portas internas (5001/5002).

---

## 🧾 Arquivos principais (o que eles fazem)

* `service1-users/app.py` → fornece `/users` (JSON).
* `service2-orders/app.py` → fornece `/orders` (JSON).
* `gateway/app.py` → expõe `/users` e `/orders`, encaminhando para `service1` e `service2`.
* Cada pasta tem `Dockerfile` e `requirements.txt` para construir imagens locais.

---

## ▶️ Passo a passo — Como executar (MacBook / VS Code / Terminal)

1. Abra o Terminal na pasta `desafio5/`:

   ```bash
   cd /caminho/para/docker-labs/desafio5
   ```

2. (Opcional) Pare containers que possam conflitar:

   ```bash
   docker ps
   docker rm -f service1-users service2-orders api-gateway || true
   ```

3. Subir e construir tudo:

   ```bash
   docker compose up -d --build
   ```

4. Conferir containers rodando:

   ```bash
   docker ps
   ```

5. Testes via curl (ou navegador / Postman):

   * Gateway → Users

     ```bash
     curl http://localhost:8080/users
     ```

     Resposta esperada: JSON com lista de usuários.

   * Gateway → Orders

     ```bash
     curl http://localhost:8080/orders
     ```

     Resposta esperada: JSON com lista de pedidos.

6. Para ver logs:

   ```bash
   docker compose logs -f
   ```

   Ou logs de um container específico:

   ```bash
   docker logs -f api-gateway
   ```

7. Parar e remover os serviços:

   ```bash
   docker compose down
   ```

---

## ✅ Testes de aceitação (o que provar para o professor)

* **Gateway como único ponto de entrada**: acessar `http://localhost:8080/users` e `http://localhost:8080/orders` e receber respostas corretas (os mesmos JSONs que os serviços originais retornam).
* **Integração correta**: gateway retorna as respostas dos serviços sem modificar indevidamente os dados.
* **Isolamento**: cada serviço roda em seu próprio container com dependências controladas via `requirements.txt`.
* **Documentação**: este README serve como prova de execução e explicação da arquitetura.

---

## 🔍 Exemplos de saída esperada

* `curl http://localhost:8080/users`

```json
[
  {"id": 1, "nome": "Guilherme Alencar", "email": "guilherme@empresa.com"},
  {"id": 2, "nome": "Mariana Costa", "email": "mariana@empresa.com"},
  {"id": 3, "nome": "Lucas Mendes", "email": "lucas@empresa.com"}
]
```

* `curl http://localhost:8080/orders`

```json
[
  {"id": 101, "user_id": 1, "produto": "Notebook", "valor": 4500.0},
  {"id": 102, "user_id": 2, "produto": "Teclado Mecânico", "valor": 520.0},
  {"id": 103, "user_id": 3, "produto": "Monitor 27\"", "valor": 1250.0}
]
```

---

## 🧾 Boas práticas e observações para entrega

* Inclua **prints** dos passos: `docker ps`, respostas do `curl`, e logs do gateway (`docker logs api-gateway`) na pasta `prints/` do repositório para evidência visual.
* Explique no README (ou anexo) **linha a linha** do `docker-compose.yml` caso o professor solicite.
* Se desejar, comente o `gateway/app.py` explicando por que usar `requests` (simplicidade) e que, em produção, você poderia usar um proxy reverso (Nginx) ou um API Gateway mais robusto (Kong, Traefik, etc).
* Garanta que **não haja containers legados** ocupando as portas antes da demonstração (use `docker ps` e `docker rm -f` conforme necessário).

---

## 🎯 Critérios de Avaliação (como isso atende)

|                             Critério |   Peso | Como foi atendido                                                         |
| -----------------------------------: | -----: | ------------------------------------------------------------------------- |
| Gateway funcionando como ponto único | 10 pts | `/users` e `/orders` expostos via gateway e retornando dados dos serviços |
|            Integração entre serviços |  5 pts | Gateway consome `service1:5001` e `service2:5002` na rede interna         |
|                     README detalhado |  5 pts | Este README com passos, exemplos e verificações                           |
|            Código organizado e claro |  5 pts | Pastas separadas, Dockerfiles e requirements isolados                     |

---

## ✨ Autor

**Guilherme Alencar** — Desafio 5: Microsserviços com API Gateway
Data: Novembro/2025

---

Se quiser, eu já gero a **versão com prints simulados** (imagens placeholders) e um arquivo `ENTREGA.md` resumido para a submissão — quer que eu gere isso agora?
