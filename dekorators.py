def greet(fx):
    def mfx(*args,**kwargs): # *args & **kwargs are useful to taking arguments as greet function
        print("Good Morning")
        fx(*args,**kwargs)
        print("thanks for taking part")
    return mfx

@greet
def hllo():
    print("hllo worl")
hllo()

print("\n")

@greet
def add(x,y):
    print(x+y)
# greet(add)(5,4)
add(4,6)

print("----------------------------------")

def wish(fx):
    print("goo morning")
    fx()
    print("thanks for your")
    return fx

@wish
def hllo():
    print("hllo worl")