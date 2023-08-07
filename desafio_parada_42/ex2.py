"""

2) Faça um programa em que o usuário precisa cadastrar nome, idade,
telefone e e-mail. Depois mostre os valores digitados na tela.

"""
from time import sleep

while True:
      nome = str(input("Digite seu nome: "))
      idade = str(input("Idade: "))
      telefone = str(input("Telefone: "))
      email = str(input("E-mail: "))

      print("Veja seus dados:")
      sleep(1)
      print(f" Nome: {nome} \n Idade: {idade} anos \n Telefone: {telefone} \n E-mail: {email}")

      resp = str(input("Seus dados estão corretos [S/N]? ")).upper()

      if resp == "S":
            print("Cadastro realizado com sucesso!")
            break

      if resp not in "SN":
            print("Digite apenas S para sim ou N para Não.")

    