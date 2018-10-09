# print('how many engines does an a 340 have?')
# answer = {
#     'A' : 2,
#     'B' : 4,
#     'C' : 3,
#     'D' : 1
# }
# for k, v in answer.items():
#     print(k,v, sep=":")
# rep = str.upper(input('enter your anwser'))
# while True:
#     if rep == 'B':
#         print('correct')
#         break
#     else:
#         print('incorrect')

a = 0
print('how many engines does an a 340 have?')
answer1 = {
    'A' : 2,
    'B' : 4,
    'C' : 3,
    'D' : 1
}
for f, g in answer1.items():
    print(f,g, sep=":")
rep1 = str.upper(input('enter your anwser'))
if rep1 == 'B':
    print('correct')
    a += 1

print('how many engines does an a 777 have?')
answer2 = {
    'A' : 2,
    'B' : 4,
    'C' : 3,
    'D' : 1
}
for h,j in answer2.items():
    print(h,j, sep=":")
rep2 = str.upper(input('enter your anwser'))
if rep2 == 'B':
    print('correct')
    a += 1

print('how many engines does an a Flacon 700X have?')
answer3 = {
    'A' : 2,
    'B' : 4,
    'C' : 3,
    'D' : 1
}
for k, v in answer3.items():
    print(k,v, sep=":")
rep3 = str.upper(input('enter your anwser'))
if rep3 == 'B':
    print('correct')
    a += 1

print('correct ', a)
percent = a/3*100
print('percentage:', percent)


