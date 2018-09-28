films = ['titanic', 'nun', 'avenger', 'LOL']
# replace = input("new film")
# films[0] = replace
# print(films)

# # i = 2
# # films[2] = input("replace")
# # print(films)

# i = int(input())
# films[i] = input("replace")
# print(films)

# films.pop(2)
# print(films)

# x = int(input())
# films.pop(x)
# print(films)

# y = input()
# films.remove(y)
# print(films)

a = 'LOL'
if a not in films:
    print("recheck")
elif a in films:
    films.remove(a)
    print(films)

# new_items1 = input('enter new items :')
# new_items2 = input('enter new items :')
# new_items3 = input('enter new items :')
# films.append(new_items1)
# films.append(new_items2)
# films.append(new_items3)
# for item in films:
#     print(item)

# new_items1 = input('enter new items :')
# new_items2 = input('enter new items :')
# new_items3 = input('enter new items :')
# films.append(new_items1)
# films.append(new_items2)
# films.append(new_items3)
# for item in films:
#     print(str.upper(item))

# new_items1 = input('enter new items :')
# new_items2 = input('enter new items :')
# new_items3 = input('enter new items :')
# films.append(new_items1)
# films.append(new_items2)
# films.append(new_items3)
# for i, item in enumerate(films):
#     print(i,'.', str.upper(item))

new_items1 = input('enter new items :')
new_items2 = input('enter new items :')
new_items3 = input('enter new items :')
films.append(new_items1)
films.append(new_items2)
films.append(new_items3)
for i, item in enumerate(films):
    if ('e' or 'E' in item):        
        print(i,'.', str.upper(item))
    else:
        print(" ")



