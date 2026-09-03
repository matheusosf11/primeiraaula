nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media= (nota1+nota2)/2
falta=int(input("Qual sua porcentagem de frequencia?"))
print("Sua média foi",media)
aprovado = media>=6 and falta>=75
print("O aluno passou?",aprovado)