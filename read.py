f = open("my1.txt","r")
i= 0
while True:
    i =i+1
    line = f.readline()
    if not line:
        break
    s1  = line.split(",")[0]
    s2  = line.split(",")[1]
    s3  = line.split(",")[2]
    print(f"marks is stufnts {i} in sin is {s1} ")
    print(f"marks is stufnts {i} in maths is {s2} ")
    print(f"marks is stufnts {i} in phy is {s3} ")