from Pessoa import Pessoa

p1 = Pessoa("Rafael", 20)
p1.aniversario()


p2 = Pessoa("Mauro", 50)
p2.aniversario()


p3 = Pessoa()


print(p1.__doc__) # Dunder Attribute

print(p1)
print(p2)
print(p3)

print(p1.__dict__) # Attribute

print(p1.__getstate__()) #Method

print(p1.__class__) # Attribute