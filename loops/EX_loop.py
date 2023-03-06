data = {'color': 'red',
        'fruit': 'apple',
        'Pet': 'dog',
        'car': 'van'}
while data:
        x = next(x for x in data)
        print(x, '=>', data.pop(x))