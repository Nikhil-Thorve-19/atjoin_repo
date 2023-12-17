class android:
    def mi(self):
        print("this is mitv")

class tv(android):
    def sony(self):
        print("this is sonytv")
    
    def mi(self):
        super().mi()
        print("this is mi tv")

obj=tv()
obj.sony()
obj.mi()

