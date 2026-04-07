pratos = int(input("Quantos pratos você consumiu? "))
prato = pratos * 25
desconto10 = (prato * 0.9)

desconto20 = (prato * 0.8)

if pratos < 4:
    print (f"Você não teve descontos e vai pagar R${prato}")
elif pratos >= 4 and pratos <= 7:
    print (f"Você ganha 10% de desconto. Que fica R$ {round(desconto10, 2) }")
elif pratos >= 8 :
    print(f"Você ganha 20% de desconto. Que fica R$ {round(desconto20, 2)}")
