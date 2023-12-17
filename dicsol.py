# class Student:
# 	def __init__(self, details):
# 		self.name = details['name']
# 		self.age = details['age']


# 		# Example usage:
# student_details = {'name': 'Alice', 'age': 15}
# alice = Student(student_details)

class Book1:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Book 1: {self.title} by {self.author}, Pages: {self.pages}")

# Creating instances of the Book class with different attributes
book1 = Book1("The Hobbit","J.R.R. Tolkien",295)

