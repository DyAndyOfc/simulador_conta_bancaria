minha_conta_corrente = 2500.0
cartao_credito = 1700.0
poupanca = 0.0

while True:
    print('\n=== Menu Principal ===\n')
    print('''
[1] Saldo conta corrente
[2] Saldo cartão de crédito
[3] Poupança
[4] Fazer um depósito
[5] Fazer um saque
[0] Sair
''')

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        print(f'O seu saldo da conta corrente é R$ {minha_conta_corrente:.2f}')

    elif opcao == '2':
        print(f'O limite do seu cartão de crédito é R$ {cartao_credito:.2f}')

    elif opcao == '3':
        print(f'O saldo da sua poupança é R$ {poupanca:.2f}')

    elif opcao == '4':
        valor_deposito = float(input('Digite o valor do depósito: R$ '))
        if valor_deposito > 0:
            minha_conta_corrente += valor_deposito
            print(f'Depósito realizado com sucesso! Novo saldo: R$ {minha_conta_corrente:.2f}')
        else:
            print("Valor inválido. Depósito deve ser maior que zero.")

    elif opcao == '5':
        valor = float(input('Digite o valor do saque: R$ '))
        if valor > 0 and valor <= minha_conta_corrente:
            minha_conta_corrente -= valor
            print(f'Saque realizado! O saldo atual é R$ {minha_conta_corrente:.2f}')
        else:
            print('Saque não autorizado. Por favor, verifique o valor!')

    elif opcao == '0':
        print('Saindo do sistema. Até logo!')
        break

    else:
        print('Opção inválida! Tente novamente.')
