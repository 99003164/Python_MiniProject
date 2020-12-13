import datetime

class MyLibrary:  # main class
    def Split():
        global book, author, copies, cost  #global variables
        book = []
        author = []
        copies = []
        cost = []
        with open("File.txt", "r") as f:  # open file in read mode

            total_lines = f.readlines()
            total_lines = [x.strip('\n') for x in total_lines]
            for var1 in range(len(total_lines)):
                index = 0
                for a in total_lines[var1].split(','):
                    if (index == 0): book.append(a)
                    elif (index == 1): author.append(a)
                    elif (index == 2):  copies.append(a)
                    elif (index == 3): cost.append(a.strip("Rs."))
                    index += 1

    def Date():  # date method
        now=datetime.datetime.now
        return str(now().date())

    def Time():  # time method
        now=datetime.datetime.now
        return str(now().time())

    def borrowBook(): # borrow method to borrow books
        success = False
        while (True):
            fst = input("Borrower first name: ")  # taking borrower first name as input
            if fst.isalpha():
                break
            print("Input only alphabet from A-Z or a-z")  # if user enter character other than alpabet, it asks user to enter name again
        while (True):
            lst = input("Borrower last name: ")  # taking borrower last name as input
            if lst.isalpha():
                break
            print("Input only alphabet from A-Z or a-z")  # if user enter character other than alpabet, it asks user to enter last name again

        borrow_file = "Borrow-" + fst + ".txt"  # creating output borrow file
        with open(borrow_file, "w+") as f:
            f.write("My Library Management System\n")
            f.write("Borrowed By: " + fst + " " + lst + "\n")
            f.write("Date: " + MyLibrary.Date() + "    Time:" + MyLibrary.Time() + "\n\n")
            f.write("S.N. \t\t Bookname \t      \tAuthorname \n")

        print("Please select a option below:")  # select the book
        for var1 in range(len(book)):
            print("Enter", var1, "to borrow book", book[var1])

        var3 = int(input())

        if (int(copies[var3]) > 0): # checks wheather the entered book is available or not
            print("The Selected book is available")
            with open(borrow_file, "a") as f:
                f.write("1. \t\t" + book[var3] + "\t\t  " + author[var3] + "\n")

        copies[var3] = int(copies[var3]) - 1
        with open("File.txt", "w+") as f:
            for var1 in range(3):
                f.write(book[var1] + "," + author[var1] + "," + str(
                    copies[var1]) + "," + "Rs." + cost[var1] + "\n")

    def returnBook():
        name = input("Name of borrower: ") # aks the user to enter the name
        a = "Borrow-" + name + ".txt"
        try:
            with open(a, "r") as f:  # open the file in read only mode
                total_lines = f.readlines()
                total_lines = [a.strip("Rs.") for a in total_lines]

            with open(a, "r") as f:
                data = f.read()
                print(data)
        except:
            print("Name of the borrower is incorrect") # if user enter incorrect name asked to to enter name again
            MyLibrary.returnBook()

        b = "Return-" + name + ".txt"  # creating the return book output file
        with open(b, "w+")as f:
            f.write("My Library Management System \n")
            f.write("Returned By: " + name + "\n")
            f.write("Date: " + MyLibrary.Date() + "    Time:" + MyLibrary.Time() + "\n\n")
            f.write("S.N.\t\tBookname\t\tPrice\n")

        total = 0.0
        for var1 in range(3):
            if book[var1] in data:
                with open(b, "a") as f:
                    f.write(str(var1 + 1) + "\t\t" + book[var1] + "\t\tRs." + cost[var1] + "\n")
                    copies[var1] = int(copies[var1]) + 1
                total += float(cost[var1])

        print("Rs." + str(total))
        print("Is return date of book is expired?")  # if book is returned after due date, fine is collected
        print("Enter y or Y for Yes and n or N for No")
        stat = input()
        if (stat.upper() == "Y"):
            print("Book returned after how many late days?")
            day = int(input())
            fine = 2 * day  # Rs. fine per day
            with open(b, "a")as f:
                f.write("Fine: Rs." + str(fine) + "\n")
            total = total + fine

        print("Final Total: " + "Rs." + str(total))
        with open(b, "a")as f:
            f.write("Total: Rs." + str(total))

        with open("File.txt", "w+") as f:
            for var1 in range(3):
                f.write(
                    book[var1] + "," + author[var1] + "," + str(copies[var1]) + "," + "Rs." +
                    cost[var1] + "\n")

object1 = MyLibrary  # object of class My Library

def start():  # main method
    while (True):
        print("My Library Management System")
        print("Select 1 to display all books in stok")
        print("Select 2 to borrow book")
        print("Select 3 to return book")
        print("Select 4 to quit")
        try:
            option = int(input("Select your option 1, 2, 3 or 4: "))
            print()
            if (option == 1):
                with open("File.txt", "r") as f:  # open file in read mode
                    total_lines = f.read()
                    print(total_lines)
                    print()
            elif (option == 2):
                MyLibrary.Split()
                MyLibrary.borrowBook()
            elif (option == 3):
                MyLibrary.Split()
                MyLibrary.returnBook()
            elif (option == 4):
                print("Thank you. Visit again")
                break
            else:
                print("Select the valid option")
        except ValueError:
            print("Provide proper input")

start()  # calling start() method
