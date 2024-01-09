
# def factorial(n):

#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# factorial(4)


# print(n)

def fib(n):
    if(n==0 or n==1):
        return n 
    else:
        return(fib(n-1)+fib(n-2))

n = int(input("fgj"))
print(fib(n))