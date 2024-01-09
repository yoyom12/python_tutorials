class managr:
    name = "parth"
    def __len__(self): #  __len__ is builtin fun like __init__ fun whic help to  print the length of the string
        i = 0
        for i in self.name:
            i = i + 1
        return i


    def __str__(self):
        return(f"the name of managr is {self.name} str ")

    def __repr__(self):
        return(f"the name of managr is {self.name} repr")