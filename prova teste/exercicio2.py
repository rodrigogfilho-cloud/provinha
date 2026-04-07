#Faça um algoritmo que receba um valor de uma compra e receba o número de prestações, apresente o valor das prestações sem juros e com 2 casas decimais.
valordecompra = float(input("Digite o valor que você gastou em sua compra: "))
prestacoes = int(input("Quantas prestações o senhor(a) deseja fazer? "))
print(f"Irá ficar {prestacoes} parcelas de R${round(valordecompra / prestacoes, 2)} ")