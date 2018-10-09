computer_brand = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30,
    'ACER' : 15,
    'TOSHIBA' : 22

}
# print('number of mac:', computer_brand['MACBOOK'])
# a = str.upper(input("enter a brand"))
# print('number of mac:', computer_brand[a])
# computer_brand['TOSHIBA'] = 10

# b = int(input('enter number'))
# c = str.upper(input('enter a brand'))
# computer_brand[c] = b

# computer_brand['DELL'] += 10
# computer_brand['MACBOOK'] = 2
computer_brand['FUJISU'] = 15
computer_brand['ALIENWARE'] = 5
for k,v in computer_brand.items():
    print(k,v, sep=':')
total = 0
number_list = []
for n in computer_brand.values():
    number_list = [n]
    for i in range(len(number_list)):
        total += number_list[i]
        i += 1
print(total)

computer_price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJISU' : 900,
    'ALIENWARE' : 1000
}
# print('price of ASUS', computer_price['ASUS'])
# brand_price = str.upper(input('enter a brand'))
# print('price of ur chosen brand', computer_price[brand_price])
# total_price = computer_price['ASUS']*5
# print(total_price)
brand = str.upper(input('enter a brand'))
number = int(input('enter a number'))
total_price = computer_price[brand]*number
computer_brand[brand] = computer_brand[brand] - number
for k,v in computer_brand.items():
    print(k,v, sep=':')
# for a in computer_brand.keys():
#     gia_tri = computer_brand[a]*computer_price[a]
#     print(a, gia_tri, sep=':')
tong = 0
for a in computer_brand.keys():
    gia_tri = computer_brand[a]*computer_price[a]
    tong = tong + gia_tri
print('total value of computers in storage:', tong)    