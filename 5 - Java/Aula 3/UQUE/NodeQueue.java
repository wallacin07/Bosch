public class NodeQueue<T> 
{
    NodeQueue<T> next = null;
    NodeQueue<T> prev = null;
    T value = null;

    public NodeQueue<T> getNext() 
    {
        return next;
    }
    public void setNext(NodeQueue<T> next) 
    {
        this.next = next;
    }
    public NodeQueue<T> getPrev() 
    {
        return prev;
    }
    public void setPrev(NodeQueue<T> prev) 
    {
        this.prev = prev;
    }

    public T getValue() {
        return this.value;
    }
    NodeQueue( T value ) 
    {
        this.value = value;
    }
    
}
