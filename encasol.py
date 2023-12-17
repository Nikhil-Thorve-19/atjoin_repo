class Example:
	def __init__(self):
		self.__private_attribute = 42

	def __private_method(self):
		return "This method is encapsulated."

obj = Example()
obj.__private_method()
