class Library:
    def __init__(self,books,name):
        self.books=books
        self.name=name
        self.dict={}

    def display_book(self):
        print(self.name)
        print("The available books are:")
        for i in self.books:
            print(i,end=", ")

        print()

    def lend_book(self):
        person=input("Please enter your name")
        want=input("Enter the book you want to lend")
        if want in self.books:
            print("Ok, you can take it!")
            self.dict[want]=person
            self.books.remove(want)
            print(self.books)
        elif want in self.dict:
            taker=self.dict[want]
            print(f"Sorry! it is already taken by {taker}")
        else:
            print("Sorry! we don't have such a book")

    def add_book(self):
        new=input("Hey Admin! Enter the book which you want to add")
        print("Adding....")
        self.books.append(new)
        print("Successfully added!")

    def return_book(self):
        ret=input("Enter the book name")
        if ret in self.dict:
            self.dict.pop(ret)
            self.books.append(ret)
            print("Successfully returned")
            print(self.books)
        else:
            print("You have not lent it!")


l1=Library(["Java Core","Python for beginners","NodeJS","Introduction to Web Dev","Panchtantra","Chandra Kiran"],
           "GT Library")
while True:
    inp=input("enter 1 to display books \n enter 2 to lend a book \n enter 3 to add a new book\n enter"
          "4 to return a book\n enter 5 to exit")
    if inp=="1":
        l1.display_book()
    elif inp=="2":
        l1.lend_book()
    elif inp=="3":
        l1.add_book()
    elif inp=="4":
        l1.return_book()
    elif inp=="5":
        break
    else:
        print("Invalid input")
