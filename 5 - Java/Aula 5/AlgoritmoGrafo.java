import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class AlgoritmoGrafo {
    
    
    int i = 0;
    
    void leitor() throws IOException{
        String[] texto = new String[4];
        FileReader arq = new FileReader("Desafio1.txt");
        BufferedReader lerArq = new BufferedReader(arq);
        String linha = lerArq.readLine();
        texto[1] = linha; 
        while (linha != null) {
            linha = lerArq.readLine(); 
            i++;
            texto[i] = linha;
          }
    lerArq.close();

    
}


        }

