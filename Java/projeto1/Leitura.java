import java.util.Scanner;

public class Leitura {
    public static void main(String[] args){
        Scanner leitura = new Scanner(System.in); //leitura do teclado do usuário

        System.out.println("Digite seu filme favorito: ");
        String filme = leitura.nextLine();

        System.out.println("Qual o ano de lançamento: ");
        int anoDeLancamento = leitura.nextInt(); //nextInt porque é inteiro

        System.out.println("Diga sua avaliação para o filme: ");
        double avaliacao = leitura.nextDouble();

        System.out.println(filme);
        System.out.println(anoDeLancamento);
        System.out.println(avaliacao);
    }
}
