class man:
    name = "parth"
    oupation= "softwar"
    ntworth = 19
    def info(self):
        print(f"{self.name} is a {self.oupation}")

a = man()
b = man()
a.name = "shubham"
a.oupation = "writr"
print(a.name,a.oupation)

b.name = "nitika"
b.oupation = "HR"
a.info()
b.info()