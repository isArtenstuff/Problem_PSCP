# rating = int(input())
# #จงใส่เขียนต่าง ๆ ให้กับ if-elif-else ด้านล่าง
# if 0 <= rating <= 4:
#     print("Bad")
# elif 4 < rating <= 7:
#     print("Okay")
# elif 7 < rating <= 10:
#     print("Good")
# else:
#     print("Wrong rating")


# fruit = input()
# if fruit == "apple":
#     print("apple apple apple")
# elif fruit == "grape":
#     print("GRAPES")
# elif fruit == "mango":
#     print("mangozzz")
# else:
#     print("the following fruit is not valid")

username_input = input()
password_input = input()
username = "admin"
password = "1234"
#จงใส่เงื่อนไข่ต่าง ๆ เพื่อแสดงผลการ login ตรงนี้
if username == "admin" and password is not "1234":
    print("wrong password")
elif username is not "admin" and password == "1234":
    print("wrong username")
elif username is not "admin" and password is not "1234":
    print("wrong username and password")
elif username == "admin" and password == "1234":
    print("login succeeded")
