# # class book:
#   def __init__(self,book_name):
#     self.book_name=book

#   def pages(self):
#     print("pages",self.num)

#   o=book("rich dad")
#   o.pages()
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

