class Queue:
      '''
      " Zasada FIFO (First In - First Out)
      - sprawdzenie czy kolejka jest pusta (is_empty)
      - dodanie elementu do końca kolejki ( enqueue )
      - usuwanie elementu z początku kolejki ( dequeue )
      - sprawdzenie jaki element znajduje się na początku kolejki
      ( peek )
      '''
      def __init__(self):
            self.queue = []

      def is_empty(self):
            return len(self.queue) == 0
      
      def enqueue(self, item):
            self.queue.append(item)
      
      def dequeue(self):
            if not self.is_empty():
                  return self.queue.pop(0)
      
      def peek(self):
            if not self.is_empty():
                  return self.queue[0]
            
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())

