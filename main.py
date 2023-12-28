import pymongo
import random

def sign():
    name = input("enter your name =")
    password = input("enter a password (must be 6 characters) =")
    mobile = input("enter the mobile number =")
    t = collection.find_one({"mobile_number": mobile})
    if (t == None):
        print("wellcome to game\n Lets start the game")
        collection.insert_one({"name": name, "password": password, "mobile_number": mobile})
        print("--------------------------------------------------------")
    else:
        print("Error : user is already exist with this mobile number  please login with your account")
        login()


def login():
    name = input("enter your name=")
    password = input("enter a password=")
    t = collection.find_one({"name ": name, "password": password})
    # t2 = collection.find_one({"name": "python"})
    # print(t)

    if t is not None:
        print("wellcome back.....")
    else:
        print("Error : wrong password OR user name try again.....")
        option()


def option():
    c = input("Signin OR Login :")
    if "signin" in c.lower():
        sign()
    else:
        login()


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["user"]
collection = db["user_detail"]
option()

u = 0
c = 0
items = ["snake", "water", "gun"]
status = [['Draw', 'Win', 'Loss'], ['Loss', 'Draw', 'Win'], ['Win', 'Loss', 'Draw']]

print(" 0-snake\n 1-water\n 2-gun\n 3-exit")

while (True):

    u = int(input("enter your choice:"))
    if (u == 3):
        print("Exiting....")
        break;
    print("computer is selecting......\n")
    c = random.randint(0, 2)
    print(f"computer:{items[c]}")
    print(f"user:{items[u]}\n\n")
    print("final result :")
    if (status[u][c] == 'Win' or status[u][c] == 'Loss'):
        print(f"computer:{status[c][u]}")
        print(f"user:{status[u][c]}\n")
        print("\n")
    else:
        print(f"{status[u][c]}")
        print("\n")


