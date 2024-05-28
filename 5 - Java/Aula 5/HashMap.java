public class HashMap<K,V> {

    EntradaValores<K,ArrayDinamico<V>>[] tabela;
    Integer capacidade;
    Integer tamanho = 0;

    void ajustandoCapacidade(Integer capacidade)
    {
        this.capacidade = capacidade;
        this.tabela = (EntradaValores<K,ArrayDinamico<V>>[])(new Object[capacidade]);
        this.tamanho = 0;
    }


    // Integer hash(K chave)
    // {
    //     if (chave == null) 
    //         return 0;
        
    //     return Math.abs(chave.hashCode()%capacidade);
    // }


    void colocarValor(K chave, V valor){
        for (int i = 0; i < tabela.length; i++) {
            if (tabela[i].chaves == chave) 
            {
                tabela[i].valores.add(valor);
            }
        tabela[tamanho].chaves = chave;
        tabela[tamanho].valores.add(valor);
        tamanho++;
        }
    }

    void pegarValores(K chave)
    {
        for (int i = 0; i < tabela.length; i++) {
            if (tabela[i].chaves == chave) {
                    tabela[i].valores.get();  
            }
        }
    }
    
    void removerValores(){

    }

//Construtor
    HashMap()
    {
        this.tabela = (EntradaValores<K,ArrayDinamico<V>>[])(new Object[8]);
    }

}
