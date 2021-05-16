pets = ['cachorro', 'gato', 'passarinho', 'peixe']
upper_pets = []
for pet in pets: 
    upper_pet = pet.upper()
    upper_pets.append(upper_pet)

upper_pets = [pet.upper() for pet in pets]

'''
#! list comprehension with a conditional statement
[expression for item in iterable if some_condition]

#! expanded form
for item in iterable:
    if some_condition:
        expression
'''    
numbers = list(range(20))
pares = []
impares = []

pares = [number ** 2 for number in numbers if number % 2 == 0]
impares = [number ** 3 for number in numbers if number % 2 != 0]

def has_four_legs(pet):
    return pet in ['pig', 'dog', 'turtle', 'hamster', 'cat']

pets = ['bird', 'snake', 'dog', 'turtle', 'cat', 'hamster']
four_legs_pets = [pet.capitalize() for pet in pets if has_four_legs(pet)]

#! Conditional Assigment
# basic syntax
# [expression0 if some_condition else expression1 for item in iterable]
# syntax explained: compared to the list comprehension's basic syntax: [expression for item in iterable], 
# we can thin about that (expression0 if some_condition else expression1) is a whole part that constitutes the expression in the general format

max_value = 10
numbers = [7, 9, 11, 4, 3, 2, 12]

celling_numbers0 = [number if number <= max_value else max_value for number in numbers]
y = [(number if number <= max_value else max_value) for number in numbers]

# map() returns an iterator object
#! map(function, iterable)
capitalized_pets = list(map(str.capitalize, pets))
print(capitalized_pets)
