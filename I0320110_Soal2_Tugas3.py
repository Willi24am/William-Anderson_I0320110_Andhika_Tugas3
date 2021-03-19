dict = {
    'nama': 'William Anderson',
    'hobi': ['Badminton', 'Main Game', 'Basket'],
    'sosmed' : {
        'Instagram': 'willi24am',
        'Twitter': 'willi24am',
        'line': 'william071902'
        },
    'lagu' : ['Stressed out', 'Ride', 'Trapdoor'],
    'makanan' : ['Nasi padang', 'Nasi goreng', 'Telur']
    }
print(dict)

dict['hobi'][2] = 'Tidur'
dict['sosmed']['Instagram'] = 'william08'

print(dict)

del dict['makanan'][1]
del dict['makanan'][0]

print(dict)

dict['hobi2'] = 'tidur'

print(dict)