employees_sheet = [
    {
        'name' : 'Huy',
        'role' : 'Waiter',
        'hours' : 12,
        'Salary per hour($)' : 0.8
    },
    {
        'name' : 'Tung',
        'role' : 'Cook',
        'hours' : 24,
        'Salary per hour($)' : 1.5
    },
    {
        'name' : 'M.Duc',
        'role' : 'Manager',
        'hours' : 20,
        'Salary per hour($)' : 2
    }

]

sheet1 = {
    'name' : 'Don',
    'role' : 'Waiter',
    'hours' : 12,
    'Salary per hour($)' : 0.9
}
sheet2 = {
        'name' : 'H.Duc',
        'role' : 'Waiter',
        'hours' : 14,
        'Salary per hour($)' : 0.7
    }
employees_sheet.append(sheet1)
employees_sheet.append(sheet2)
#print(employees_sheet)

# print(employees_sheet[2])

# employees_sheet[0] = {
#     'name' : 'Huyen',
#     'role' : 'Waitress',
#     'hours' : 14,
#     'Salary per hour($)' : 1
# }
# print(employees_sheet)

# del employees_sheet[4]
# print(employees_sheet)

for p in employees_sheet:
    for i in range(len(employees_sheet)):
        
        print(i+1,'.',p['name'])
        print(p['role'])
        print(p['hours'])
        print(p['Salary per hour($)'])

for s in employees_sheet:
    print(s['name'])
    salary = s['hours']*4*s['Salary per hour($)']
    salaryi = int(salary)
    print('salary:',salaryi,'$')
x = 0
total = 0
for i in range(len(employees_sheet)):
    x < len(employees_sheet)
    total += employees_sheet[x]['hours']*4*employees_sheet[x]['Salary per hour($)']
    x = x +1
totalint = int(total)
print('total payment:', totalint, '$')