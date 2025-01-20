def add(*args):
    total = 0
    for n in args:
        total += n

    print(total)

add(5,4,11,15)

#kwargs

def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2,add=3, multiply=5)