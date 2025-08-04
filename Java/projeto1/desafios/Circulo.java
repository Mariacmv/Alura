package desafios;
import java.util.Scanner;

public class Circulo {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Escolha: ");
        System.out.println("1. Calcular área do quadrado");
        System.out.println("2. Calcular área do círculo");
        int escolha = scanner.nextInt();

        switch(escolha){
            case 1:
                System.out.println("Digite o lado do quadrado: ");
                int lado = scanner.nextInt();
                float area = lado * lado;
                System.out.println("A área do quadarado é: " +area);
                break;
            case 2:
                System.out.println("Digite o raio do círculo: ");
                int raio = scanner.nextInt();
                double area_circulo = 3.14 * (raio * raio);
                System.out.println("A área do círculo é: " +area_circulo);
                break;
            default:
                System.out.println("Opção inválida");
                break;
        }
        scanner.close();
    }
}
