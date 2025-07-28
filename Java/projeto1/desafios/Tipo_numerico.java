/*Peça ao usuário para inserir dois números inteiros. Compare os números e imprima uma mensagem indicando se são iguais, diferentes,
o primeiro é maior ou o segundo é maior. */
package desafios;
import java.util.Scanner;

public class Tipo_numerico {
    public static void main(String[] args){
        Scanner numeros = new Scanner(System.in);
        System.out.println("Digite um número inteiro: ");
        int numero1 = numeros.nextInt();
        System.out.println("Digite outro número inteiro: ");
        int numero2 = numeros.nextInt();

        if (numero1 == numero2){
            System.out.printf("Os números %d e %d são iguais.", numero1, numero2);
        } else if(numero1 != numero2){
            System.out.printf("Os números %d e %d são diferentes.", numero1, numero2);
            if(numero1 > numero2){
                System.out.printf("O número %d é maior que %d.", numero1, numero2);
            } else if(numero2 > numero1){
                System.out.printf("O número %d é maior que %d.", numero2, numero1);
            }
        }
        numeros.close();
    }
}
