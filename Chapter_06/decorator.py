class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = '{0}.{1}@gmail.com'.format(first, last)


per1 = Person('Ross', 'Geller')

per1.first = "Rachel"
print(per1.first)

print(per1.email)
