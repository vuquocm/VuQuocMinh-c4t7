
from random import shuffle

listwords = ['sulfur', 'nitrate', 'clorine', 'florine', 'iodine', 'copper', 'aldehyde']
while True:
    i = len(listwords)
    shuffle(listwords)
    random = list(listwords[3])
    x = len(listwords[3])
    shuffle(random)
    for i in range(x):
        print(random[i])
    word_guess = input("your guess : ")
    if word_guess == listwords[3]:
        print("true")
        break
    else:
        print("false")
        
            
