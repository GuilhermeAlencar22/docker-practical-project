# 🐳 Desafio 1 — Containers em Rede

## 1. Descrição da solução, arquitetura e decisões técnicas

### 🧩 Descrição da solução
A solução consiste em dois containers Docker conectados em uma rede Docker personalizada (`rede-flask`):

- **Container `web`** → servidor web simples implementado com **Flask (Python)**.  
  Expõe uma rota `/` que retorna uma mensagem de confirmação. Escuta na porta **8080**.
- **Container `client`** → container leve baseado em **Alpine** que executa um script Bash (`script.sh`) fazendo requisições HTTP periódicas para `web:8080` usando `curl`, imprimindo os resultados nos logs.

🎯 **Objetivo:** demonstrar comunicação entre containers via rede Docker, resolvendo endereçamento por nomes (DNS interno do Docker).

---

### ⚙️ Decisões técnicas e justificativas
- **Flask (Python):** rápido para criar uma API HTTP simples e legível.
- **Alpine + curl:** imagem mínima ideal para simular requisições HTTP.
- **Rede customizada (`rede-flask`):** permite comunicação interna entre containers por nome, sem precisar expor IPs.
- **Scripts `run-containers.sh` e `docker-network.sh`:** automatizam build, criação de rede e execução, garantindo reprodutibilidade.
- **Mapeamento de porta `-p 8080:8080`:** permite acessar o Flask também no navegador via `http://localhost:8080`.
- **Uso de hostnames Docker:** o container `client` acessa o servidor simplesmente via `web:8080`, demonstrando boas práticas de rede.

---

## 2. Explicação detalhada do funcionamento

### 🧱 Componentes
- **Imagem `flask-server`**  
  - Construída a partir de `web/Dockerfile`  
  - Contém `app.py` com servidor Flask  
  - Expõe porta 8080 e executa `python app.py`

- **Imagem `curl-client`**  
  - Construída a partir de `client/Dockerfile`  
  - Contém `script.sh` que:
    1. Aguarda o servidor subir (`sleep 5`)
    2. Entra em loop e executa `curl -s web:8080`
    3. Exibe no log a resposta recebida do Flask

- **Rede `rede-flask`**
  - Criada com `docker network create rede-flask`
  - Permite que o container `client` resolva o nome `web` via DNS interno do Docker

---

### 🔁 Fluxo de execução
1. O script `run-containers.sh` constrói as imagens e cria a rede se necessário.  
2. O container `web` é iniciado e expõe a aplicação Flask.  
3. O container `client` entra em loop chamando `web:8080` a cada 5 segundos.  
4. O Docker DNS resolve o nome `web` → IP interno do container Flask.  
5. O `client` mostra no log a resposta vinda do servidor.  

---

### 🔒 Isolamento e rede
- A comunicação ocorre apenas pela rede interna Docker (`rede-flask`).
- Somente a porta 8080 do `web` é exposta ao host.
- O `client` nunca acessa o host diretamente — ele fala com `web` pela bridge interna.

---

## 3. 🚀 Instruções de execução passo a passo

> **Pré-requisitos (no MacBook):**
> - Docker Desktop instalado e em execução (ícone da baleia ativo)
> - VS Code ou Terminal nativo
> - Estar na pasta `desafio1/` do projeto

---

### 1️⃣ Navegar até a pasta do desafio
```bash
cd /caminho/para/seu/projeto/desafio1
2️⃣ Garantir permissões de execução dos scripts
bash
Copiar código
chmod +x docker-network.sh run-containers.sh client/script.sh
3️⃣ Remover containers antigos (opcional, para evitar conflitos)
bash
Copiar código
docker rm -f web client || true
4️⃣ Executar o script principal
bash
Copiar código
./run-containers.sh
Esse script:

Constrói as imagens (flask-server e curl-client)

Cria a rede (rede-flask) se não existir

Inicia os dois containers conectados entre si

5️⃣ Verificar se os containers estão rodando
bash
Copiar código
docker ps
Saída esperada:

mathematica
Copiar código
CONTAINER ID   IMAGE          COMMAND          STATUS         PORTS                    NAMES
45d5a7a06430   flask-server   "python app.py"  Up X seconds   0.0.0.0:8080->8080/tcp   web
90011fada11c   curl-client    "/script.sh"     Up X seconds                            client
6️⃣ Ver logs do cliente (comunicação com o servidor)
bash
Copiar código
docker logs -f client
Saída esperada:

yaml
Copiar código
Cliente consultando o servidor...
Olá! Mensagem recebida do container web (Flask)!
---
7️⃣ Testar no navegador
Acesse:

arduino
Copiar código
http://localhost:8080
ou use:

bash
Copiar código
curl http://localhost:8080
8️⃣ Encerrar e limpar
bash
Copiar código
docker rm -f client web
docker network rm rede-flask