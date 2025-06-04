
def main(n,n2,s):

    #1
    def addF(n, n2):
        print(result := (n + n2))
        return result
    #achei que dava pra diminuir codigo criando a variavel dentro do print, mas nao da naturalmente, so com o uso do ':='

    #2
    def subF(n,n2):
        result = n-n2
        print(f'O valor da subtração é: {result}.')
        return result
    
    #3
    def mult(n, n2):
        product = n*n2
        print(f'O valor do produto é: {product}.')
        return 
    
    #4
    def div(n, n2):
        try:
            division = n/n2
        except ZeroDivisionError:
            print("ERROR, o divisor não pode ser igual a 0")
            n2 = float(input("Digite um valor diferente de 0: "))
            division = n/n2
            print(division)
        else:
            division = n/n2 
            print(f'O resultado da divisão é: {division}.')
        return division
        #primeiro fiz com if else, mas pra tentar me desafiar fiz com try except até porque é mais profissional
        #deve dar pra fazer um loop e diminuir codigo

    #5
    """def fatorial(n):
        fat = n*(n-1)
        while fat !=0:
            do fat
                     atualizar valor de n em - duas unidades e fazer de novo enaquanto salvo o resultado antior em outra variavel 
                nao salvar a ultima iteracao q é qnd ele admite a condicao q é para ele parar
                 fatResult *= fat em cada iteracao
                 dificuldade em criar iteracoes de cabeca
                 treinar mais loops """

    """def fatorial(n):
        fat = 1
        counter = n
        while counter > 1:
            fat *= counter
            print(fat)
            counter -= 1
        print(f'\nO fatorial {n}! é igual a {fat}.\n')"""

    def fatorial(n):
        fat = 1
        fat *= n
        print(fat)
        fatorial(n-1)
        return print(f'\nO fatorial {n}! é igual a {fat}.\n')
        
        
    #6
    def prime (n):
        if n == 0 or n == 1:
            print(f'O número {n} é primo pq é 0 ou 1')
        #elif n % 2 == 0:
         #       print(f'O número {n} é primo')
        for i in range(2,n-1):#(2,3,4,5)
            if n % i == 0: #and (i != 1 and i != n):
                print(f'{i} O número {n} não é primo')
                break#in case x appears at least one time than do y
            else:
                print(f'O número {n} é primo')


    #7
    def listSum(n,n2):
        list = [n, n2, 4, 2]
        #num = 0
        sum= 0
        for num in list:
            print(num) #ta pegando o ultimo num da interacao, talvez usar while
            sum += num
            continue
        print(f"A soma é {sum}")

    def listSum2(n,n2):
        list = [n, n2, 4, 2]
        counter= 1
        #while list != list[-1]:
        #sum = 0 + num

        print(f"A soma é {sum}")

    #8 
    def bigNum(n, n2):
        myList = [n, n2, 4, 2,n2]
        if not isinstance(n, (int)):
            return "Não é inteiro"
        else:
            nn=0
            count=0
            while myList[nn]> len(myList);

                if myList[nn] > myList[nn+1]:
                    bigger =myList[nn]
                print(myList[nn+1])
                print(bigger)
                print(nn)
                nn+=2
                print(nn)
                else: bigger = myList[nn+1]
                nn+=1
                print(nn)
                count ++
                ''' if myList[1] > myList[0]: 
                    big = myList[1]
                    n = myList[big+1]   
                else: big = myList[0]
                n = myList[big+2]

                bigNum(big,n) # e va pro proximo ate chegar no numfinal'''
    #10
    def invString(s):
        if not isinstance(s, (str)):
            print("Não é uma palavra")
        else: inversa = s[-1]
    #11
    def vowel(n):
        print(n)
        listWord = list(s)
        print(listWord)
        #transformar s em lista
        counter = 0
        #while counter =5
        vogais = ["a","e","i","o","u"]
        for letter in listWord:
            for v in vogais:
                if letter == v:
                    qntd +=1
                    print(qntd)
               # counter+=1


    
    ''''def teste(n,n2,option):
        print(f"Opção escolhida: {option}")'''
#for function in main():

    functions = {"add": lambda:addF(n,n2),
                "sub": lambda: subF(n,n2),
                "mult": lambda: mult(n,n2),
                "div": lambda: div(n,n2),
                "fatorial": lambda: fatorial(n),
                "primo": lambda: prime(n),
                "listsum": lambda: listSum(n, n2),
                "bignum": lambda: bigNum(n,n2),
                "invstr": lambda: invString(s),
                "vogal": lambda: vowel("s")
               }    
    print(functions.keys())
    option = input("Qual operação deseja realizar? Caso você deseje sair digite \"sair\"\n ").lower()


        #if option == function:
        #option
   # option = input("Qual operação deseja realizar? Caso desejes sair digite \"sair\" ").lower()
    sair = ("sair" or "exit" or "dar o fora"or "fechar o programa").lower()
    while option != sair:
    

        if option in functions:
            functions[option]()
            option2=input("Use o programa novamente ou saia, o que você escolhe?\n ")
        #option = input("Qual operação deseja realizar? Caso desejes sair digite \"sair\" ").lower()
        
        #if option == "addf" :#or "soma" or "Soma": nao entendo pq nao passa deste comando e aceita qualquer coisa
         #   addF(n,n2)
        #elif option == "subf":
         #   subF(n,n2)
        #elif option == "sair":
        #    break

        else: print("A alternativa não existe")

        if option2 != sair:
            continue
        else:
            print("Você saiu do programa com sucesso")
            break


if __name__== "__main__":
    main(int(input('Insira o primeiro número:\n')),(int(input('Insira o segundo número:\n'))),
     str(input("Digite uma palavra \n")))
