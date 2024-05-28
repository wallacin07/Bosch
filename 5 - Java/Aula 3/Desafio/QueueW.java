public class QueueW <E>
{
    private NodeQueueW<E> head = null;
    private NodeQueueW<E> tail = null;
    private Integer size = 0;

    void enqueue(E value)
    {
        size++;
        NodeQueueW<E> node = new NodeQueueW<E>(value);
        if (head == null) 
        {
            head = node;
            tail = node;    
        }
        NodeQueueW<E> current = head;
        // if (current.getPrev() == null) 
        // {
        //     current = current.setPrev(node);    
        // }
        // head = current;
        if(current.getPrev() != null) 
        {
            current = current.getPrev();    
        }
        current.setPrev(node);    
        head = node;
    
    }

    E dequeue()
    {
        E lastTail = tail.getValue();
        tail = tail.getPrev();
        return lastTail;
    }

    E peek()
    {
        return tail.getValue();
    }

    Integer size()
    {
        return size;
    }
}
