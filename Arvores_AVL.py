#Importar base de dados
import csv

DADOS = {
    'VALOR': []
}

with open('Ajuste patrimonial - Saldos (R$).csv', newline='') as basedados:
    leitor = csv.reader (basedados, delimiter=';', quotechar='|')
    for linha in leitor:
        DADOS['VALOR'].append(float(linha[1]))


#Código para balancear toda a árvore
class NoAVL:
    def __init__(self, info):
        self.info = info
        self.esquerda = None
        self.direita = None


def altura(no):
    if no is None:
        return 0
    else:
        altura_esquerda = altura(no.esquerda)
        altura_direita = altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1


def fator_balanceamento(no):
    if no is None:
        return 0
    return altura(no.esquerda) - altura(no.direita)


def rotacao_rr(pai):
    filho = pai.direita
    pai.direita = filho.esquerda
    filho.esquerda = pai
    return filho


def rotacao_ll(pai):
    filho = pai.esquerda
    pai.esquerda = filho.direita
    filho.direita = pai
    return filho


def rotacao_lr(pai):
    filho = pai.esquerda
    pai.esquerda = rotacao_rr(filho)
    return rotacao_ll(pai)


def rotacao_rl(pai):
    filho = pai.direita
    pai.direita = rotacao_ll(filho)
    return rotacao_rr(pai)


def balancear(no):
    if no is None:
        return no

    fator_bal = fator_balanceamento(no)

    if fator_bal > 1:
        if fator_balanceamento(no.esquerda) > 0:
            no = rotacao_ll(no)
        else:
            no = rotacao_lr(no)
    elif fator_bal < -1:
        if fator_balanceamento(no.direita) > 0:
            no = rotacao_rl(no)
        else:
            no = rotacao_rr(no)

    return no


def inserir(raiz, valor):
    if raiz is None:
        return NoAVL(valor)
    elif valor < raiz.info:
        raiz.esquerda = inserir(raiz.esquerda, valor)
        raiz = balancear(raiz)
    elif valor >= raiz.info:
        raiz.direita = inserir(raiz.direita, valor)
        raiz = balancear(raiz)

    return raiz

def busca_na_arvore(no, valor):
    if no is None:
        return False
    elif no.info == valor:
        return True
    elif valor < no.info:
        return busca_na_arvore(no.esquerda, valor)
    else:
        return busca_na_arvore(no.direita, valor)

def exibir_arvore(no, nivel=0):
    if no is not None:
        exibir_arvore(no.direita, nivel + 1)
        print("  " * nivel, end="")
        if no == raiz:
            print("R.", end="")
        print(no.info)
        exibir_arvore(no.esquerda, nivel + 1)

#Teste do código
raiz = None

print ('MOSTRA TODOS OS DADOS')
for valor in DADOS['VALOR']: 
    raiz = inserir(raiz, valor)
    
print ('ÁRVORE AVL COMPLETA BASEADA NOS SALDOS DO AJUSTE PATRIMONIAL:')
exibir_arvore(raiz)

print ('\nBUSCA DADO ESPECÍFICO')
a = 99372.07
b = 532.2
resultado = busca_na_arvore(raiz, a)
resultado2 = busca_na_arvore(raiz, b)
if resultado:
    print ('Achou o número ', a, ' na árvore!')
else:
    print ('Não achou o número %.2f!' %(a))

if resultado2:
    print ('Achou o número ', b, ' na árvore!')
else:
    print ('Não achou o número %.2f!' %(b))

