my = {
    "nam" : "parth",
    "ag" :18 ,
    "liv" : "nasahik"
}
# print(my["ag"]) # throw error
print(my.get("ag")) #  not throw error

print(my.values())

for k in my.keys():
    print(my[k]) 

'''
p1 = { 123: 70, 536: 69, 85: 96 }
p2 ={ 222: 98, 527:23,852:63}
# p1.update(p2)

# p2.clear()
# print(p2)

# p1.pop(123) # remove given item
p1.popitem() # remove last item
print(p1)'''