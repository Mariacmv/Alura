#!/bin/bash

LOG_DIR="../myapp/logs"
ARQUIVO_DIR="../myapp/logs-processados"
TEMP_DIR="../myapp/logs-temp"

mkdir -p $ARQUIVO_DIR
mkdir -p $TEMP_DIR

find "$LOG_DIR" -name "*.log" -print0 | while IFS= read -r -d '' arquivo;
do
    grep "ERROR" "$arquivo" > "${arquivo}.filtrado"
    grep "SENSITIVE_DATA" $arquivo >> "${arquivo}.filtrado"

    sed -i 's/User password is .*/User password is REDACTED/g' "${arquivo}.filtrado"
    sed -i 's/User password reset request with token .*/User password reset request with token REDACTED/g' "${arquivo}.filtrado"
    sed -i 's/API key leaked: .*/API key leaked: REDACTED/g' "${arquivo}.filtrado" 
    sed -i 's/User credit card last four digits: .*/User credit card last four digits: REDACTED/g' "${arquivo}.filtrado"
    sed -i 's/User session initiated with token: .*/User session initiated with token: REDACTED/g' "${arquivo}.filtrado"

    sort "${arquivo}.filtrado" -o "${arquivo}.filtrado"
    uniq "${arquivo}.filtrado" > "${arquivo}.unico"

    num_palavras=$(wc -w < "${arquivo}.unico")
    num_linhas=$(wc -l < "${arquivo}.unico")

    nome_arquivo=$(basename "${arquivo}.unico")

    echo "Arquivo: $nome_arquivo" >> "${ARQUIVO_DIR}/log_stats_$(date +%F)"
    echo "Número de linhas: $num_linhas" >> "${ARQUIVO_DIR}/log_stats_$(date +%F)"
    echo "Número de palavras: $num_palavras" >> "${ARQUIVO_DIR}/log_stats_$(date +%F)"
    echo "---------------------------------" >> "${ARQUIVO_DIR}/log_stats_$(date +%F)"

    if [[ "$nome_arquivo" == *frontend* ]]; then
	    sed 's/^/[FRONTEND] /' "${arquivo}.unico" >> "${ARQUIVO_DIR}/logs_combinados_$(date +%F).log"
    elif [[ "$nome_arquivo" == *backend* ]]; then
	    sed 's/^/[BACKEND] /' "${arquivo}.unico" >> "${ARQUIVO_DIR}/logs_combinados_$(date +%F).log"
    else
	    cat "${arquivo}.unico" >> "${ARQUIVO_DIR}/logs_combinados_$(date +%F).log"
    fi

done
sort -k2 "${ARQUIVO_DIR}/logs_combinados_$(date +%F)" -o "${ARQUIVO_DIR}/logs_combinados_$(date +%F).log"

mv "${ARQUIVO_DIR}/logs_combinados_$(date +%F).log" "$TEMP_DIR/"
mv "${ARQUIVO_DIR}/logs_stats_$(date +%F).txt" "$TEMP_DIR/"

tar -czf "${ARQUIVO_DIR}/logs_$(date +%F).tar.gz" -C "$TEMP_DIR" .
rm -r "$TEMP_DIR"
