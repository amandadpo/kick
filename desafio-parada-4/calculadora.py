print('-=' * 10)
print("    CALCULADORA ")
print('-=' * 10)

while True:
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        operacao = int(input(' 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \nEscolha a operação:  '))
    except:
        print('Um ou mais números inválidos.')
        continue

    if operacao == 1:
        soma = n1 + n2 
        print(f'{n1} + {n2} = {soma}')
    elif operacao == 2:
        subtrair = n1 - n2
        print(f'{n1} + {n2} = {subtrair}')
    elif operacao == 3:
        if n2 == 0:
            print('Erro! Não existe divisão por 0.')
        else:
            dividir = n1 / n2
            print(f'{n1} / {n2} = {dividir}')
    elif operacao == 4:
        multiplicar = n1 * n2
        print(f'{n1} * {n2} = {multiplicar}')
    elif operacao > 5 or operacao <= 0:
        print('Digite uma opção válida!')
        continue
    
    opcao = str(input('Digite [S] para Sair: ')).upper().strip()

    if opcao == 'S':
        print('VOLTE SEMPRE!')
        break
    
    
       