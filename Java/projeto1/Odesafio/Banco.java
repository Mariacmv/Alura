package Odesafio;
import java.util.Scanner;

public class Banco {
   public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int escolha;
    String cliente = "Maria";
    String conta = "Corrente";
    float saldo = 2500;
    do{
        System.out.printf("""
        **************************************
            Dados iniciais do cliente:

            Nome: %s
            Tipo conta: %s
            Saldo Inicial: R$ %.2f
        **************************************
        """,cliente, conta, saldo);
        System.out.println("""
        Operações 
        1- Consultar saldos
        2- Receber valor
        3- Transferir valor
        4- Sair
        """);
        System.out.println("Digite a opção desejada: ");
        escolha = scanner.nextInt();

        switch(escolha){
            case 1:
                System.out.printf("O valor do saldo é: R$ %.2f\n\n", saldo);
                break;
            case 2:
                System.out.println("Informe o valor a receber: ");
                float valorAReceber = scanner.nextFloat();
                saldo += valorAReceber;
                System.out.printf("Saldo atualizado: R$ %.2f\n\n", saldo);
                break;
            case 3:
                System.out.println("Informe o valor que deseja transferir: ");
                float transfere = scanner.nextFloat();
                if (transfere > saldo){
                    System.out.println("Não há saldo suficiente");
                } else{
                    saldo -= transfere;
                    System.out.printf("Valor transferido: %.2f", transfere);
                    System.out.printf("\nSaldo final: %.2f\n\n", saldo);
                }
                break;
            case 4:
                System.out.println("Saindo...");
                break;
            default:
                System.out.println("Opção inválida");
        }
    } while (escolha != 4);
    scanner.close();
    }
}
