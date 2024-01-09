class my:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"valu is {self._value} ")
    
    # getter
    @property
    def Xvalue(self):
        return 5*self._value
        
    # setter
    @Xvalue.setter
    def Xvalue(self,nw_valu):
        self._value = nw_valu*5
    
n = int(input("no."))

# getter
obj = my(1)

obj.Xvalue = n
print(obj.Xvalue)
obj.show()