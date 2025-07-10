echo "Informe um arquivo: "
read arquivo

if [ -e "$arquivo" ]; then
	echo 'O arquivo existe'
	quantidade=$(wc -w $arquivo)
	echo $quantidade
else
	echo 'Arquivo não encontrado'
fi

