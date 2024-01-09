def fun():
    try:
        l  = [5,3,4,2,5]
        i = int(input("No."))
        print(l[i])
    except:
        print("som error happn")
    finally:
        print("i am always run")

fun()