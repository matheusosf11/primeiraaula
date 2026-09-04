print("SISTEMA DE DIVISÃO DE CONTA DE BAR/RESTAURANTE")

valor_total=float(input("Digite o valor total da sua conta: "))
qtd_pessoas=int(input("Quantas pessoas dividirá a conta com vc?"))
valor=(valor_total/qtd_pessoas)

print("O valor total da conta ficou R$",valor_total,"e são um total de",qtd_pessoas,"pessoas,cada pessoa deve pagar R$",valor,".")