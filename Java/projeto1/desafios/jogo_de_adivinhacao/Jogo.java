import java.util.Random;
import java.util.Scanner;

public class Jogo{
    public static void main(String[] args){
        int numero = new Random().nextInt(100);
        Scanner palpite = new Scanner(System.in);

        int contador = 0;
        while (contador != 5){
            System.out.println("\nDigite seu palpite: ");
            int adivinha = palpite.nextInt();

            if (adivinha == numero){
                System.out.printf("Parabéns, você acertou o número: %d. Você acertou em %d tentativas.", numero, contador+1);
                break;
            } else if (adivinha > numero){
                System.out.println("Número muito alto. Tente novamente!");
            } else if (adivinha < numero){
                System.out.println("Número muito baixo. Tente novamente!");
            } else{
                System.out.println("Valor inválido!");
            }
            contador++;
            System.out.printf("Tentativas restantes: %d\n", 5 - contador);
        } 
        if (contador == 5){
                System.out.printf("Fim do jogo. A resposta era: %d.", numero);
        }
    palpite.close();
    }
}