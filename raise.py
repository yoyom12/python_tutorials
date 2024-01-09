# using raise kyword create custom error

a = int(input("ntr btn 5 to 9:- "))
if (a<5 or a>9):
    raise ValueError("ntr vali input btwn 5-9")