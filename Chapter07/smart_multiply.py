def smart_multiply(func):
    def inner(a,b):
        if (a.isdigit() and b.isdigit()):
            a = int(a)
            b = int(b)
            print("multiplying ",a," with ",b)
            return func(a,b)
        else:
            print("Whoops!! Not valid multiplication")
            return
    return inner

@smart_multiply
def multiply(a,b):
    print(a*b)
a = input("value of a: ")
b = input("value of b: ")
multiply(a,b)
