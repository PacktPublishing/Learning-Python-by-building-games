class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
 
per1 = Person('Ross', 'Geller')

per1.first = "Rachel"
print(per1.first)

print(per1.email)
