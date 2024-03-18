class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.age = age
    self.breed = breed

  def __str__(self):
    return f"{self.breed} dog named {self.name}"

class GuardDog(Dog):
  def __init__(self, name, breed):
    super().__init__(name, breed, 5)

  def rrrr(self):
    print("stay away!")

class Puppy(Dog):
  def __init__(self, name, breed):
    super().__init__(name, breed, 0.1)

  def woof_woof(self):
    print("Woof Woof~")

  
  
  
ruffus = Puppy(name='Ruffus', breed='Beagle')
bibi = GuardDog(name='Bibi', breed='Dalmatian')

print(ruffus, bibi)

ruffus.woof_woof()
bibi.rrrr()