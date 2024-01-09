with open("my1.txt",'r') as f:
    print(type(f))
# move to the 10th byte of the file
    f.seek(10)

# read the next 5 bytes
    print(f.tell())
    l = f.read((5))
    print(l)

with open("sam.txt",'w') as f:
    f.write("my parth")
# only 5 charactors can be save in file by truncate method
    f.truncate(5)

with open("sam.txt",'r') as f:
    print(f.read())