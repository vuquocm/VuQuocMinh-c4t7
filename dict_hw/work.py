# favorite = {
#     "film" : "pacific rim",
#     "genre" : "action",
#     "release" : 2016,
# }
# print(favorite)
# favorite["about"] = "robot"
# print(favorite)
# a =input("enter your favorite sth")
# b =input("enter a fact")
# c =input("enter another fact")
# favorite = {
#     "name" : input("enter name"),
#     a : input(),
#     b : input(),
#     c : input(),
# }
# print(favorite)
# favorite[input("enter another fact")] = input()
# print(favorite)

# favorite[a] = input("more detail")
# print(favorite)
# del favorite[c]
# del favorite[input("enter a key")]

# person = {
#     'name' : 'qminh',
#     'age' : 16,


# }
# loop = True
# while loop:
#     print(person)   
#     if 'name' in person:
#         print("'name' exists in dict")
#         break
#     else:
#         print("'naem' does not exist")
#         break
# while loop:
#     if 'nationality' in person:
#         print("exist")
#         break
#     else:
#         print('nowhere')
#         break

dictionary = {
    "thurst" : "the main force that makes planes lift of the ground",
    "thurst-reverser" : '''a device that is placed inside an engine which
    is deployed when a plane lands to help it slows down''',
    "cat" : "not a dog"
}
print(dictionary)
while True:
    find = str.lower(input("a plane related word :"))
    print(dictionary[find])
