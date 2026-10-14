"""
Ponto de entrada do programa.

Executa a aplicação instanciando a View, que por sua vez usa o Model
e os Templates (padrão MVT).
"""

from view import AlunoView


def main():
    app = AlunoView()
    app.executar()


if __name__ == "__main__":
    main()
