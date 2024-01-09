class manar:
    company = "googl"
    def show(self):
        print(f"the name is {self.name} work in {self.company}")
    
    @classmethod
    def changcompany(cls, nwcompany):
        cls.company = nwcompany
    
a1 = manar()
a1.name = "parth"
a1.show()
a1.changcompany("JP Morgan")
a1.show()