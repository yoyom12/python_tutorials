
# t = (1,5,6,9)
# print(type(t))
# print(t[0])
# print(t[1])
# print(t[2])
# print(t)

# if 5 in t:
#     print("S")
# else:
#     print("no")


# t2 = t[1:4]
# print(t2)



kontris = ("inia","hungary","thialan", "portugiz", "norway")
# print(k) 

# rs = k.count("inia")
# print(rs)

# i = k.index("hungary")
# print(i)


tmp = list(kontris)
tmp.append("russia")
tmp.pop(3)
tmp[2] = "finlan"
kontris = tuple(tmp)
print(kontris)