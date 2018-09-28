items = ['com', 'pho', 'chao', 'bun']
x = len(items)
# for i in range(x):
#     print(items[i])
# for item in items:
#     print(item)

for i, item in enumerate(items):
    print(i + 1,'.' , item)