import reduce

l = [2,7,6,9,5,96,56]

def sum(x,y):
    return x+y

s = reduce(sum,l)

print(s)