
import math

def divide_or_square(rand_num):
    if rand_num % 5 == 0:
        return math.sqrt(rand_num)
    else:
        return rand_num % 5

print(divide_or_square(10))
