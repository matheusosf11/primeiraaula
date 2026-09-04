saldo=float(input("Insira seu saldo atual: "))
saque=float(input("Qual valor você gostaria de sacar? "))

saldo_pos_saque= saldo-saque

if saque<=saldo:
    print("Saque realizado com sucesso! Saldo atual: R$",saldo_pos_saque,".")

else:
    print("Saldo insuficiente para realizar esta operação.")