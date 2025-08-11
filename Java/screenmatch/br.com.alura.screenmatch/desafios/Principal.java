package screenmatch.br.com.alura.screenmatch.desafios;
import Pessoa from desafios;

public class Principal {
    public static void main(String[] args) {
        ArrayList<Pessoa> listaDePessoas = new ArrayList<>();

        Pessoa pessoa1 = new Pessoa("Maria", 21);
        Pessoa pessoa2 = new Pessoa("Clara", 20);
        Pessoa pessoa3 = new Pessoa("Monal", 6);

        listaDePessoas.add(pessoa1);
        listaDePessoas.add(pessoa2);
        listaDePessoas.add(pessoa3);

        System.out.printf("%d", listaDePessoas.size());
        System.out.println("1º pessoa: %s", listaDePessoas.get(0));
        System.out.println("Lista completa: ");
        for (Pessoa pessoa : listaDePessoas) {
            System.out.println(pessoa);
        }
    }
}
