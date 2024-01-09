class animals:
    def __init__(self,color) -> None:
        pass

    def show(self):
        print(f"\nThe color of the dog is {self.color}")

        

class dog(animals):
    def __init__(self,breed,name) -> None:
       pass

    def show(self):
        animals.show(self)
        print(f"The breed of dog is {self.breed} & name is {self.name}\n")


class animaldog(dog):
    def __init__(self ,color,name,breed) -> None:
        self.color = color
        self.name = name
        self.breed = breed
        
       
    def show(self):
        dog.show(self)
        

a = animaldog("blak","yash","grman")
a.show()