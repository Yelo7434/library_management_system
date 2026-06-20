"""
Date: 18 January 2021
Author: Sanam Kandar
Project: Student Library Management System
"""

class Person:
    """Base class for all people in the library system."""
    def __init__(self, name):
        self.name = name
    def display_role(self):
        print(f"{self.name} is a person.")

class Library:
    """Handles all library operations."""
    def __init__(self, books):
        self.books = books
        self.borrowed_books = []  # Encapsulation: replaces global track variable
    def display_available_books(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS:")
        for book in self.books:
            print(f" ♦-- {book}")
        print()
    def borrow_book(self, student_name, book_name):
        if book_name not in self.books:
            print(
                f"{book_name} is not available. It may already be borrowed.\n"
            )
        else:
            self.borrowed_books.append(
                {"student": student_name, "book": book_name}
            )
            self.books.remove(book_name)
            print("BOOK ISSUED: Please return it on time.\n")
    def return_book(self, student_name, book_name):
        record = {"student": student_name, "book": book_name}
        if record in self.borrowed_books:
            self.borrowed_books.remove(record)
            self.books.append(book_name)
            print("BOOK RETURNED: Thank you!\n")
        else:
            print("No matching borrowing record found.\n")
    def donate_book(self, book_name):
        self.books.append(book_name)
        print("BOOK DONATED: Thank you for your contribution!\n")
    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("NO BOOKS ARE CURRENTLY ISSUED.\n")
            return
        for record in self.borrowed_books:
            print(f"{record['book']} is issued to {record['student']}.")
        print()

class Student(Person):
    """Student class derived from Person."""
    def display_role(self):
        print(f"{self.name} is a student.")
    def request_book(self):
        print("So, you want to borrow a book!")
        return input("Enter book name: ")
    def return_book(self):
        print("So, you want to return a book!")
        student_name = input("Enter your name: ")
        book_name = input("Enter book name: ")
        return student_name, book_name
    def donate_book(self):
        print("You want to donate a book!")
        return input("Enter book name: ")

class Librarian(Person):
    """Librarian class derived from Person."""
    def display_role(self):
        print(f"{self.name} is the librarian.")

def main():
    delhi_library = Library(
        [
            "vistas",
            "invention",
            "rich&poor",
            "indian",
            "macroeconomics",
            "microeconomics",
        ]
    )
    student = Student("Guest")

    print("\t\t♦♦♦ WELCOME TO THE DELHI LIBRARY ♦♦♦\n")

    while True:
        print(
            """
1. List all books
2. Borrow a book
3. Return a book
4. Donate a book
5. Track borrowed books
6. Exit
"""
        )

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                delhi_library.display_available_books()

            elif choice == 2:
                name = input("Enter your name: ")
                book = student.request_book()
                delhi_library.borrow_book(name, book)
            elif choice == 3:
                name, book = student.return_book()
                delhi_library.return_book(name, book)
            elif choice == 4:
                book = student.donate_book()
                delhi_library.donate_book(book)
            elif choice == 5:
                delhi_library.display_borrowed_books()
            elif choice == 6:
                print("THANK YOU! Visit Again.")
                break
            else:
                print("INVALID CHOICE!\n")

        except ValueError:
            print("Please enter numbers only.\n")

if __name__ == "__main__":
    main()