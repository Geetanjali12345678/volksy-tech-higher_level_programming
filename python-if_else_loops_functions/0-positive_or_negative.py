#!/usr/python3
import random
number = random.randint(-10, 10)
if number>0:
    print(number,'it is postive')
elif number == 0:
    print(number,'its zero')
else number<0:
    print(number,'its negative')
