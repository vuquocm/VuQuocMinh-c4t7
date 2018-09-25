username = input("enter yo username ")
password = input("enter your password ")
if len(password) >= 8:
    print("strong")
else:
    print("weak")
    password = input("enter your password ")
email = input("enter yo email address ")
if "@" and "." not in email:
    print("re enter")
    email = input("enter yo email address ")
repass = input("reenter yo password ")
if password == repass:
    print("good to go")
else:
    print("wrong")
    repass = input("reenter yo password ")



