"""
1) Faça um programa em que o usuário digita dois valores e o resultado da
soma é exibido na tela.
"""

print("Soma de dois números:")
print("=" * 30)
try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    soma = n1 + n2
    print(f"{n1} + {n2} = {soma}")

except:
    print("Digite apenas números!")

