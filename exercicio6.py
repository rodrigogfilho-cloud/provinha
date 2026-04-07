
gasolina = 5.89
alcool = 4.42
combustivel = input("Você deseja abastecer com alcool ou gasolina ? ").upper()
if combustivel == "ALCOOL" or combustivel == "GASOLINA":
    print("")
else:
    print("Não consegui entender")
    exit()

litros = int(input("Quantos litros você deseja abastecer ? "))
print("")
precoA = litros * 4.42
precoG = litros * 5.89
desconto3A = precoA * 0.97
desconto5A = precoA * 0.95
desconto4G = precoG * 0.96

desconto6G = precoG * 0.94

if combustivel == "ALCOOL" and litros <= 20 :
    print(f"Você ira pagar R${round(desconto3A,2)}")
elif combustivel == "ALCOOL" and litros > 20:
    print(f"Você irá pagar R${round(desconto5A,2)}")
elif combustivel == "GASOLINA" and litros <= 20:
    print(f"Você ira pagar R${round(desconto4G,2)}")
elif combustivel == "GASOLINA" and litros > 20:
    print(f"Você ira pagar R${round(desconto6G,2)}")
