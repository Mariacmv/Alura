package desafios;
import java.util.Scanner;

public class Tabuada {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número: \n");
        float numero = scanner.nextFloat();

        int aux = 0;
        while (aux < 11){
            float calculo = numero * aux;
            System.out.printf("%.2f * %d = %.2f\n", numero, aux, calculo);
            aux++;
        }
        scanner.close();
    }
}
