preco = int(input('Digite o valor do produto R$: '))
opcao = int(input('Digite a forma de pagamento:\n [1]-À vista dinheiro / À vista cheque\n [2]- À vista no cartão\n '
                  '[3]- 2x no cartão\n [4]-3 ou mais parcelas no cartão'))

if opcao == 1:
    novoPreco = preco*0.9
elif opcao == 2:
    novoPreco = preco*0.95
elif opcao == 3:
    novoPreco = preco
elif opcao == 4:
    novoPreco = preco*1.2
else:
    print('Opção inválida')
print(f'O preço do produto será: { novoPreco }')