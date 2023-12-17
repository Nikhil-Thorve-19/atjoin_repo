# class Car:
#     def __init__(self, model, color, name):
# 	    self.model = model
# 	    self.color = color
#         self.name = name

#     def start_engine(self):
# 	   return f"The {self.color} car with model {self.model} is starting its engine.company name is{self.name}"

# 		# Example usage:
# my_car = Car("Sedan", "Blue","Maruti")
# print(my_car.start_engine())

class Car:
    def __init__(self, model, color, name):
        self.model = model
        self.color = color
        self.name = name

    def start_engine(self):
        return f"The {self.color} car with model {self.model} is starting its engine. Company name is {self.name}"

# Example usage:
my_car = Car("Sedan", "Blue", "Maruti")
print(my_car.start_engine())

