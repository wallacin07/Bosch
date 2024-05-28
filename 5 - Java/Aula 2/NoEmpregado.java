class NoEmpregado
{
    // Atributo next
    private NoEmpregado next = null;
    NoEmpregado getNext() 
    {
        return next;
    }
    void setNext(NoEmpregado next)
    {
        this.next = next;
    }

    // Atributo Empregado
    private Empregados value;
    Empregados getEmpregado() 
    {
        return value;
    }

    // Construtor
    NoEmpregado(Empregados value) 
    {
        this.value = value;
    }
}
