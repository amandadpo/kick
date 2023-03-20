programa {
funcao inicio() {

  escreva(":::::CALCULADORA:::::\n")

  real soma, subtracao, multiplicacao, divisao
  real n1, n2
  real op = 0

    faca {
    

    escreva("informe a operacao que deseja: \n")
    escreva("Digite: \n")
    escreva("1 para Somar \n")
    escreva("2 para Subtrair \n")
    escreva("3 para Multiplicar \n")
    escreva("4 para Dividir \n")
    escreva("5 para Sair \n")
    
    leia(op)

    limpa()

    escreva("Informe o primeiro valor\n")
    leia(n1)
    escreva("Informe o segundo valor\n")
    leia(n2)
    
    se(op == 1){
      soma = n1+n2
      escreva("a soma é: ",soma)
    }
    senao se(op == 2){
      subtracao = n1-n2
      escreva("a diferença é: ",subtracao)
    }
    senao se(op == 3){
      multiplicacao = n1*n2
      escreva("a multiplicação é: ",multiplicacao)
    }
    senao se(op == 4){
      divisao = n1/n2
      escreva("a divisão é: ",divisao)
    }
    senao{
      escreva(Operacao Invalida)
    }

    escreva("\nDigite 6 para Voltar ao Menu ou 5 para sair \n")
    leia(op)
    limpa()
  }
  
  }enquanto (op != 5) 
  continue
   enquanto (op != 6)
  continue
  
}

