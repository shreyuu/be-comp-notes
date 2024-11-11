import random

username = input("Enter Username: ")
pwd = input("Enter Password: ")

if username == 'test' and pwd == '1234':
    num = random.randint(1000, 9999)
    print("Enter this 4 digit number:", num)
    user_num = int(input())
    
    if num == user_num:
        print("Login Successfully")
    else:
        print("Login Failed")
else:
    print("Login Failed")
