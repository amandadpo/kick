"""
4) Faça um programa que converte centímetros em metros.

"""

print("*"*10,"Conversor de medidas","*"*10)
try:
    cm = float(input("Digite a medida em cm: "))
    conversor_em_metros = cm / 100
    print(f"{cm} cm equivalem a {conversor_em_metros} m")
except:
    print("Digite apenas números!")



