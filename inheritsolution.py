class person:
	def eat(self):
		return "person is hungry"

class man(person):
	def run(self):
			return "man is running"

		# Example usage:
person1 = man()
print(person1.run())
print(person1.eat())

