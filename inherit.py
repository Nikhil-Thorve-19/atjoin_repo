class animal:
 def run(self):
   print("animal run")

    
 def eat(self):
    print ("animal eat")

class dog(animal):
    def breed(self):
        print("animal breed is golden retriver")



obj=dog()
obj.run()
obj.eat()

obj.breed()