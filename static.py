class math:
    @staticmethod
    def add(a,b): #by using staticmethod as decorator it not require self argument
        return (a+b)/2

a = math()
print(a.add(4,5))