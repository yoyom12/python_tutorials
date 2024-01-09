import os

files = os.listdir("C:/Users/parth/Desktop/python/minipro/kluttr/")
i = 1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"C:/Users/parth/Desktop/python/minipro/kluttr/{file}",f"C:/Users/parth/Desktop/python/minipro/kluttr/{i}.jpg")
        i = i+1