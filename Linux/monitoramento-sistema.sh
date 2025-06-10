#!/bin/bash

LOG_DIR="monitoramento-sistema"
mkdir -p $LOG_DIR

function monitorar_logs() {
   journalctl -p 3 -b | grep -E "(fail(ed)?|error|denied|unauthorized)" > "$LOG_DIR/monitoramento_logs_sistema.txt"
}

function monitorar_rede() {
    if ping -c 1 8.8.8.8 > /dev/null; then
        echo "$(date): Conectividade ativa." >> $LOG_DIR/monitoramento_rede.txt
    else
        echo "$(date): Sem conexão com a internet." >> $LOG_DIR/monitoramento_rede.txt
    fi

    if curl -s --head https://www.alura.com.br/ | grep "HTTP/2 200" > /dev/null; then
        echo "$(date): Conexão com a Alura bem-sucedida." >> $LOG_DIR/monitoramento_rede.txt
    else
        echo "$(date): Falha ao conectar com a Alura." >> $LOG_DIR/monitoramento_rede.txt
    fi
}

function executar_monitoramento() {
    monitorar_logs
    monitorar_rede
}

executar_monitoramento
