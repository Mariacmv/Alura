echo "Digite o nome do arquivo: "
read arquivo

if [ -e "$arquivo" ]; then
	echo 'O arquivo existe!'
else
	echo 'O arquivo não foi encontrado'
fi
