from candidatos import candidato
from candidatos import leiaOpcao
import time
import os

lista = []

#encontrar o arquivo.csv (tabela candidatos)
pasta = os.path.dirname(__file__)
nome_base = os.path.join(pasta, "dados.csv")

try:

    #abrindo o arquivo em modo leitura
    with open(nome_base, "r", encoding="utf-8") as leitor:
        leitor.readline()

        for linha in leitor:
                dados_linha = linha.strip().split(",")
                obj_candidato = candidato(int(dados_linha[0]) , (dados_linha[1]), int(dados_linha[2]), int(dados_linha[3]), dados_linha[4] == "Sim", dados_linha[5] == "Sim")
                #linha[0] = id; linha[1] = nome; linha=[2] = idade; linha[3] = exp; linha[4] = tec; linha[5] = ing
            
                if obj_candidato not in lista:
                    lista.append(obj_candidato)


    print(f"Quantidade de candidatos: {len(lista)} \n")

    while True:

        print("\n==== MENU INTERATIVO ====\n")

        print("1. TRIAGEM PARA QUALIFICAÇÃO TÉCNICA")
        print("2. EXPAÇÃO DE TALENTOS INTERNACIONAIS")
        print("3. FILTRO DE POTENCIAL JOVEM")
        print("4. CLASSIFICAÇÃO SALARIAL")
        print("5. ENCERRAR PROGRAMA")

        print()

        opcao = leiaOpcao()

        


        if opcao == 1:
            print()
            print("==== TRIAGEM DE QUALIFICAÇÃO TÉCNICA ====")
            for item in lista:
                if item.idade >= 18 and item.tec:
                    print(item)
            time.sleep(2)

        elif opcao == 2:
            print()
            print("==== EXPANSÃO DE TALENTOS INTERNACIONAIS ====")
            for item in lista:
                if item.exp >= 3 or item.ing:
                    print(item)
            time.sleep(2)

        elif opcao == 3:
            print()
            print("==== FILTRO DE POTENCIAL JOVEM ====")
            for item in lista:
                if item.idade < 25 and (item.exp >= 1 or item.tec):
                    print(item)
            time.sleep(2)

        elif opcao == 4:
            print()
            print("==== CLASSIFICAÇÃO SALARIAL (SÊNIOR: EXP > 5 | JÚNIOR: EXP <= 5) ====")
            for item in lista:
                if item.exp > 5:
                    print(f"Nome: {item.nome} | Categoria: SÊNIOR")
                else:
                    print(f"Nome: {item.nome} | Categoria: JÚNIOR")
            time.sleep(2)
        
        elif opcao == 5:
            print("Encerrando programa...")
            break

except Exception as e:
    print("Ocoreu algum erro...",e)