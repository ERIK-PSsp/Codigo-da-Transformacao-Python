print ("\n-----------------------------")
print ("\nSeja bem-vindo a tela.")
print ("\n-----------------------------")


pessoa_nome = input ( ' Olá, qual é o seu nome? ' )
print ("\n-----------------------------")

print (f"Seja bem vindo {pessoa_nome}")
print ("\n-----------------------------")

pessoa_idade = int (input (f"{pessoa_nome}, quantos anos você tem?"))
if pessoa_idade >= 18:
    print ('Parabéns por ser maior de idade')
else: 
    print (f'Que pena, você tem {pessoa_idade} anos, você ainda é menor de idade')

print ("\n-----------------------------")
pessoa_altura = float (input ("Nossa, qual a sua altura?"))
if pessoa_altura >= 1.80:
    print ('Caramba, você é gigante!!!')
    print ("\n-----------------------------")

print (f" Oi {pessoa_nome}, então você tem {pessoa_idade} anos, e {pessoa_altura}m. 😮 Uau!")
print ("\n-----------------------------")