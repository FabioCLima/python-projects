import pandas as pd 

df = pd.DataFrame(data={"id": ['a', 'b', 'c'],
                        "value" : [1, 2, 3]})

print(df)

def multiply_value(df, multiplier):  
    df = df.copy() 
    df['value'] = df['value'] * multiplier 
    return df

multiplier_list = [1, 2, "3"]

for mult in multiplier_list: 
    print(mult)  
    multiply_value(df, mult)

