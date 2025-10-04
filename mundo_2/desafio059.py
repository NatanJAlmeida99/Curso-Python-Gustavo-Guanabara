from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
    print(
        """
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa 
        """
    )
    print(">" * 5, end=" ")
    opcao = int(input("Qual é a sua opção? "))

    if opcao == 1:
        print(f"A soma entre {n1} + {n2} é {n1 + n2}")
        print("=-=" * 15)
        sleep(1)
    elif opcao == 2:
        print(f"O resultado de {n1} x {n2} é {n1 * n2}")
        print("=-=" * 15)
        sleep(1)
    elif opcao == 3:
        maior = 0
        if maior > n1:
            maior = n1
            print(f"Entre {n1} e {n2} o maior valor é {maior}")
            print("=-=" * 15)
            sleep(1)
        else:
            maior = n2
            print(f"Entre {n1} e {n2} o maior valor é {maior}")
            print("=-=" * 15)
            sleep(1)
    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        sleep(1)
    elif opcao == 5:
        print("Finalizando...")
        sleep(1)
    else:
        print("Opção inválida. Tente novamente")
        print("=-=" * 15)
        sleep(1)
print("=-=" * 15)
print("Fim do programa! Volte sempre")