class Animal:
    def __init__(self,name):
        self.name = name
        self.order = 0

    def set_order(self,order):
        self.order = order

    def get_order(self):
        return self.order

    def is_older_than(self, animal2):
        return this.order < animal2.get_order()

    
class AnimalQueue:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(animal1):
        animal1.set_order(self.order)
        self.order += 1
        
        if (type(animal1)=='Dog'):
            dogs.append(animal1)
        elif (type(animal1)=='Cat'):
            cats.append(animal1)

    def dequeueAny(self):
        if (len(dogs)==0):
            return dequeue_cats()
        elif (len(cats)==0):
            return dequeue_dogs()
        else:
            dog1 = dogs.pop()
            cat1 = cats.pop()
        if (dog.is_older_than(cat)):
            return dequeue_dogs()
        else:
            return dequeue_cats()

    def dequeue_dogs():
        return dogs.pop()

    def dequeue_cats():
        return cats.pop()

class Dog(Animal):
    def __init__(self,n):
        Animal(n)

class Cat(Animal):
    def __init__(self,n):
        Animal(n)

    
        
