"""
WAP to define a function Random() that takes as parameter and display any five number of size.
The n input should be between 1-7 only.
"""

def random(n):
    import random
    for i in range(5):
        print(random.randint(10 ** n, ((10 ** (n + 1)) - 1)))


n = int(input('Enter value of n: '))
if 1 <= n <= 7:
    random(n - 1)
else:
    print('Wrong Input')
