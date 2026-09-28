import os

details = []

print("-"*30)
print("Signup Here")
print("-"*30)

name = input("Enter Name: ")
password = input("Enter Password: ")
details.append(name)
details.append(password)
os.system("cls")

print("-"*30)
print("Login Now")
print("-"*30)

while(True):
    name=input("Enter name: ")
    password = input("Enter Password: ")
    if(name == details[0] and password ==  details[1]):
        print("Login Success!")
        break
    else:
        print("Wrong username or password please try again")
        print("-"*30)