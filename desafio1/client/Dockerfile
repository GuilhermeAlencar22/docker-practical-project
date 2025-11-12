# Usa uma imagem leve com curl
FROM alpine:latest

# Instala curl
RUN apk add --no-cache curl bash

# Copia o script para dentro do container
COPY script.sh /script.sh

# Dá permissão de execução
RUN chmod +x /script.sh

# Comando para rodar o script
CMD ["/script.sh"]
