
register = {'Michael' : 'yes', 'John' : 'no' , 'Peter' : 'Yes', 'Mary': 'Yes'}
register_true = 'yes'

def register_check(register, register_true):
    count = 0
    for x in register.values():
        if x.lower() == register_true:
            count += 1

    return print(count)

register_check(register, register_true)
