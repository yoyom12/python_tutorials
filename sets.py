# h = set()
# print(type(h))

s1 = {"parth",True, 2,4,5}
# print(type(s1))

# union & union-update
s2 = {"yash", 2,56,5}
# print(s1.union(s2))  # union
# s = s1.update(s2)   # union-update
# print(s1)

#  intersection & intersection-update
# s = s1.intersection(s2)
# s1.intersection_update(s2)
# print(s1)

# symmetric_difference
# s = s1.symmetric_difference(s2)
# s = s1.difference(s2)
# s = s2.difference(s1)
# print(s)

# isdisjoint() => no similarities in both sets
p = {"amria","inia","yahoo"}
q = {"amria","inia"}
# print(p.isdisjoint(q))

# issuperset => all element 2nd set, is all present in 1st set  
# print(p.issuperset(q))

# add in set & remove/discard is for remove the element
# q.add("russia")
# q.remove("amria")
# print(q)

# del for delete the set
del q
# print(q)

# clear the element from set
p.clear()
print(p)

# for val in s1:
#     print(val)