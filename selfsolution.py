class Car:
    def __init__(nikhil, model, color, name):
        nikhil.model = model
        nikhil.color = color
        nikhil.name = name

    def start_engine(nikhil):
        return f"The {nikhil.color} car with model {nikhil.model} is starting its engine. Company name is {nikhil.name}"

# Example usage:
my_car = Car("Sedan", "Blue", "Maruti")
print(my_car.start_engine())
