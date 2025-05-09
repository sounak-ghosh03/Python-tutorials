# # creating classes and objects in python

# class Person:
#   name = "Harry"
#   occupation = "Software Developer"
#   networth = 10
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")


# a = Person()
# b = Person()
# c = Person()

# a.name = "Shubham"
# a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()

class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()

