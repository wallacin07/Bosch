public class NodeQueueW<E> {
   
    private NodeQueueW<E> next =  null;
    private NodeQueueW<E> prev = null;

    NodeQueueW<E> getNext()
    {
        return next;
    }

    void setNext(NodeQueueW<E> next)
    {
        this.next = next;
    }

    NodeQueueW<E> getPrev()
    {
        return prev;
    }

    NodeQueueW<E> setPrev(NodeQueueW<E> prev)
    {
        this.prev = prev;
        return this.prev;
    }


    private E value;

    E getValue()
    {
        return value;
    }

    NodeQueueW(E value)
    {
        this.value = value; 
    }

}
