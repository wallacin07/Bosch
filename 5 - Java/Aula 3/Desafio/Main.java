

public class Main {
    
    public static void main(String[] args) {
        // System.out.println("aaaaaaaaaaaa");
        
        QueueW<Integer> queue = new QueueW<>();

        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);

        System.out.println(queue.peek());
        queue.dequeue();
        System.out.println(queue.peek());
        queue.dequeue();
        System.out.println(queue.peek());
        
//--------------------------------------------------------------------------

        Stack<String> stack = new Stack<>();
        stack.push("Oi");
        stack.push("Olá");
        stack.push("Java eh rui");
        System.out.println(stack.peek());


    }

}
