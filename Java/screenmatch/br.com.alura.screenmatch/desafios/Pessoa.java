package screenmatch.br.com.alura.screenmatch.desafios;

public class Pessoa {
    private String nome;
    private int idade;

    //inicializando variáveis
    public Pessoa(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    @Override
    public String toString() {
        return "Pessoa: " + nome + " (Idade: " + idade + ")";
    }
}
