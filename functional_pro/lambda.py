peoples = [
    {'name' : "Hamsa", 'house': 'Assaripadi' },
    {'name' : 'Fazza', 'house': 'Pazhoor'},
    {'name':'Jazeela' ,'house':'makutty'},
    {'name':'Zinan' ,'house':'Chalakudy'}
]

def f(person):
    return person['name']
peoples.sort(key=f)
print(peoples)