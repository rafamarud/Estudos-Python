from Avaliacao import Avaliacao
from rich import print, inspect
def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    av1.nota = -3
    print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")
    

    

if __name__ == "__main__":
    main()  