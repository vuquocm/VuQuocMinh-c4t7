i = int(input("enter a month"))
if i in (1, 3, 5, 7, 8, 10, 12):
    print("there are 31 days")
elif i in (6, 9, 11, 4):
    print("there are 30 days")
elif i == 2:
    print("there are 28 days ") 
