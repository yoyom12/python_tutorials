class vector:
    def __init__(self,i,j,k) -> None:
        self.i = i 
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return vector(self.i + x.i, self.j + x.j, self.k + x.k)
    

o1 = vector(2,3,5)
print(o1)

o2 = vector(4,5,6)
print(o2)

print(o1+o2)