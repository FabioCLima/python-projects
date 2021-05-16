
def power_of_two(value):
    
    # user_input = input('Please enter a number: ')
    try:
        n = float(value)
        n_square = n ** 2
        return n_square
        
    except ValueError:
        print('Your input was invalid. Using default value 0')
        n = 0
        return n 
     
# %%
test_values = [-2, 0, 4, 'Fabio']
# %%
for user in test_values: 
    power_of_two(value=user)
# %%
