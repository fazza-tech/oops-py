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

#we can make our code more readable by using a lambda function:

peoples = [
    {'name' : "Lijith", 'house': 'Assaripadi' },
    {'name' : 'Nidhin', 'house': 'Pazhoor'},
    {'name':'Anusree' ,'house':'makutty'},
    {'name':'Fazza' ,'house':'Chalakudy'}
]


peoples.sort(key=lambda person:person['name'])
print(peoples)