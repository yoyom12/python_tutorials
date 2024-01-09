# x = (1,2,3)
# print(dir(x)) # dir is used to get the object & method from tuple/list/dictionary & so on

# print(x.__add__)

class prson:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
p = prson("parth",10000000)
print(p.__dict__)  # __dict__ is used for convert in into dictionary

print(help(prson)) # help is get information of any class/method/any type of fun