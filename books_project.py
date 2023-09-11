class Book:
    def __init__(self, title, author, price, publish):
        self.book_title = title
        self.book_author = author
        self.book_price = price
        self.book_publish = publish

        
    def add_book(self):
        print("book title: " + self.book_title)
        print("book author: " + self.book_author)
        print("book price: " + str(self.book_price))
        print("book publish date: " + self.book_publish)
        print("book added")
       
        

book1 = Book("i am number four", "jobie hughes and james frey", + 15, "august 3rd, 2010")
book1.add_book()

print("this book was published 13 years ago")

book2 = Book("divergent", "veronica roth", + 17, "april 26th, 2011")
book2.add_book()

print("this book was published 12 years ago")

