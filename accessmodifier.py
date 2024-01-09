class employ:
    def __init__(self):
        # self.nam = "parth"
        self.__nam = "parth" #if i can use '__' then it cant be aaccess

a = employ()

# print(a.__nam) # cant be access directly 
print(a._employ__nam) # can be access using this

print(a.__dir__())