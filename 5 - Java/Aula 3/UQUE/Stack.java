public class Stack<T>
{
    // push pop peek size
    // array dinamico
    T[] data;
    Integer size = 0;
    Stack()
    {
        data = (T[])(new Object[10]);
    }
    
    Stack( int capacity )
    {
        data = (T[])(new Object[capacity]);
    }

    public void push( T value )
    {
        if ( size == data.length )
        {
            T[] copy = (T[])( new Object[ data.length * 2 ]);
            for( int i = 0 ; i < size ; i++ )
            {
                copy[i] = this.data[i];
            }
        }
        this.data[size] = value;
        this.size++;
    }

    public void pop(){
        if(this.size > 0)
        {
            this.data[this.size] = null;
            this.size--;
        }
    }

    public T peek()
    {
        return this.data[this.size];
    }

    public Integer getSize()
    {   
        return this.size;    
    }
}
