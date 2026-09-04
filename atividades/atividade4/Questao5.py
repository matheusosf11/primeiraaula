print("Bem vindo a festa!")
idade=int(input("Para entrar na festa,digite sua idade: "))
vip=input("Você possui cartão VIP?\nDigite 1 para sim e 0 para não: ")
time=input("Você faz parte da organização do evento?Digite 1 para sim e 0 para não: ")

if idade>=18 and vip=="1" or time=="1":
    print("Acesso liberado! Boa festa.")
elif idade<18 and vip=="1":
    print("Acesso negado! Você possui cartão vip porém é menor de idade!")
elif idade>18 and vip=="0":
    print("Acesso negado! Você é maior de idade,mas não possui o cartão VIP para entrar.")
elif idade>=18 and time=="1":
    print("Acesso liberado! Voce faz parte da organização do evento.")
else:
    print("Acesso negado!")
