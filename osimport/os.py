import os


if(not os.path.exists("java")):
    os.mkdir("java")

for i in range(0,100):
    os.mkdir(f"java/day {i+1}")