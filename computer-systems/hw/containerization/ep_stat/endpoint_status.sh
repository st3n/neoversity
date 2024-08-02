#!/bin/bash

websites=("https://google.com" "https://facebook.com" "https://twitter.com")

log_file="website_status.log"

> $log_file

for website in "${websites[@]}"
do
  # Виконання запиту за допомогою curl і отримання статус-коду
  status_code=$(curl -L -o /dev/null -s -w "%{http_code}\n" "$website")
  
  # Перевірка статус-коду та запис результату у файл логів
  if [ "$status_code" -eq 200 ]; then
    echo "<$website> is UP" >> $log_file
  else
    echo "<$website> is DOWN" >> $log_file
  fi
done

# Виведення результатів у консоль
cat $log_file

echo "Results saved in $log_file"

