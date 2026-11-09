from classes.Funcionario import Funcionario
from classes.Horista import Horista
from classes.Mensalista import Mensalista


def main():
    
    f1 = Mensalista("Amanda", 9500)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Horista("Paulo", 12, 200)
    f2.calc_sal()
    f2.analisar_sal()




if __name__ == "__main__":  
    main()