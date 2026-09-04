idade=int(input("Insira sua idade: "))
if idade>=18 and idade<60:
    print("Você é obrigado a votar")
elif idade>60 or idade>=16:
    print("Para você ,votar é opcional.")

else:
    print("Você ainda não é obrigado a votar")