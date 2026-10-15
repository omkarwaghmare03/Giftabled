class Automobile:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour



    def start(self):
        print(self.brand, self.colour, "has started")


    def stop(self):
        self.speed= 0
        print(self.brand, self.colour, "has stopped")




class car(Automobile):
   def __init__(self, brand, colour):
      super().__init__(brand, colour)



car1= car("Audi", "White")


print("car details")

car1.start()
car1.stop()