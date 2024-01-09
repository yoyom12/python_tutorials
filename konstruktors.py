# for constructor
class man:
    def __init__(self,n, o):
        print("hi i am parth")
        self.name = n
        self.oupation = o 

    def info(self):
        print(f"{self.name} is a {self.oupation}")

a = man("parth","managr")
b = man("harshal","HR")
a.info()
b.info()
# s.name = "harshal"
# s.oupation = "HR"