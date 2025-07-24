package desafios;

public class Conversao {
    public static void main(String[] args){
        double valorEmDolares = 250;
        double valorEmReais = valorEmDolares * 4.94;

        System.out.println(String.format("Valor %.2f em reais -> %.2f",valorEmDolares,valorEmReais));
    }
}
