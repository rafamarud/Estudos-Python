num = [2, 5, 9 ,1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse = True)
num.insert(2, 2)
##num.pop(2)
num.remove(2)
print(num)
print(f'Esse lista tem {len(num)} elementos')

##for c, v in enumerate(num): enumerate pega tanto o 'c' quanto o 'v'

a = [2, 5, 7, 1] 
b = a[:] ## criar uma copia de uma lista

b = a ## ao alterar uma lista a outra tambem recebe alteracao

