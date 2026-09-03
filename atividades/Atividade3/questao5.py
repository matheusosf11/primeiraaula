compra=float(input("Digite o valor da sua compra: "))
vip = bool(input("Voce é VIP? \n1)Sim, sou VIP.\n0) Não sou VIP."))
desconto = compra>200 or vip==1

print(desconto)

