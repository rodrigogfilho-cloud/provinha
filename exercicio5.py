altura = int(input("Qual a altura do seu reservaório em centímetros: "))
largura = int(input("Qual a largura do seu reservaório em centímetros: "))
comprimento = int(input("Qual o comprimento do seu reservaório em centímetros: "))
litrosdiario = float(input("Quantos litros você consome em média p/ dia?"))
#volume e litros
volumecm = altura * largura * comprimento #cm³
volumemetro = volumecm // 100 #m³
litroemagua = volumemetro * 1000
#autonomia
dias = litroemagua // litrosdiario


print(f"A capacidade máxima de água que se eu reservatório é capaz de suportar são {litroemagua} L")
print(f"A autonomia do seu reservatório é que ele aguente {round(dias,)} dias")
if dias < 2 :
    print("Seu consumo é elevado")
elif dias >= 2 and dias <= 7:
    print("Seu consumo é moderado")
elif dias > 7:
    print ("Seu consumo é reduzido")

    #algo de errado no resultado , analisar dps