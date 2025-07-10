echo "Digite um tipo de arquivo:"
read tipo

arquivos=(*.$tipo)

if [ ${#arquivos[@]} -gt 0 ]; then
    echo "Arquivos com .$tipo encontrados:"
    for arquivo in "${arquivos[@]}"; do
        echo "$arquivo"
    done
fi
