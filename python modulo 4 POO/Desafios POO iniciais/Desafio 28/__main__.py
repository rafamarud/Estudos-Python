from Termostato import Termostato

def main():
    t = Termostato()

    try:
        t.temperatura = 12
        print(t.ftemperatura)
    except Exception as e:
        print(f"Houve um problema: {e}")

if __name__ == "__main__":
    main()