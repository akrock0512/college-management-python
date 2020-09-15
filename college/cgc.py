import random
import shelve


def intro():
    print("\t\t\t\t****************************")
    print("\t\t\t\tCHANDIGRAH GROUP OF COLLEGES")
    print("\t\t\t\t****************************")

    print("\t\t\t\tBrought To You By:")
    print("\t\t\t\tAMIT KUMAR[1802292].")


def login(n):
    roll_no = int(input("Enter your roll no.:"))
    pin = int(input("Enter your pin:"))
    with shelve.open("cgc") as file:
        if str(roll_no) in file:
            if pin in file[str(roll_no)]:
                print()
                print("Welcome {}".format(file[str(roll_no)][0]))
                loginn(roll_no)
            else:
                print("Wrong Password")
                print("1: Try again.")
                print("2: Change password")
                j = int(input())
                if j == 1:
                    login(j)
                elif j == 2:
                    change_password(roll_no)
        else:
            print("User id does not exist")


def change_password(roll_no):
    t = int(input("Enter new PIN: "))
    with shelve.open("cgc", writeback=True) as file:
        file[str(roll_no)][6] = t
        print("Pin changed successfully.")
    start()


def loginn(roll_no):
    print("1: Open profile.")
    print("2: Fee payment")
    print("3: Edit profile")
    print("4: Delete account.")
    print("5: Exit")
    i = int(input())
    if i == 1:
        open_profile(roll_no)
    elif i == 2:
        fee_payment(roll_no)
    elif i == 3:
        edit_profile(roll_no)
    elif i == 4:
        delete(roll_no)
    elif i == 5:
        exit()
    else:
        print("Invalid input")
        loginn(roll_no)


def open_profile(roll_no):
    with shelve.open("cgc") as file:
        print("Name = {}".format(file[str(roll_no)][0]))
        print("Course = {}".format(file[str(roll_no)][1]))
        print("Stream = {}".format(file[str(roll_no)][2]))
        print("Father Name = {}".format(file[str(roll_no)][3]))
        print("Mother Name = {}".format(file[str(roll_no)][4]))
        print("Mobiel no. = {}".format(file[str(roll_no)][5]))
    print()
    print("1: Back")
    print("2: Home page")
    print("3: exit")
    s = int(input())
    if s == 1:
        loginn(roll_no)
    elif s == 2:
        start()
    elif s == 3:
        exit()
    else:
        print("Invalid input")
        loginn(roll_no)


def fee_payment(roll_no):
    print("1: Deposit fee.")
    print("2: Fee status.")
    k = int(input())
    f = 0
    with shelve.open("cgc", writeback=True) as file:
        if k == 1:
            z = int(input("Enter amount to deposit: "))
            file[str(roll_no)].append(z)
            print("Successfully deposited.")
        if k == 2:
            for i in range(7, len(file[str(roll_no)])):
                f += file[str(roll_no)][i]
            print("Total fee Submitted = {}".format(f))
    print()
    print("1: Back")
    print("2: Home page")
    print("3: exit")
    s = int(input())
    if s == 1:
        loginn(roll_no)
    elif s == 2:
        start()
    elif s == 3:
        exit()
    else:
        print("Invalid input")
        loginn(roll_no)


def edit_profile(roll_no):
    print("1: Modify Name.")
    print("2: Modify course.")
    print("3: Modify Stream")
    print("4: Father Name")
    print("5: Mother Name")
    print("6: Mobile No.")
    d = int(input())
    with shelve.open("cgc", writeback=True) as file:
        if d == 1:
            h = input("Please enter name:").upper()
            file[str(roll_no)][0] = h
        elif d == 2:
            h = input("Please enter course:").upper()
            file[str(roll_no)][1] = h
        elif d == 3:
            h = input("Please enter stream:").upper()
            file[str(roll_no)][2] = h
        elif d == 4:
            h = input("Please enter Father name:").upper()
            file[str(roll_no)][3] = h
        elif d == 5:
            h = input("Please enter Mother name:").upper()
            file[str(roll_no)][4] = h
        elif d == 6:
            h = input("Please enter Mobile No.")
            file[str(roll_no)][5] = h
    print()
    print("1: Back")
    print("2: Home page")
    print("3: Exit")
    s = int(input())
    if s == 1:
        loginn(roll_no)
    elif s == 2:
        start()
    elif s == 3:
        exit()
    else:
        print("Invalid input")
        loginn(roll_no)


def delete(roll_no):
    with shelve.open("cgc") as file:
        del file[str(roll_no)]
        print("Account deleted successfully.")
    print()
    print("1: Back")
    print("2: Home page")
    print("3: Exit")
    s = int(input())
    if s == 1:
        loginn(roll_no)
    elif s == 2:
        start()
    elif s == 3:
        exit()
    else:
        print("Invalid input")
        loginn(roll_no)


def create():
    rollno = random.randint(1111111, 9999999)
    name = input("Enter your name: ").upper()
    course = input("Enter your course: ").upper()
    stream = input("Enter your stream: ").upper()
    father = input("Enter your Father name: ").upper()
    mother = input("Enter your Mother name: ").upper()
    mobile = int(input("Enter your Mobile no: "))
    pin = int(input("Enter PIN(4 digit): "))
    money = int(input("Enter registration fee: "))
    list1 = [name, course, stream, father, mother, mobile, pin, money]
    with shelve.open("cgc") as file:
        file[str(rollno)] = list1
    list1.clear()
    print("You have successfully created your account:")
    print("Your roll no. is : {}".format(rollno))
    print("Keep your pin safe it will further help you in login.")
    start()


def start():
    f = 0
    print("1: Create new account.")
    print("2: Login.")
    print("3: All accounts")
    print("4: Exit.")
    n = int(input())
    if n == 1:
        create()
    elif n == 2:
        login(n)
    elif n == 4:
        exit()
    elif n == 3:
        with shelve.open("cgc") as file:
            print("Roll no.\t\tName\t\tCourse\t\tBranch\t\tFee status")
            print()
            for i in file:
                for j in range(7, len(file[str(i)])):
                    f += file[str(i)][j]
                print(i, "\t", file[i][0], "\t", file[i][1], "\t\t", file[i][2], "\t\t", f)
                f = 0
    else:
        print("Invalid entry.")
        start()


intro()
start()