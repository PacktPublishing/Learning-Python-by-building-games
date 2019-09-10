class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{0}.{1}@gmail.com'.format(self.first, self.last)


per1 = Person('Ross', 'Geller')

per1.first = "Racheal"
print(per1.first)

print(per1.email)
