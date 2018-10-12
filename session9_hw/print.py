# for i in range(20):
#     print('*', end='')
# a = int(input('enter number of *'))
# for i in range(a):
#     print('*', end='')
# a = int(input('enter:'))
# for i in range(a):
#     if i%2 == 0:
#         print('x', end='')
#     elif i%2 != 0:
#         print('*', end='')
a = int(input('enter:'))
for i in range(a):
    if i%2 == 0:
        print('x', end=' ')
    
    elif i%2 != 0:
        print('*',end=' ')
print()
# for i in range(3):
#     for j in range(7):
#         print('*', end=' ')
#     print()
x = int(input('collumn'))
y = int(input('row'))
for i in range(x):
    for j in range(y):
        print('*', end=' ')
    print()





