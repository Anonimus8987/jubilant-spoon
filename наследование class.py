class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return 'woof!'
    
class Cat(Animal):
    def make_sound(self):
        return 'Meowmeow'
    
class Caw(Animal):
    def make_sound(self):
        return 'momo'
    
dog = Dog()

cat = Cat()

caw = Caw()


print(dog.make_sound())
print(cat.make_sound())
print(caw.make_sound())