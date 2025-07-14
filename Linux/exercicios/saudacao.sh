#!/bin/bash

date=$(date +%H)
usuario=$(whoami)

if ["$date" -ge 5] && ["$date" -lt 12]; then
	saudacao='Bom dia'
elif ["$date" -ge 12] && ["$date" -lt 18]; then
	saudacao='Boa tarde'
else
	saudacao='Boa noite'
fi

echo "$saudacao, $usuario"
echo "Agora são &(date +%H:+%M:+%S)"
