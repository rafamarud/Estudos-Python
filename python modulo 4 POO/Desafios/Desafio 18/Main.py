from Churrasco import Churrasco



## Consumo médio = 400g p pessoa; KG da carne = R$82,40

while True:
    opcao = input("Deseja analisar um churrasco?[S ou N]: ").upper()

    if opcao == "S":
        c = Churrasco()

        c.pessoas = int(input("Quantas pessoas vão participar do churrasco?: "))

        c.analisar()

    elif opcao == "N":
        break

    else:
        print("Opcao inválida, responda apenas com S ou N!!!")

        