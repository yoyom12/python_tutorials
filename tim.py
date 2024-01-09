import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

t = time.localtime()
print(t)


H = int(time.strftime("%H"))
print(H)
M = int(time.strftime("%M"))
print(M)
S = int(time.strftime("%S"))
print(S)


if(H>0 and H<12):
    print("it's",timestamp,"so good morning")
elif(H>=12 and H<=18):
    print("it's",timestamp,"so good afternoon")
elif(H>=18 and H<=22):
    print("it's",timestamp,"so good evening")
else:
    print("it's",timestamp,"so good night")

