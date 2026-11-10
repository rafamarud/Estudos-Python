from Guerreiro import Guerreiro
from Mago import Mago
from Personagem import Personagem

def main():
    p1 = Guerreiro("Megaman", 1000)
    p2 = Mago("Gandalf", 2000)

    p1.atacar(p2, 100)

    p2.curar()

    p2.atacar(p1, 100)

    p1.curar()
    

if __name__ == "__main__":
    main()