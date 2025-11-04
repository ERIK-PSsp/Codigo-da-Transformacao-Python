def calcula_media(notas):
    """Calcula a média de uma lista de notas."""
    # sum(notas) soma todos os itens da lista
    # len(notas) conta quantos itens há na lista
    return sum(notas) / len(notas)  # 
def verificar_aprovacao(media, presenca):
    """
    Verifica se o aluno foi aprovado (média >= 7 e presença >= 75%).
    """
    if media >= 7 and presenca >= 75:
        return "O aluno(a) está aprovado(a)🥳" 
    
    else:
        if media < 7 and presenca < 75:
            return "O aluno(a) está reprovado(a) por média e presença😢"
        
        elif media < 7:
            return "O aluno(a) está reprovado(a) por média😢"
        
        else:
            return "O aluno(a) está reprovado(a) por presença😢"

print("Cálculo de Média e Verificação de Aprovação")
print("\n-------------------------------------------")

num_notas = int(input("Quantas notas o aluno tem? "))


# Notas do aluno
notas_aluno = []
for i in range(num_notas):
    nota = float(input(f"Insira a nota {i+1}: "))
    notas_aluno.append(nota)
'''
notas_aluno = input("Insira as notas do aluno separadas por um espaço: ")
notas_aluno = [float(nota) for nota in notas_aluno.split(' ')]
'''
# Presença do aluno
presenca_aluno = float(input("Insira a presença do aluno (em %): "))
# Chamando as funções
media_final = calcula_media(notas_aluno)
status_aluno = verificar_aprovacao(media_final, presenca_aluno)
# Exibindo o resultado
print(f"Notas: {notas_aluno}")
print(f"Média: {media_final:.2f}")
print(f"Presença: {presenca_aluno:.2f}%")
print(f"Status: {status_aluno}")