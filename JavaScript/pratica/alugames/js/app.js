function alterarStatus(id){
	// let livre = document.innerHTML(`dashboard__item__button`);
    // livre = True;

    // if(livre == False){
    //     livre.classList.remove(`dashboard__item__button`);
    //     livre.classList.add(`dashboard__item__button dashboard__item__button--return`);
    // }else{
    //     livre.classList.remove(`dashboard__item__button dashboard__item__button--return`);
    //     livre.classList.add(`dashboard__item__button`);
    // }

    let gameClicado = document.getElementById(`game-${id}`); //pego o que foi clicado
    //recupera a div e o botão
    let imagem = document.gameClicado.querySelector('.dashboard__item__img');
    let botao = document.gameClicado.querySelector('.dashboard__item__button');
    //let nomeJogo = document.gameClicado.querySelector('.dashboard__item__name');
    //alert(nomeJogo.textContent); //só para conferir que o elemento foi realmente clicado

    if (imagem.classList.contains('dashboard__item__img--rented')){
        imagem.classList.remove('dashboard__item__img--rented');
        botao.classList.remove('dashboard__item__button--return');
        botao.textContent = 'Alugar';
    }else{
        imagem.classList.add('dashboard__item__img--rented');
        botao.textContent = 'Devolver';
        botao.classList.add('dashboard__item__button--return');
    }
}