def add(*args):
    #print (args[1])

    summ = 0 
    for n in args:
        sum += n 
    return sum 
#print(add(3,5,6,2,1,7,4,3))


#**kwargs Keyworded variable length Argmeunts 
def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n += kwargs["multiply"]

calculate(2, add=3, multiply=5)


#Hot to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)