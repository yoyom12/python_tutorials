# library class 
# 1. no of books
# 2. books  = list add th book
# no of books == len of books

for j in range(0,3):
    class library:
        def books(self):
            listofbook = []
            nobook = int(input("how many books name that you want to add:- "))
            for i in range(0,nobook):
                nameofbook = input("Enter the name of the book you want:- ")
                listofbook.append(nameofbook)
            if(nobook == len(listofbook)):
                print("The book library is working good")
            print(f"The book name is '{','.join(listofbook)}'")



    a = library()
    a.books()