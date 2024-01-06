def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


multiplicador = criar_multiplicador(2)

numero_multiplicado = input("Informe o valor para ser dobrado: ")
numero_multiplicado_int = int(numero_multiplicado)

print(multiplicador(numero_multiplicado_int))
