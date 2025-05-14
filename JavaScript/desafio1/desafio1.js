//1: 
// Altere o conteúdo da tag h1 com document.querySelector e atribua o
// seguinte texto: Hora do Desafio.
let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

//2:
// Crie uma função que exiba no console a mensagem O botão foi 
// clicado sempre que o botão Console for pressionado.
function clique_botao(){
    console(`O botão foi clicado`);
}

//3:
// Crie uma função que exiba um alerta com a mensagem: Eu amo JS, 
// sempre que o botão Alerta for pressionado.
function botao_alerta(){
    alert('Eu amo JS');
}

//4:
// Crie uma função que é executada quando o botão prompt é clicado, 
// perguntando o nome de uma cidade do Brasil. Em seguida, exiba um 
// alerta com a mensagem concatenando a resposta com o texto: Estive 
// em {cidade} e lembrei de você.
function clique_prompt(){
    cidade = prompt(`Digite o nome de uma cidade brasileira: `);
    alert('Estive em '+cidade+' e lembrei de você');
}

//5:
// Ao clicar no botão soma, peça 2 números inteiros e exiba o 
// resultado da soma em um alerta.
function botao_soma(){
    let num_1 = parseInt(prompt(`Digite um número: `)); //tem que dizer que é número, senão entende que é string
    let num_2 = parseInt(prompt(`Digite outro número: `));
    let soma = num_1 + num_2;
    alert(`A soma dos números é: ${soma}`);
}

