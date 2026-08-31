from time import sleep

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = "titulo"
        self.paginas = paginas
        self.pagina_atual = 1

        print(f"Voce abriur o livro {self.titulo} que tem {self.paginas} paginas no total. Voce agora esta na pagina {self.pagina_atual}")

        

    def avancar(self, qtd):

        for i in range(qtd):

            if self.pagina_atual >= self.paginas:
                print(f"Voce avancou {qtd} paginas e chegou ao fim do livro e está na ultima pagina: pagina {self.pagina_atual}")
                return

            print(f"Pagina {self.pagina_atual} =>")
            

           
        

            sleep(0.5)
            self.pagina_atual += 1


        print(f"Voce avancou {qtd} paginas e está na pagina {self.pagina_atual}.")
            

            
        



        

l1 = Livro("AAAA", 5)
l1.avancar(2)
sleep(2)
l1.avancar(4)


    
