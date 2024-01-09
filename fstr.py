a = "my name is {} I am from {}"
name = "parth"
country = "india"
prize = 498.856856
print(a.format(name,country))

print(f"my name is {name} I am from {country}")

b = f"the prize money is Rs {prize:.2f}"
print(b)
b = f"the prize money is Rs {prize:.3f}"
print(b)