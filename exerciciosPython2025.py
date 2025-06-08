
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
    def fatorial(n):
        fat = 1
        fat *= n
        print(fat)
        fatorial(n-1)
        return print(f'\nO fatorial {n}! é igual a {fat}.\n') 
    
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
            #print(num) #ta pegando o ultimo num da interacao, talvez usar while
            sum += num
            continue
        print(f"A soma é {sum}")

        '''def listSum2(n,n2):
            list = [n, n2, 4, 2]
            counter= 1
            #while list != list[-1]:
            #sum = 0 + num

            print(f"A soma é {sum}")'''

    #8 
    def bigNum(n, n2):
        myList = [n, n2, 4, 2,n2]
        bigger = myList[0]
        if not isinstance(n, (int)):
            return "Não é inteiro"
        else:
        #while myList[nn]> len(myList):
            for l in range(len(myList) - 1):# ate o fim da lista
                if (myList[l+1] > bigger):# se encontro um novo bigger eu salvo e se nao eu continuo com o anterior
                    bigger = myList[l+1]
                '''else:
                    bigger = myList[l]# aqui eu estava apagando o bigger anterior salvo
                # print(bigger)'''
            print(bigger)
            '''#while myList[nn]> len(myList):
            for l in myList:
                print(l)
                if myList[nn] > myList[nn+1]:
                    bigger =myList[nn]
                    print(myList[nn+1])
                    print(bigger)
                    print(nn)
                    nn+=2
                    print(nn)
                else: 
                    bigger = myList[nn+1]
                    print(nn)
                    nn+=1
                    print(myList[nn+1])
                    print(bigger)
                    print(nn)
            #def myList2(bigger,myList[nn])
            #count +=1
             if myList[1] > myList[0]: 
                    big = myList[1]
                    n = myList[big+1]   
                else: big = myList[0]
                n = myList[big+2]

                bigNum(big,n) # e va pro proximo ate chegar no numfinal'''
    
    #9     
    def smallNum(n, n2):
        myList = [n, n2,0,3, 4, 2,n2]
        small=myList[0]
        if not isinstance(n, (int)):
            return "Não é inteiro"
        else:
            for l in range(len(myList) - 1):# percorre ate o final da lista. -1 pq começa do 0
                if (myList[l+1] < small):
                    small = myList[l+1]
            print(small)
    
    #10
    def invString(s):
        inversa=[]
        if not isinstance(s, (str)):
            print("Não é uma palavra")
        else: 
            wList=list(s)
            print(wList)
            print(wList[-1])
            for w in wList[::-1]:
                print(w)
                inversa+=w
            #w[-1]
        # print(w[-1])    
        print("".join(inversa))
    
    #11
    def vowel(s):
        qntd =0
        listWord = list(s)
        #transformar s em lista
        counter = 0
        #while counter <5
        vogais = ["a","e","i","o","u"]
        for letter in listWord:
            for v in vogais:
                if letter == v:
                    qntd +=1
        print(f"O total de vogais na palavra é: {qntd}")

    #12   
    def celsToFaren(n):
        f = ((9/5)*n) +32
        print(f"{n}ºC = {f:.2f}ºF ")

    #13
    def average(n,n2):
        return "A média é ", (n+n2)/2
    
    #14
    def evenOdd(n):
        #if n/2 % 0:
        if n% 2 ==0:
            print(f"{n} é par")
        else: 
            print(f"{n} é impar")

    #15
    def leapYear(n):
        if n in range(4,n+1,4):
            print(f"ano {n} é bissexto")
        else:
            print(f"ano {n} não é bissexto")

    #16
    def mdc(n,n2):
        mult= 1
        if n < n2:
            stop = n
        else: 
            stop= n2
        for i in range(2,stop+1,1):
            print(i,"i")
            if (n % i == 0) and (n2 % i == 0):
                mult*=i
            else: 
                if (n % i != 0) and (n2 % i != 0):
                    print(mult,"mult")
                    break
        print(f"O mdc entre {n} e {n2} = {mult}")

    #17
    def mmc(n, n2):
        mult = 1
        a = n
        b = n2

        for i in range(2, max(n, n2) + 1):
            while n % i == 0 or n2 % i == 0:
                if n % i == 0:
                    n = n // i
                if n2 % i == 0:
                    n2 = n2 // i
                mult *= i#embaixo das condicoes pra nao repetir os multiplos
                print(f"Usando fator {i}: n = {n}, n2 = {n2}, mult = {mult}")
            if n == 1 and n2 == 1:
                break
        print(f"\nO mmc entre {a} e {b} = {mult}")
        #esta eu tive que pedir ajuda para o chat gpt poin nao consegui de jeito nenhum, entendo o que acontece no codigo

        '''def mmc(n,n2):
            mult= 1
            mult2=1
            k=n
            j=n2
            
            if n < n2:
                stop = n
            else: 
                stop= n2
                
            for i in range(2,stop+1,1):
                while ((n % i) == 0) or( (n2 % i) == 0):
                    if (n % i == 0):
                        nn= (n/i)
                        n =nn
                        mult*=i
                    else: 
                        continue
                    print(mult,"mult")
                    print(nn,"nn")
                    print(n,"n\n")
            
                        
                    if (n2 % i == 0):
                        nn2= (n2/i)
                        n2 = nn2
                        mult2*=i
                    else: 
                        continue
                    print(mult2,"mult2")
                    print(nn2,"nn2\n")
            
            
                    if mult ==mult2:
                        mmc = mult
                    else:
                        mmc = mult*mult2
                    print(mult2,"mult2")
                    print(mult2,"mult2")
                    print("mmc ",mmc)
                        
            print(f"O mmc entre {k} e {j} = {mmc}")


            def mdc(n,n2):
                mult= 1
                if n < n2:
                    stop = n
                else: 
                    stop= n2
                for i in range(2,stop+1,1):
                    print(i,"i")
                    if (n % i == 0) and (n2 % i == 0):
                        mult*=i
                    else: 
                        if (n % i != 0) and (n2 % i != 0):
                            print(mult,"mult")
                            break
                print(f"O mdc entre {n} e {n2} = {mult}")

            #17
            def mmc(n,n2):
                mult= 1
                if n < n2:
                    stop = n
                else: 
                    stop= n2
                for i in range(2,stop+1,1):
                    print(i,"i")
                    if (n % i == 0) and (n2 % i == 0):
                    #  nn == n/i nn2 == n2/i
                        if (n/i) > 1 and (n2/i) > 1:
                            mult*=i
                            print(mult,"mult")
                        else:
                            print(mult,"mult")
                print(f"O mmc entre {n} e {n2} = {mult}")
                
        def mmc(n,n2):
            mult= 1
            if n < n2:
                stop = n
            else: 
                stop= n2
            for i in range(2,stop+1,1):
                print(i,"i")
                if (n % i == 0) or (n2 % i == 0):
                    print(mult)
                #  nn == n/i nn2 == n2/i
                    #if (n/i) > 1 and (n2/i) > 1:
                    if (n/i) ==1:
                        break#entao pare de calcular n
                    if (n2/i) ==1:
                        break
                    if (n/i) ==1 and  (n2/i) ==1:
                        break
                    mult*=i
                    print(mult, "mu")
            print(f"O mmc entre {n} e {n2} = {mult}")
        mmc(40,22)

        def mmc(n,n2):
            mult= 1
            mult2=1
            if n < n2:
                stop = n
            else: 
                stop= n2
                
            for i in range(2,stop+1,1):
                if (n % i == 0):
                    nn= n/i
                    if (nn/i) ==1:
                        break#entao pare de calcular n 
                        mult*=i
                    
                    if (n2 % i == 0):
                        nn2= n2/i
                        if (nn2/i) ==1:
                            break
                        mult2*=i
                    
                if mult == mult2:
                    mult = mult2
                    mult2=1
                    mult*=mult
                    
                mmc = mult*mult2

                if (n/i) ==1 and  (n2/i) ==1:
                    break
                
                print(mult, "mult")
                print(mult2, "mult2")

                    
            print(f"O mmc entre {n} e {n2} = {mmc}")
        mmc(40,22)
                    
            print(f"O mmc entre {n} e {n2} = {mmc}")
        mmc(40,22) '''

        '''mult= 1
        if n < n2:
            stop = n
        else: 
            stop= n2
        for i in range(2,stop+1,1):
            print(i,"i")
            if (n % i == 0) and (n2 % i == 0):
                mult*=i
                print(mult,"mult")
        print(f"O mdc entre {n} e {n2} = {mult}")'''

        '''stop = n*n2
        for i in range(2,stop,1):
            print(i)
            if (n % i == 0):
                mult*=i
            print(mult)
            if (n2 % i == 0):
                mult*=i
                print(mult)
        print(f"O mdc entre {n} e {n2} = {mult}")'''
   
        '''mult= 1
        for i in range(2,1):
            mult*=(n % i == 0)
            print(mult)
            mult*=(n2 % i == 0)
        print(f"O mdc entre {n} e {n2} = {mult}")'''

    #18
    def fibonacci(n):
        fn= ((1.618**n)-(1-1.618)**n)/5**0.5
        print(round(fn))
        #n= ((1,6**n)-(1-1,6)**n)**0,5
    
    #19
    def sumDigit(n):
        qnt =0
        for digit in str(n):
            qnt+=1
        print(qnt)


    #20
    def decimalToBy(n,n2):
        p

    #21
    def removeRepetition(n,n2):
        llist = [1,n,4,6,4,7,1,4,0,n2,n]
        cleanList = set(llist)
        print(cleanList)

    #22 
    def palindromo(s):
        sInList=list(s)
        invert=[]
        for l in sInList[::-1]:
            invert += l
        if invert == sInList:
            print("É palindromo")
        else:
            print("Não é palindromo")
    #Nao achei que iria funcionar de primeira, mas foi to sentindo a evoluçao


    #23
    def evenList(n,n2):
            myList = [n, n2, 4, 2,n2]
            sum = 0
            for l in myList:
                if l%2 ==0:
                    sum +=l
            print(sum)

    #24
    def oddList(n,n2):
        myList = [n, n2, 4, 2,n2]
        sum = 0
        for l in myList:
            if l%2 !=0:
                sum +=l
        print(sum)


    #27
def frequency():
        llist = [1,4,6,4,7,1,4,0]
        dict={}
        qnt = 0
        
        for elem in set(llist):
            for l in llist:
                if elem ==l in llist:
                    qnt += 1
            (f"A quantidade de {elem} na lista {llist} = {qnt}\n")
        
            dict.update({elem: qnt})
            qnt=0
        for key,value in dict.items():#itwm() pego todos os key, value da lista e o for me retorna a string de cada
            print(f"A quantidade de {key} na lista {llist} = {value}\n")
        
                    
def frequency():
        llist = [1,4,6,4,7,1,4,0]
        dict={}
        qnt = 0
        
        for elem in set(llist):
            for l in llist:
                if elem ==l in llist:
                    qnt += 1
            (f"A quantidade de {elem} na lista {llist} = {qnt}\n")
        
            dict.update({elem: qnt})
            qnt=0
        for keyValue in dict:
            print(f"A quantidade de {keyValue.keys()} na lista {llist} = {keyValue.values()}\n")
        


    def frequency():
        list = [1,4,6,4,7,1,4,0]
        #indice=0
        qnt = 0
        for l in list:
            for indice in range(len(list) -1):
                if list[indice] ==l:
                    qnt += qnt
                    print(f"A quantidade de {list[indice]} na lista {list} = {qnt}\n")    
                    #dict {list[indice]: qnt,
                    #[indice]: qnt}
    def frequency():
        list = [1,4,6,4,7,1,4,0]
        #indice=0
        qnt = 0
        
        #for indice in range(len(list) -1):
        for l in list:
            if l ==l:
                qnt += 1
                print(f"A quantidade de {l} na lista {list} = {qnt}\n")
                    #dict= list[indice]: qnt,
                    #[indice]: qnt,
frequency()
    
    #28
    def potencia(n,n2):
        print(n**n2)
        return n**n2
    
    #29
    def listSearcher(n):
        myList=[1,3,5,7,9,5,2]
        for l in myList:
            if l==n:
                print(f"{n} está na lista {myList}")
        else:
            print(f"{n} não está na lista {myList}")
        
    #30
    def sumMatrix():
            matrix = [[1,0,7,1,4,0],[2,3,6,8],[1,4,7,6,5]]
            summ = 0
            for listt in matrix:
                for num in listt:                    
                    print(f"somando {num} a soma {summ}")
                    summ+=num
            print(summ)

            

    
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
                "inversa": lambda: invString(s),
                "vogal": lambda: vowel(s),
                "cemf": lambda: celsToFaren(n),
                "media": lambda: average(n,n2),
                "imparpar": lambda: evenOdd(n),
                "bissexto": lambda: leapYear(n)

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

        else: print("A alternativa não existe")
        option=input("Tente novamente ou saia, o que você escolhe?\n ")
        if option == sair:
            print("Você saiu do programa com sucesso")
            break
        else:
            continue

                #option = input("Qual operação deseja realizar? Caso desejes sair digite \"sair\" ").lower()
        
        #if option == "addf" :#or "soma" or "Soma": nao entendo pq nao passa deste comando e aceita qualquer coisa
         #   addF(n,n2)
        #elif option == "subf":
         #   subF(n,n2)
        #elif option == "sair":
        #    break



if __name__== "__main__":
    main(int(input('Insira o primeiro número:\n')),(int(input('Insira o segundo número:\n'))),
     (input("Digite uma palavra:  "))).strip()

    '''option = ""
    printf("    1 - addF\n
    2 - subF\n
    3 - mult\n
    4 - div\n
    #fatorial(n)
    #prime(n)
    #listSum(n, n2)
    #bigNum(n,n2)")
    while option == "sair":
        option = input("Qual operação deseja realizar? Caso deseje sair digite \"sair\" ").lower()
        
        if option == "addf" :#or "soma" or "Soma": nao entendo pq nao passa deste comando e aceita qualquer coisa
            addF(n,n2)
        elif option == "subf":
            subF(n,n2)
        #elif option == "sair":
        #    break

        else: print("A alternativa não existe")
        option=input("Desejas tentar de novo? ")
        if option == "sim" or "s":
            continue
        #elif option == "sair":
        #    break
    print("Tu saistes programa com sucesso")
    
            # if again is written then start again if break then break
''' 
'''      
    while option != "sair":
        #option = input("Qual operação deseja realizar? Caso desejes sair digite \"sair\" ").lower()
        
        if option == "addf" :#or "soma" or "Soma": nao entendo pq nao passa deste comando e aceita qualquer coisa
            addF(n,n2)
        elif option == "subf":
            subF(numbers)
        #elif option == "sair":
        #    break

        else: print("A alternativa não existe")
        option=input("Desejas tentar de novo? ")
        if option == "sim" or "s":
            continue
        #elif option == "sair":
        #    break
    print("Tu saistes do programa com sucesso")'''



#main(int(input('Insira o primeiro número:\n')),(int(input('Insira o segundo número:\n'))))
#print(inp + \n)
