sleep 5
while true; do
  echo "Cliente olhando o servidor..."
  curl -s web:8080
  echo -e "\n---"
  sleep 5
done
