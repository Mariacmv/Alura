function sortear(){
    let quantidade = parseInt(document.getElementById('quantidade').value); //pega o id da tag do html e o valor passado pelo usuário no input do html
    let de = parseInt(document.getElementById('id').value);
    let ate = parseInt(document.getElementById('ate').value);

    let sorteados = [];

    let numero;

    for (let i = 0; i < quantidade; i++){
        numero.obterNumeroAleatorio(de,ate);
        while (sorteados.includes(numero)){//enquanto o número estiver dentro do array, enquanto existir no array
            numero = obterNumeroAleatorio(de, ate);
        }
        sorteados.push(numero);
    }
    
    let resultado = document.getElementById('resultado');
    resultado.innerHTML = `<label class="texto__paragrafo">Números sorteados: ${sorteados}</label>`;
    alterarStatusBotao();
}

function obterNumeroAleatorio(min, max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function alterarStatusBotao(){
    let botao = document.getElementById('btn-reiniciar');
    if (botao.classList.contains('container__botao-desabilitado')){
        botao.classList.remove('container__botao-desabilitado');
        botao.classList.add('container__botao');
    }else{
        botao.classList.remove('container__botao');
        botao.classList.add('container__botao-desabilitado');
    }
}

function reiniciar(){
    document.getElementById('quantidade').value = ''; //para limpar um campo é só atribuir uma string vazia
    document.getElementById('de').value = '';
    document.getElementById('ate').value = '';
    document.getElementById('resultado').innerHTML = 'Números sorteados:  nenhum até agora';

    alterarStatusBotao();
}