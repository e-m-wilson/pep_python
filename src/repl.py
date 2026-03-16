from src.books.book import Book
from src.books.book_service import BookService
from src.books.book_repository import BookRepository

class BookREPL:
    def __init__(self, book_svc):
        self.running = True
        self.book_svc = book_svc

    def start(self):
        print('Welcome to the book app! Type \'Help\' for a list of commands!')
        while self.running:
            cmd = input('>>>').strip()
            self.handle_command(cmd)

    def handle_command(self, cmd):
        if cmd == 'exit':
            self.running = False
            print('Goodbye!')
        elif cmd == 'addBook':
            self.add_book()
        elif cmd == 'getBooks':
            self.get_all_books()
        elif cmd == 'help':
            print('Available commands: addBook, getBooks, help, exit')

    def add_book(self):
        try:
            print('Enter book details:')
            title = input('Title: ')
            author = input('Author: ')
            book = Book(title=title, author=author)
            new_book_id = self.book_svc.add_book(book)
            print(new_book_id)
        except Exception as e:
            print(f'An unexpected error has occurred: {e}')

    def get_all_books(self):
        books = self.book_svc.get_all_books()
        print(books)

if __name__ == '__main__':
    repo = BookRepository('books.json')
    book_service = BookService(repo)
    repl = BookREPL(book_service)
    repl.start()
