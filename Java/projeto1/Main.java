public class Main{
    public static void main(String[] args){
        System.out.println("Klisten");
        System.out.println("Música: I need the Light");

        //definindo algumas variáveis
        //int ano = 2022; //definindo fixamente
        int anoDeLancamento = 2022;
        //concatenação
        System.out.println("Ano de lançamento: " +anoDeLancamento);
        boolean incluidoNoPlano = true;
        int notaMusica = 10;

        double media = (9.8 + 6.3 + 8.6) / 3;
        System.out.println("Média: " +media);

        String dados;
        /*dados = "Música do grupo Enhypen";
        System.out.println(dados);*/
        dados = """
                Música I need the light
                Artista Enhypen
                Ano de lançamento: """ +anoDeLancamento; //permite concatenar também
        System.out.println(dados);
    }
}