public class Condicional{
  public static void main(String[] args){
    int anoDeLancamento = 2022;
    boolean incluidoNoPlano = true;
    double notaDoFIlme = 8.1;
    String tipoPlano = "plus";
    
    if (anoDeLancamento >= 2022){
      System.out.println("Lançamento que os clientes estão curtindo!");
    } else{
      System.out.println("Filme retrô que vale a pena assistir!");
    }

    if (incluidoNoPlano || tipoPlano.equals("plus")){ //ou if (incluidoNoPlano == true) mas o ideal é com equals()
      System.out.println("Filme liberado");
    } else{
      System.out.println("Deve pagar a locação");
    }
  }
}