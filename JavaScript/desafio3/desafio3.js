//1- Crie uma função que calcule o índice de massa corporal (IMC) de uma 
// pessoa, a partir de sua altura, em metros, e peso, em quilogramas, 
// que serão recebidos como parâmetro.
function imc(altura, peso){
    return peso/altura; 
}
resultado = imc(170, 63);

//2- Crie uma função que calcule o valor do fatorial de um número passado
// como parâmetro.
function fatorial(numero){
    while (numero != 0){
        return numero * numero - 1;
    }
}
fatorial(2);

//3- Crie uma função que converte um valor em dólar, passado como 
// parâmetro, e retorna o valor equivalente em reais. Para isso, 
// considere a cotação do dólar igual a R$4,80.
function convertor(dolar){
    return dolar * 4.80;
}
convertor(100);
//4- Crie uma função que mostre na tela a área e o perímetro de uma sala 
// retangular, utilizando altura e largura que serão dadas como 
// parâmetro.
function medidas(altura, largura){
    area = altura * largura;
    console.log(area);
    perimetro = (altura*2)+(largura*2);
    console.log(perimetro);
}
medidas(100, 50);

//5- Crie uma função que mostre na tela a área e o perímetro de uma sala 
// circular, utilizando seu raio que será fornecido como parâmetro. 
// Considere Pi = 3,14.
function circulo(raio, pi=3.14){
    area = raio**raio*pi;
    console.log(area);
    perimetro = 2*pi*raio;
    console.log(perimetro);
}
circulo(5);
//6- Crie uma função que mostre na tela a tabuada de um número dado como 
// parâmetro.
function tabuada(numero){
    while (i != 10){
        return numero * i;
    }
    i++;
}
