import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;


public class Main {
  public static void main(String[] args) throws IOException{
    
    lerArquivo();
  }

  static void lerArquivo() throws IOException{
    int i = 0;
    String[] texto = new String[5];
    Integer[] pais = new Integer[5];

    System.out.printf("\nConteúdo do arquivo texto:\n");
      FileReader arq = new FileReader("desafio1.txt");
      BufferedReader lerArq = new BufferedReader(arq);

        String linha = lerArq.readLine();
        String[] line = linha.split(" ");
        texto[i] = line[0];
        while (linha != null) {
          linha = lerArq.readLine();
          if (linha != null) {
            line = linha.split(" ");
            i++;
            texto[i] = line[0];
          }
        }
          for (int j = 0; j < texto.length-1; j++) {
            // System.out.println(texto[j]);
            pais[j] = Integer.parseInt(texto[j]);
          }
          int a, b;
          for (a = 0; a < pais.length-2; a++) {
            for (b = a + 1; b < pais.length-1; b++) {
              if ( pais[b] < pais[a]) {
                int auxiliar1 = pais[a];
                int auxiliar2 = pais[b];
                pais[a] = auxiliar2;
                pais[b] = auxiliar1;
        
              }
              
            }
          }
          for (int j = 0; j < pais.length-1; j++) {
            System.out.println(pais[j]);
          }
            lerArq.close();


  }
}

