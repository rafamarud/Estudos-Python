from ContaBancaria import ContaBancaria

def main():
    c1 = ContaBancaria(111, "Rafael", 3000)
    c1.depositar(-500)
    c1.sacar(-100)
    c1.titular = "Pedro"
    print(c1)
     
if __name__ == "__main__":
    main()