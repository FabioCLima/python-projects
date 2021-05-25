import random

Total = 0
i = 0
while Total < 100:
    Total += random.randint(-10, 10)
    print(Total)
    i += 1
    if i == 120 or  i == -120:
        break
