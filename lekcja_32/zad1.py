from stos import Stack

'''
Utwórz symulator przeglądarki gdzie historia przeglądania będzie zapisywana w
formie stosu. 

Użytkownik może wchodzić na różne strony w programie i cofać się
w historii przeglądania.
'''

class BrowserHistory:
      def __init__(self):
            self.history = Stack()
            self.current_page = None

      def go_to_page(self, url):
            self.history.push(self.current_page)
            self.current_page = url

      def go_back(self):
            previous_page = self.history.pop()
            if previous_page is not None:
                  self.current_page = previous_page

      def print_history(self):
            print("Current page: ", self.current_page)
            print("History:")
            for page in reversed(self.history.stack):
                  print(page)

historia = BrowserHistory()

historia.go_to_page("Google.com")
historia.go_to_page("Google.com/kot")
historia.go_to_page("Google.com/kot/brytyjski")
historia.print_history()
print("=====")
historia.go_back()
historia.go_back()
historia.go_to_page("Google.com/pies")
historia.print_history()




