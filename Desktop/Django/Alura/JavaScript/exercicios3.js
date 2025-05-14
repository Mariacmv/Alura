//1:
// Crie um contador que comece em 1 e vá até 10 usando um loop while. 
// Mostre cada número.

contador = 1;
while (contador <= 10){
    console.log(contador);
    contador ++;
} //(V)

//2:
// Crie um contador que começa em 10 e vá até 0 usando um loop while. 
// Mostre cada número.

contador = 10;
while (contador != 0){
    console.log(contador);
    contador --;
}
//while (contador >= 0)

//3:
// Crie um programa de contagem regressiva. Peça um número e conte 
// deste número até 0, usando um loop while no console do navegador.

let numero = prompt(`Digite um número: `);
while(numero > 0){
    console.log(numero);
    numero --;
}
//while(numero >= 0)

//4:
// Crie um programa de contagem progressiva. Peça um número e conte 
// de 0 até esse número, usando um loop while no console do navegador.

let numero = prompt(`Digite um número: `)
//let contador = 0;
while(numero != 0){
    console.log(numero);
    numero ++;
}//while (contador <= numero)