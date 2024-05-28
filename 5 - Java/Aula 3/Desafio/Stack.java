
public class Stack<E> 
{

    private E[] stack;
    private Integer size = 0;

    Stack()
    {
        stack = (E[])(new Object[10]);
    }

    Stack(Integer capacity)
    {
        stack = (E[])(new Object[capacity]); 
    }

    E push(E value)
    {
        if (size == stack.length) 
        {
            E[] copy = (E[])(new Object[2 * stack.length]);
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

    E pop()
    {
        E var;
        var = stack[size-1];
        stack[size-1] = null;
        return var;
    }

    E peek()
    {
        return stack[size-1];
    }

    Integer size()
    {
        return size;
    }

}
