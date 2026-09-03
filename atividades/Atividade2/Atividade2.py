nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
plano=input("Tem plano de saúde?\n1)Sim  2)Não  ")
plano_de_saude= plano=="1"
print("Seu nome é",nome,",Você tem",idade,"anos.\nTem plano?",plano_de_saude,"\nVocê foi aceito?",plano_de_saude)


