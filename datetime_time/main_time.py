#%%
import time 

def measure_runtime(func):      
    start = time.time()#! current time
    func()
    end = time.time()  #! end time
    print(end - start)
    
    
def powers(limit):  
    """[retorna uma lista com o square do argumento limit]

    Args:
        limit ([int]): [base numérica da série de potências]

    Returns:
        [list]: [série de potências quadradas da base de entrada]
    """    
    return [x**2 for x in range(limit)]
#! usar lambda function pq temos que passar o argumento da inner
#! function
measure_runtime(lambda: powers(limit = 500000))
# %%
import timeit

print(timeit.timeit("[x**2 for x in range(30)]"))
# %%
