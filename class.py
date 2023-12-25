class Person:
    def init(self, name, age):
        self.name = name 
        self.age = age


client = Person('Jordan', 20)
client1 = Person('Emily', 22)
client2 = Person('Jonatan',24)
print(client.name, client.age)
print(client1.name, client1.age)
print(client2.name, client2.age)