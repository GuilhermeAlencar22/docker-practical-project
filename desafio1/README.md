# 🐳 Desafio 1 — Containers em Rede

## 1. Descrição da solução, arquitetura e decisões técnicas

### 🧩 Descrição da solução
A solução consiste em dois containers Docker conectados em uma rede Docker personalizada (`rede-flask`):

- **Container `web`** → servidor web simples implementado com **Flask (Python)**.  
  Expõe uma rota `/` que retorna uma mensagem de confirmação. Escuta na porta **8080**.
- **Container `client`** → container leve baseado em **Alpine** que executa um script Bash (`script.sh`) fazendo requisições HTTP periódicas para `web:8080` usando `curl`, imprimindo os resultados nos logs.

🎯 **Objetivo:** demonstrar comunicação entre containers via rede Docker, resolvendo endereçamento por nomes (DNS interno do Docker).

---

## 2. Explicação detalhada do funcionamento

### Componentes
- **Imagem `flask-server`**  
  - Construída a partir de `web/Dockerfile`  
  - Contém `app.py` com servidor Flask  
  - Expõe porta 8080 e executa `python app.py`

- **Imagem `curl-client`**  
  - Construída a partir de `client/Dockerfile`  
  - Contém `script.sh` que:
    1. Aguarda o servidor subir
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
4. O Docker DNS resolve o nome `web` IP interno do container Flask.  
5. O `client` mostra no log a resposta vinda do servidor.  

---

### 🔒 Isolamento e rede
- A comunicação ocorre apenas pela rede interna Docker (`rede-flask`).
- Somente a porta 8080 do `web` é exposta ao host.
- O `client` nunca acessa o host diretamente — ele fala com `web` pela bridge interna.

---

## 3. 🚀 Instruções de execução passo a passo

### 1️⃣ Navegar até a pasta do desafio
Garantir permissões de execução dos scripts:
chmod +x docker-network.sh run-containers.sh client/script.sh

Remover containers antigos: 
bash
docker rm -f web client || true

Executar o script principal:
bash
./run-containers.sh
Esse script:

Constrói as imagens (flask-server e curl-client)

Cria a rede (rede-flask) se não existir

Inicia os dois containers conectados entre si

Verificar se os containers estão rodando:
bash
docker ps

Ver logs do cliente (comunicação com o servidor):
docker logs -f client

Testar no navegador:
Acesse:

http://localhost:8080
ou use:


Encerrar e limpar:
docker rm -f client web
docker network rm rede-flask
