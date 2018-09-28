from random import shuffle

word = input("enter a word : ")
character = list(word)
x = len(character)
shuffle(character)
for i in range(x):
    print(character[i])

