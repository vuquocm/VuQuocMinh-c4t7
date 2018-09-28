from random import randint

loop = True
while loop:

    a = randint(0, 20)
    b = randint(0,20)
    c = randint(0, 40)

    print(a, "+", b, "=", c)
    x = str(input())
    if x == "true" and a + b == c:
        
        x = input()
    elif x == "false" and a + b != c:
        
        x = input()
    elif x == "true" and a + b != c:
        print("game over")
        loop = False
    elif x == "false" and a + b == c:
        print("game over")
        loop = False