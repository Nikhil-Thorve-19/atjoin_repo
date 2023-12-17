class Car:
    def __init__(self,model,color):
        self.model=model
        self.color=color

    def start_engine(self):
        print(f"this is {self.model} color is {self.color}")
    

obj=Car("mahindra","white")
obj.start_engine()


