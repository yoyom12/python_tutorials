'''def op(x,y):
    if(x>y):
        print(x,"is gratr than", y)
        print(x/y)
    else:
        print(x,"is lss than", y)
        print(x*y)
  
a=int(input("fi"))
b=int(input("fi"))
op(a,b)
'''
print("---------------")


def avg(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i

        return "th avg is ",sum/len(num)
    
w = avg(5,4,9,4,5,8)
print(w)



'''
def nam(fnam,mnam,lnam):
    print("hello",fnam ,  mnam , lnam )

# nam(fnam = "parth ", mnam = "gajanan", lnam = "patil")
fnam = input("first nam")
mnam = input("middle nam")
lnam = input("last nam")

nam(fnam,mnam,lnam)

'''