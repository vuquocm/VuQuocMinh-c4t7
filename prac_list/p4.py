Highscores = [96, 74, 67, 85, 19 ]
# Highscores = sorted(Highscores, reverse = 1)
# print ('Highscores:')
# for i, item in enumerate(Highscores):
#     print (i+1,'.', item)
# new_score = int(input('enter yo new highscore: '))
# Highscores.append(new_score)
# Highscores = sorted(Highscores, reverse = 1)
# print ('Highscores:')
# for i, item in enumerate(Highscores):
#     print (i+1,'.', item)

Highscores = sorted(Highscores, reverse = 1)
print ('Highscores:')
a = 0
b = -1
for i in range(5):
    a = a + 1
    b = b+1 
    print (a,'.', Highscores[b])

new_score = int(input('enter yo new highscore: '))
Highscores.append(new_score)
Highscores = sorted(Highscores, reverse = 1)
print ('Highscores:')
a = 0
b = -1
for i in range(5):
    a = a + 1
    b = b+1 
    print (a,'.', Highscores[b])





