altura = int(input("Qual a altura do seu reservaório em metros: "))
largura = int(input("Qual a largura do seu reservaório em metros: "))
comprimento = int(input("Qual o comprimento do seu reservaório em metros: "))
litrosdiario = float(input("Quantos litros você consome em média p/ dia?"))
#volume e litros
volumem = altura * largura * comprimento * 1000#m³


#autonomia
dias = volumem // litrosdiario


print(f"A capacidade máxima de água que se eu reservatório é capaz de suportar são {volumem} L")
print(f"A autonomia do seu reservatório é que ele aguente {round(dias,)} dias")
if dias < 2 :
    print("Seu consumo é elevado")
elif dias >= 2 and dias <= 7:
    print("Seu consumo é moderado")
elif dias > 7:
    print ("Seu consumo é reduzido")

    #algo de errado no resultado , analisar dps