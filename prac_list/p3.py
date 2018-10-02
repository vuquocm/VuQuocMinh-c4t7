district = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
population = [150300,247100,333300,266800,420900,318000]
# a = max(population)
# b = min(population)
# for x in range(6):
#     if population[x] == a :
#         print('district', district[x], 'has the largest pop of', a)
# for y in range(6):
#     if population[y] == b :
#         print('district', district[y], 'has the smallest pop of', b)       
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.04]

mddc = []
for i in range(6):
    mddc.append(population[i]/ area[i])
    
    
print(mddc)

mddctb = sum(mddc) / len(district)
print(mddctb)








# area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.04]