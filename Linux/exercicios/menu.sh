#!/bin/bash'
echo 'Escolha uma opção: 
	     1- Mostrar data
	     2- Mostrar usuário
	     3- Sair'
read escolha

case $escolha in
	1)
	  echo "$(date +%H:%M:%S)"
	  ;;
	2)
	  echo "$USER"
	  ;;
	3)
	   echo "Saindo..."
	   exit
	   ;;
        *)
	   echo "Opção inválida"
	   ;;
esac
