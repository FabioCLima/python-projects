import sys
import time
lista = list(range(10000))
print(sys.getsizeof(lista))


def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r


l1 = [x for x in range(10000)]
print(sys.getsizeof(l1))
l2 = (x for x in range(10000))
print(sys.getsizeof(l2))
