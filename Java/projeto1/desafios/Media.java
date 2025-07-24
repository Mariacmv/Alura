package desafios;

public class Media {
    public static void main(String[] args){
        double nota1, nota2;
        double media; 
        nota1 = 8.5;
        nota2 = 10;
        media = (nota1 + nota2)/2;
        System.out.println(String.format("A média de %.2f e %.2f é: %.2f" ,nota1, nota2, media));
    }
}
