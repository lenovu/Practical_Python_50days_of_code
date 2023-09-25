
fruits = ['apple', 'orange', 'bannana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicates(fruits, names):

    if len(fruits) != len(set(fruits)):
        print("Duplicates found!")
    else:
        print("No Duplicates!")

    if len(names) != len(set(names)):
        print("Duplicates found!")
    else:
        print("No Duplicates!")

check_duplicates(fruits,names)
