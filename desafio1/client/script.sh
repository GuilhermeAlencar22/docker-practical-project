#!/bin/bash

# Espera o servidor subir
sleep 5

# Faz requisições a cada 5 segundos
while true; do
  echo "Cliente consultando o servidor..."
  curl -s web:8080
  echo -e "\n---"
  sleep 5
done
