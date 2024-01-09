class shap:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

rec = shap(2,5)
print(rec.area())