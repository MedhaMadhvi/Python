# Write a Python program to create a class named Book with attributes title, author and price. Implement methods to display the book’s information and apply a discount on the price. Also, implement a subclass named EBook with an additional attribute format. Override the display method for the EBook subclass.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price:}"

    def apply_discount(self, discount):
        self.price -= self.price * discount

class EBook(Book):
    def __init__(self, title, author, price, format):
        super().__init__(title, author, price)
        self.format = format

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price:}, Format: {self.format}"

print("Enter book details:")
title = input("Enter title: ")
author = input("Enter author: ")
price = float(input("Enter price: "))
book = Book(title, author, price)

print("Book Information:")
print(book.display_info())

discount = float(input("Enter the discount) / 100
book.apply_discount(discount)
print("Discount applied.")

print("Updated Book Information:")
print(book.display_info())

print("Enter eBook details:")
title = input("Enter title: ")
author = input("Enter author: ")
price = float(input("Enter price: "))
format = input("Enter format: ")
ebook = EBook(title, author, price, format)

print("EBook Information:")
print(ebook.display_info())