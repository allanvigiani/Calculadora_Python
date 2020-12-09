print("Bem-vindo à Calculadora Python")
print('*********************************')

operacao = 1

while operacao != 0:
    operacao = int(input("Selecione a opção desejada: "
                         "\n 1 - Soma"
                         "\n 2 - Subtração"
                         "\n 3 - Multiplicação"
                         "\n 4 - Divisão"
                         "\n 0 - Sair"
                         "\n Digite o número correspondente: "))
    if operacao != 0:

        # Função de Soma
        if operacao == 1:
            valor1 = int(input('Digite o primeiro valor: '))
            valor2 = int(input('Digite o segundo valor: '))


            def somar(valor1, valor2):
                return print(f'A soma de {valor1} + {valor2} é {valor1 + valor2}')


            somar(valor1, valor2)

        # Função de Subtração
        elif operacao == 2:
            valor1 = int(input('Digite o primeiro valor: '))
            valor2 = int(input('Digite o segundo valor: '))


            def subtrair(valor1, valor2):
                return print(f'A subtração de {valor1} - {valor2} é {valor1 - valor2}')


            subtrair(valor1, valor2)

        # Função de Multiplicação
        elif operacao == 3:
            valor1 = int(input('Digite o primeiro valor: '))
            valor2 = int(input('Digite o segundo valor: '))


            def multiplicar(valor1, valor2):
                return print(f'A multiplicação de {valor1} X {valor2} é {valor1 * valor2}')


            multiplicar(valor1, valor2)

        # Função de Divisão
        elif operacao == 4:
            valor1 = int(input('Digite o primeiro valor: '))
            valor2 = int(input('Digite o segundo valor: '))


            def dividir(valor1, valor2):
                return print(f'A divisão de {valor1} / {valor2} é {valor1 / valor2}')


            dividir(valor1, valor2)

        else:
            print('Digite um número válido!')
            continue
    else:
        break

print("Obrigado por utilizar a Calculadora Python")
