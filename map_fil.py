# MAP
def sq(x):
    return x*x

l = [2,7,6,9,5,96,56]

nl = list(map(sq, l))
print(nl)

# FILTER
def filter_fun(a):
    return a>4

nf = list(filter(filter_fun,l))
print(nf)
