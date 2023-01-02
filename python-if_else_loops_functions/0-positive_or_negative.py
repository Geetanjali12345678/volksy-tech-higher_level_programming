#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number,'it is positive')
elif number == 0:
    print(number,'its zero')
else:
    print(number,'its negative')
