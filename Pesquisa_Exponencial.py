#Importar base de dados
import csv

DADOS = {
    'VALOR': []
}

with open('Ajuste patrimonial - Saldos (R$).csv', newline='') as basedados:
    leitor = csv.reader (basedados, delimiter=';', quotechar='|')
    for linha in leitor:
        DADOS['VALOR'].append(float(linha[1]))

# A ideia é determinar um intervalo no qual o valor alvo reside e realizar uma Pesquisa binária dentro desse intervalo
# Algoritmo de busca binária para retornar a posição da chave `x` na sublista A[esquerda…direita]
def binarySearch(A, esquerda, direita, x):
 
    # Condição base # (o espaço de busca está esgotado)
    if esquerda > direita:
        return -1
 
    # encontra o valor médio no espaço de busca e compara com a chave
 
    meio = (esquerda + direita) // 2
 
    # O estouro de # pode acontecer. Usar abaixo mid = esquerda + (direita - esquerda) // 2
 
    # Condição base # (uma chave é encontrada)
    if x == A[meio]:
        return meio
 
    # descarta todos os elementos no espaço de busca correto, incluindo o elemento do meio
    elif x < A[meio]:
        return binarySearch(A, esquerda, meio - 1, x)
 
    # descarta todos os elementos no espaço de busca à esquerda, incluindo o elemento do meio
    else:
        return binarySearch(A, meio + 1, direita, x)
 
# Retorna a posição da chave `x` em uma determinada lista `A` de comprimento `n`
def exponentialSearch(A, x):
    # caso básico
    if not A:
        return -1
 
    bound = 1

    # encontra o intervalo no qual a chave `x` residiria
    while bound < len(A) and A[bound] < x:
        bound *= 2                                # calcula a próxima potência de 2
 
    # chama busca binária em A[bound/2 … min(bound, n-1)]
    return binarySearch(A, bound // 2, min(bound, len(A) - 1), x)
 
 
#Algoritmo de pesquisa exponencial
print('MOSTRA TODOS OS DADOS')
for valor in DADOS['VALOR']:
    index = exponentialSearch(sorted(DADOS['VALOR']), valor)
    
    if index != -1:
        print('Elemento', valor, 'encontrado na posição', index)
    else:
        print('Elemento', valor, 'não encontrado na lista')

print('\nMOSTRA DADO ESPECÍFICO')
a = 97771.33
index = exponentialSearch(sorted(DADOS['VALOR']), a)
        
if index != -1:
    print('Elemento', a, 'encontrado na posição', index)
else:
    print('Elemento', a, 'não encontrado na lista')