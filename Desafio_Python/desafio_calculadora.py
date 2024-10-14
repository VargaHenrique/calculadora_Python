def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("s - Sair")
        operacao = input("Selecione uma opção ou aperte 's' para Sair: ")

        if operacao == "s" or operacao == "S":
            print("OBRIGADO POR UTILIZAR A CALCULADORA SIMPLES.")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
            continue

        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))

        if operacao == "1":
            resultado = num1 + num2
            print("O resultado da operação Soma é: ", resultado)
        elif operacao == "2":
            resultado = num1 - num2
            print("O resultado da operação Subtração é: ", resultado)
        elif operacao == "3":
            resultado = num1 * num2
            print("O resultado da operação Multiplicação é: ", resultado)
        else:
            if num2 == 0:
                print("Divisões com zero não são possíveis. Tente novamente. ")
                continue
            else:
                resultado = num1 / num2
                print("O resultado da operação Divisão é: ", resultado)

calculadora()