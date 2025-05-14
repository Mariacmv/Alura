//1- Criar uma função que exibe "Olá, mundo!" no console.
function mensagem(){
    console.log('Olá, mundo!');
}
mensagem();
//2- Criar uma função que recebe um nome como parâmetro e exibe "Olá, 
// [nome]!" no console.
function mensagem(nome){
    console.log(`Olá, ${nome}`);
}
mensagem('Maria');
//3- Criar uma função que recebe um número como parâmetro e retorna o 
// dobro desse número.
function dobrar(numero){
    return numero * 2;
}
let resultado = dobrar(2);
console.log(resultado);
//4- Criar uma função que recebe três números como parâmetros e retorna
// a média deles.
function media(a, b, b){
    return (a + b + c)/3;
}
let resul = media(2,3,4);
console.log(resul);
//5- Criar uma função que recebe dois números como parâmetros e retorna
// o maior deles.
function maior(a, b){
    if (a > b){
        return a;
    }else{
        return b;
    }
}
let maior = maior(4, 9);
console.log(maior);
//6- Criar uma função que recebe um número como parâmetro e retorna o 
// resultado da multiplicação desse número por ele mesmo
function mult(numero){
    return numero*numero;
}
let res = mult(5);
console.log(res);