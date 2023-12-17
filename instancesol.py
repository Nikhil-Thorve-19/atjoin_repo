class Book:
    def __init__(self, book_name,num):
        self.book_name = book_name
        self.num=num
        

    def pages(self):
        print("book name",self.book_name)
        print("page no:", self.num)

# Creating an instance of the Book class
b1= Book("Rich Dad",20)
b1.pages()
