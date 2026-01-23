from queue import Queue

'''
Utwórz symulator kolejki do kina gdzie elementami kolejki są klienci razem z ich
zamówieniem. 
Do utworzenia symulatora kolejki użyj naszej struktury Kolejki, którą
stworzyliśmy wcześniej.
'''

class Customer:
      def __init__(self, name, order):
            self.name = name
            self.order = order

class CinemaQueue:
      """
      add_customer
      remove_customer
      next_customer_order
      """
      def __init__(self):
            self.queue = Queue()

      def is_empty(self):
            return self.queue.is_empty()

      def add_customer(self, customer):
            self.queue.enqueue(customer)

      def remove_customer(self):
            if not self.queue.is_empty():
                  return self.queue.dequeue()
      
      def next_customer_order(self):
            if not self.queue.is_empty():
                  next_customer = self.queue.peek()
                  return next_customer.order
            
queue = CinemaQueue()

queue.add_customer(Customer("Ania", "popcorn"))
queue.add_customer(Customer('Tomek', "cola"))
queue.add_customer(Customer("Karol", "hot dog"))

while not queue.is_empty():
      next_customer = queue.remove_customer()
      print(f"Obsługujemy klienta {next_customer.name}, który zamówił {next_customer.order}")
