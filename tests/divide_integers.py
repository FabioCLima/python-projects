# divide_integers.py

def divide(numerator, denominator):
    
    if denominator == 0:                           #?test_case2
        return 'Not defined'
    elif denominator is None or numerator is None: #?test_case4
        return 'Numerator/denominator value is None' 
    return int(numerator/denominator)              #?test_case3 and test_case1