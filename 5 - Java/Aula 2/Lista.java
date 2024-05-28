

public class Lista {
    private NoEmpregado head = null;
    private int size = 0;
    private int contador = 0;
    void add(Empregados empregado)
    {
        size++;
        NoEmpregado no = new NoEmpregado(empregado);
        if (head == null) 
        {
            head = no;
            return; 
        }

        NoEmpregado atual = head;
        while (atual.getNext() != null) 
        {
            atual = atual.getNext();  
        }
        atual.setNext(no);
    }


    // public int verifyAccess(String cpf, String password) {
        
    //     NoEmpregado current = head;
        
    //     while (!current.getValue().getCpf().equals(cpf)) {
    //         if (current.getValue().getCpf().equals(cpf)) {
    //             System.out.println("\n é esse campeao");
    //             break;
    //         }
    //         System.out.println("\n nao é esse");
    //         current = current.getNext();
            
    //     }
        
    //     return current.getValue().getAdmin();

    Empregados get(int index)
    {
        contador = 0;
        NoEmpregado atual = head;
        if (index > size) 
        {
                
        }
        while (contador != index) 
        {
            atual = atual.getNext();
            contador++; 
        }
        return atual.getEmpregado();

    }

    int getSize()
    {
        return this.size;
    }
}
