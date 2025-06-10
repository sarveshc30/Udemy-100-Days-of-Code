def add(*args):
    op = 0
    for i in args:
        op += i
    return op

print(add(1, 2, 3, 4, 5))

class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.year = kwargs.get('year')
        self.company = kwargs.get('company')

    def show(self):
        print(self.year, self.company, self.model)

car = Car(year='1998',  model='Civic')
car.show()