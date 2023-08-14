cadastro_completo = []

def cadastrar_alunos():
    aluno = {}
    notas = []

    aluno['Nome'] = input("Nome do aluno: ")

    while True:
        try:
          nota = float(input(f"Nota do aluno {aluno['Nome']}: "))
          notas.append(nota)
        except ValueError:
            print("Escolha inválida. Tente novamente.")
            continue

        try: 
          resp = input("Deseja continuar [S]im / [N]ão: ").upper()
        except ValueError:
            print("Escolha inválida. Tente novamente.")
            continue

        if resp == "N":
            break
    
    aluno["Todas as notas"] = notas
    media = sum(notas) / len(notas)
    aluno["Média"] = "{:.2f}".format(media)

    cadastro_completo.append(aluno)

def listar_alunos():
    for aluno in cadastro_completo:
        print(f"Nome: {aluno['Nome']}")
        print(f"Todas as notas: {aluno['Todas as notas']}")
        print(f"Média: {aluno['Média']}")
        print()

def main():
    while True:
        print("\nSistema Escolar")
        print("1. Cadastrar alunos")
        print("2. Listar alunos")
        print("3. Sair")

        try:
            escolha = int(input("Escolha uma opção: "))
            print()
        except ValueError:
            print("Escolha inválida. Tente novamente.")
            continue
        
        if escolha == 1:
            cadastrar_alunos()
        elif escolha == 2:
            listar_alunos()
        elif escolha == 3:
            print("Até logo!")
            break
        else:
            print("Escolha inválida. Tente novamente.")

main()