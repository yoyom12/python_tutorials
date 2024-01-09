import os 
folders = os.listdir("java")

print(os.getcwd())

os.rmdir(f"java/tutorial 2/")

for folder in folders:
    print(folder)
    print(os.listdir(f"java/{folder}"))