'''
1. Program : you're building a program to manage a library. One common task in a library system is to check out books to patrons. You can create a function called check_out_book to handle this task. This function might take parameters such as the book to be checked out, the patron who is checking out the book, and the due date for returning the book. Here's how you could implement this function:
python
'''
# Define the Book class
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
    
    def is_available(self):
        return self.available
    
    def check_out(self, patron, due_date):
        if self.available:
            self.available = False
            self.checked_out_by = patron
            self.due_date = due_date
            return True
        else:
            return False

# Function to check out a book
def check_out_book(book, patron, due_date):
    if book.is_available():
        if book.check_out(patron, due_date):
            print(f"Book '{book.title}' checked out to {patron} until {due_date}.")
        else:
            print(f"Sorry, '{book.title}' is not available for checkout.")
    else:
        print(f"Sorry, '{book.title}' is not available for checkout.")

# Create a Book instance
book_to_check_out = Book("Python Programming", "Guido van Rossum")

# Example usage
patron = "John Doe"
due_date = "2024-02-28"
check_out_book(book_to_check_out, patron, due_date)
