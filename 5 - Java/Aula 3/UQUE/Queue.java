public class Queue<T>
{
    // enqueue(enfia) dequeu(desfia) peek size    
    NodeQueue<T> head = null;
    NodeQueue<T> tail = null;
    Integer size = 0;
    
    public void enqueue( T value )
    {
        NodeQueue<T> node = new NodeQueue<T>( value );
        this.size++;
        if( this.head == null )
        {
            this.head = node;
            this.tail = node;
            return;
        }
        NodeQueue<T> current = head;
        while( current.getNext() != null )
        {
            current = current.getNext();
        }
        current.setNext(node);
        current.setPrev(this.tail);
        this.tail = current.getNext();
    }

    public T dequeue()
    {
        T current = null;
        if( head != null )
        {
            this.head = head.getNext();
            current = head.getValue();
        }
        return current;
    }

    public T peek()
    {
        return head.getValue();
    }

    public Integer getSize()
    {
        return this.size;
    }


}
