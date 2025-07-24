package desafios;

public class Desconto {
    public static void main(String[] args){
        double precoOriginal = 10.20;
        double percentualDesconto = 0.1;
        String oDesconto = "10%";

        double desconto = precoOriginal * percentualDesconto;

        double precoFinal = precoOriginal - desconto;
        System.out.println("Preço cheio: " +precoOriginal);
        System.out.println(String.format("Aplicando desconto de %s" ,oDesconto));
        System.out.println(String.format("Preço com desconto: %.2f" ,precoFinal));
    }
}
