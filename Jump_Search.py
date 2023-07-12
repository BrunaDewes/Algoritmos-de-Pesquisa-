#Importar base de dados
import csv

DADOS = {
    'VALOR': []
}

with open('Ajuste patrimonial - Saldos (R$).csv', newline='') as basedados:
    leitor = csv.reader (basedados, delimiter=';', quotechar='|')
    for linha in leitor:
        DADOS['VALOR'].append(float(linha[1]))

#Jump Search
import math

def jumpSearch( arr , x , n ):
	
	# Encontrar o tamanho do bloco a ser saltado
	step = math.sqrt(n)
	
	# Encontrar o bloco onde o elemento está presente (se estiver)
	prev = 0
	while arr[int(min(step, n)-1)] < x:
		prev = step
		step += math.sqrt(n)
		if prev >= n:
			return -1
	
	# Fazendo uma busca linear por x no bloco começando com anterior
	while arr[int(prev)] < x:
		prev += 1
		
		# Se atingir o próximo bloco ou o fim do array, o elemento não está presente
		if prev == min(step, n):
			return -1
	
	# Se o elemento é encontrado
	if arr[int(prev)] == x:
		return prev
	
	return -1

# Código p/ testar a função
print('MOSTRA DADO ESPECÍFICO')
x = 109289.24
n = len(DADOS['VALOR'])

# Encontra o índice de 'x' usando Jump Search
v = sorted (DADOS['VALOR'])                         #põe em ordem já que o jump só faz com coisas em ordem
index = jumpSearch(v, x, n)

# Printa o índice onde 'x' está localizado
print("Número" , x, "está no índice" ,"%.0f"%index)

print('\nMOSTRA TODOS OS DADOS')
for valor in DADOS['VALOR']: 
	x = valor
	n = len(DADOS['VALOR'])

	# Encontra o índice de 'x' usando Jump Search
	v = sorted (DADOS['VALOR'])                         #põe em ordem já que o jump só faz com coisas em ordem
	index = jumpSearch(v, x, n)

	# Printa o índice onde 'x' está localizado
	print("Número" , x, "está no índice" ,"%.0f"%index)