
    public class Stack
{

    private Individuo[] stack;
    private Integer size = 0;

    Stack(Integer tolerantes, Integer copiadores, Integer trapaceiros, Integer rabugentos,Integer colaborativos)
    {
        this.stack = new Individuo[tolerantes + copiadores + trapaceiros + rabugentos+ colaborativos];
        int i=0,j = 0;
        for(; i<tolerantes;i++)
            stack[i] =new Tolerante("Tolerante"); 
        j +=tolerantes;
        for(; i <j+copiadores;i++)
            stack[i] = new Copiador("Copiador");
        j+= copiadores;
        for(;i<j+trapaceiros;i++)
            stack[i] = new Rabugento("Rabugento");
        j+= rabugentos;
        for(; i<j+colaborativos;i++)
            stack[i] = new Colaborativo("Colaborativo");
        size = j+colaborativos;    
    
    }

    Individuo push(Individuo value)
    {
        if (size == stack.length) 
        {
            Individuo[] copy = new Individuo[2 * stack.length];
            for (int i = 0; i < size; i++) 
            {
                copy[i] = stack[i];
            }
            stack = copy;
        }
        stack[size] = value;
        size++;

        return stack[size];
    }

    Individuo pop()
    {
        Individuo var;
        var = stack[size-1];
        stack[size-1] = null;
        return var;
    }

    Individuo peek()
    {
        return stack[size-1];
    }

    Integer size()
    {
        return size;
    }

}

