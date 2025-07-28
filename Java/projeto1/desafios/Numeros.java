/*Crie um programa que solicite ao usuário digitar um número. Se o número for positivo, exiba "Número positivo", caso contrário, 
exiba "Número negativo". */
package desafios;
import java.util.Scanner;

public class Numeros {
    public static void main(String[] args){
        Scanner numeros = new Scanner(System.in); 
        System.out.println("Digite um número: ");
        int numero = numeros.nextInt();

        if (numero > 0){
            System.out.printf("O número %d é positivo.", numero);
        } else if(numero < 0){
            System.out.printf("O número %d é negativo.", numero);
        } else if(numero == 0){
            System.out.printf("O número é igual a 0");
        }
        numeros.close();
    }
}
