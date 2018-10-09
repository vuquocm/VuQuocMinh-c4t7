
character = {
    'Name' : 'Light',
    'Age' : 17,
    'Strength' : 8,
    'Defense' : 10,
    'HP' : 100,
    'Backpack' : ['Shield', 'Bread Loaf'],
    'Gold' : 100,
    'Level' : 2
}
character['Gold'] += 50
character['Backpack'].append('FlintStone')
character['Pocket'] = ['MonsterDex', 'Flashlight']
skill = []
skill1 = {
    'Name' : 'Tackle',
    'Minimum level' : 1,
    'Damage' : 5,
    'Hit rate' : 0.3
}

skill2 = {
    'Name' : 'Quick Attack',
    'Minimum level' : 2,
    'Damage' : 3,
    'Hit rate' : 0.5
}

skill3 = {
    'Name' : 'Strong Kick',
    'Minimum level' : 4,
    'Damage' : 7,
    'Hit rate' : 0.2
}
skill.append(skill1)
skill.append(skill2)
skill.append(skill3)
# for k,v in skill1.items():
#     print(k,v)
# for k,v in skill2.items():
#     print(k,v)
# for k,v in skill3.items():
#     print(k,v)
print('Available Skills')
for i in range(len(skill)):
    print('Skill', i + 1, sep=' ')
    print(skill[i]['Name'])
    i += 1

loop = True
while loop:
    a = input('Choose a skill: ')    
    if a == 'Skill 1':
        if skill[0]['Minimum level'] <= character['Level']:
            print('deal', skill[0]['Damage'], 'damage' )
        else:
            print('not enough experience')
    elif a == 'Skill 2':
        if skill[1]['Minimum level'] <= character['Level']:
            print('deal', skill[1]['Damage'], 'damage' )
        else:
            print('not enough experience')
    elif a == 'Skill 3':
        if skill[2]['Minimum level'] <= character['Level']:
            print('deal', skill[2]['Damage'], 'damage' )
        else:
            print('not enough experience')
    else:
        print('Your character does not have that skill')


