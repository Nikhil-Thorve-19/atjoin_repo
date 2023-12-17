class Android:
	def samsung(self):
		return "this is android phone"

class Ios(Android):
	def samsung(self):
		return "this is sansung phone"

		# Example usage:
	def iphone13(android):
		return "this is ios phone version13"

my_phone = Ios()
print(my_phone.iphone13())
print(my_phone.samsung())


