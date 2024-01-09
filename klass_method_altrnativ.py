class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"th anm is {self.name} & ag is {self.age}")

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],string.split("-")[1])

a = students("parth",45)
# print(a.name)
# print(a.age)

string = "john-42" #if i gt input in string format then i want to create fromstr fun to gt propr values from given string
b = students.fromStr(string)
# print(b.name)
# print(b.age)