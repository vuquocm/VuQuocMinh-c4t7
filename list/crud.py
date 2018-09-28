items = ['airbus', 'boeing', 'bombardier']
print(items)
a = input("choose C or R or U or D :")
while True:
    
    if a == 'C':
        new_item = input('wanna add sth? :')
        items.append(new_item)
        print(items)
        a = input("choose C or R or U or D :")
    elif a == 'R':
        x = len(items)
        if x > 0:
            for i, item in enumerate(items):
                print(item)

        elif x == 0:
            print('no item in list')
        a = input("choose C or R or U or D :")    
    elif a == 'U':
        i = int(input("whic item u wanna replace: "))
        replace = input('what do u wnat to change: ')
        items[i] = replace
        print(items)
        a = input("choose C or R or U or D :")
    elif a == 'D': 
        i = int(input('which item u wanna remove? : '))
        items.pop(i)
        print(items)
        a = input("choose C or R or U or D :")