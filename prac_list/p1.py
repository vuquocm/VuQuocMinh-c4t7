colors = ['red', 'blue', 'black', 'white']
print("our color list")
print(*colors, sep = ',')
# x = input('add a color :')
# colors.append(x)
# print("new list")
# print(*colors, sep = ',')
# y = int(input('position?'))
# print("color at chosen position")
# print(colors[y])
print("choose number or color:")
x = input()
if x == 'color' :
    
    colour = input("what number?")
    colors.remove(colour)
    for i, item in enumerate(colors):
        print(i+1, '.', item)
elif x == 'number' :
    
    a = int(input("what number?"))
    colors.pop(a)
    for i, item in enumerate(colors):
        print(i+1, '.', item)

from turtle import *

for i in range(3):
    forward(50)
    color(colors[i-1])
mainloop()








    



