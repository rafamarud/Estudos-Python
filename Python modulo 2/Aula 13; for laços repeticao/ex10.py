maiorpeso = -999
menorpeso = 1000

for i in range(0,5):
    peso = int(input('Digite um peso: '))
    if(peso > maiorpeso):
        maiorpeso = peso
        
    if (peso < menorpeso):
       menorpeso = peso


print('Menor peso: ', menorpeso)
print('Maior peso: ', maiorpeso)