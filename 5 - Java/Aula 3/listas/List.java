//Array list.
public class List<T>
{
    //Atributos
    private T[] data;
    private Integer size = 0;
    

    //Metodo Construtor
    List()
    {
        data =(T[])(new Object[10]);
    }

    List(int capacity)
    {
        data = (T[])(new Object[capacity]);
    }


    //Funções ou Métodos
    void add(T value)
    {   
        if (size == data.length) 
        {
            T[] copy = (T[])(new Object[2* data.length]);
            for (int i = 0; i < size; i++) 
            {
                copy[i] = data[i];
            }
            data = copy;
        }

        data[size] = value;
        size++;
    }

    Integer size()
    {
        return this.size;
    }

    T get(int index)
    {
        if (index >= size) 
        {
            return null;
        }
        return this.data[index];
    }
}
