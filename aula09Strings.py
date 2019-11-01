def testastrings():
    frase = 'Curso em Video Python'
    print(frase[9])
    print(frase[9:13])
    print(frase[9:13:2])
    print(frase[:5])
    print(frase[5:])
    print(frase[9::3])
    print(len(frase))
    print(frase.count('o'))
    print(frase.count('o',0,13))
    print(frase.find('deo'))
    print(frase.find('android'))
    #como nao existe ele retorna -1
    print('Curso'in frase)
    print(frase.replace('Python','Android'))
    print(frase.upper())
    print(frase.lower())
    print(frase.capitalize())
    print(frase.title())
    frase = '   Aprenda Python   '
    print(frase.strip())
    print(frase.rstrip())
    print(frase.lstrip())
    print(frase.split())
    frase = ['Aprenda', 'Python', 'travez']
    print('-'.join(frase))
    frase = 'Curso em Video Python'
    print(frase.split().pop(2))
    print(len(frase)-frase.count(' '))

def testanumero():
    numero = int(1834)
    print(numero)
    n = str(numero)
    print(n[3])
    print(n[2])
    print(n[1])
    print(n[0])
    num = int(input('informe numero '))
    u = num //1 % 10
    d = num //10 % 10
    c = num //100 % 10
    m = num //1000 % 10
    #pega o numero divide por 1 e pega o resto que sera unidade centena...
    print('unidade {}'.format(u))
    print(f'unidade = {u}' )
    print(f'dez = {d}' )
    print(f'cent = {c}' )
    print(f'milhar = {m}' )

def testacidade():
    cid = str(input('onde nasceu ')).strip()
    print(cid[:5].upper() == 'SANTO')

def desafio25():
    nom = str(input('seu nome')).strip()
    #para já tirar os espaços em brancos antes e depois
    print(nom.find('Silva'))
    print('silva' in nom.lower())

def desafio26():
    frase = str(input('digite frase ')).lower().strip()
    f = frase.count('a')
    print(f'Letra a = {f} vezes')
    l = frase.find('a')+1
    x = frase.rfind('a')+1
    print(f'primeira letra a {l}')
    print(f'ultimo letra a {x}')

def desafio27():
    n = str(input('entre nome ')).strip()
    nome = n.split()
    print(nome)
    print(nome[0])
    print(f'primeiro nome {nome[0]}')
    print(f'ultimo nome {nome[len(nome)-1]}')

def aula10():
    tempo=int(input("Quantos anos tem carro?"))
    print('Carro novo'if tempo<=3 else 'carro veio')
    print('fim')

def desafio28():
    from random import randint
    from time import sleep
    computador = randint(0, 5)
    print('Vou pensar em um nr entre 0 e 5, tente adivinhar ')
    print('-=-'*20)
    jogador = int(input('Em q nr pensei '))
    print('Processando...')
    sleep(3)
    if jogador == computador:
        print('vc venceu ')
    else:
        print('perdeu, eu pensei em {} e não {} '.format(computador, jogador))

def desafio29():
    vel = int(input('Velocidade do seu carro '))
    if vel > 80:
        multa = vel-80
        print('Multado em {}'.format(multa*7))
    else:
        print('parabéns dentro da veloci permit ')

def desafio30():
    num = int(input('entre numero '))
    resul = num % 2
    'ver o resto da divisão'
    if resul == 0:
        print('par ')
    else:
        print('impar ')

def desafio31():
    #Exercicio Python #031 - Custo da Viagem
    dist = float(input('Qual distancia '))
    if dist <= 200:
        preço = dist*0.50
    else:
        preço = dist*0.45
    print('passagem = ', preço)
    print('Preço R$ {:.2f}'.format(preço))
    print(f'Preço de novo = R$ {preço}')

def desafio31a():
    # IF SIMPLIFICADO
    dist = float(input('Qual distancia '))
    preço = dist * 0.50 if dist <= 200 else dist * 0.45
    print(f'Preço de novo = R$ {preço}')

def desafio32():
    from datetime import date
    #Exercicio Python 032 - Ano Bissexto
    ano = int(input(' ano a analisar? 0 para o ano atual '))
    if ano == 0:
        ano = date.today().year

    # divisivel por 4, e por 100 ou por
    # IF COM AND E COM OR
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('Bissexto')
    else:
        print('não bissexto')

def desafio33():
    #Exercicio Python #033 - Maior e menor valores
    a = int(input('primeiro valor '))
    b: int = int(input('segundo valor '))
    c = int(input('terceiro valor'))
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c
    print(f'Menor = {menor}')
    print(f'Maior = {maior}')

def desafio34():
    #Exercicio Python #034 - aumentos multiplos
    sal = float(input('salario '))
    if sal <= 1250:
        novo = sal * 1.15
    else:
        novo = sal * 1.1
    print(f'Salario novo é {novo}')

def coresnoterminal():
    #Curso Python #11 Cores Terminal - CODIGO ANSI
    #STYLE, 0 NONE, 1 BOLD, 4 UNDERLINE, 7 NEGATIVE
    #TEXT, 30 BRANCO, 31 VERMELHO, 32 VERDE, 33 AMARELO, 34 AZUL, 35 ROXO, 36 PISCINA, 37 CINZA
    #BACK, 40 BRANCO, 41 VERMELHO, 42 VERDE, 43 AMARELO, 44 AZUL, 45 ROXO, 46 PISCINA, 47 CINZA
    # \033[0:30:41m
    print('\033[1:31:43mOLA MUNDO\033[m')
    print('\033[4:33:45mOLA MUNDO\033[m')
    print('\033[7:30:46mOLA MUNDO\033[m')
    print('\033[1:35:42mOLA MUNDO\033[m')
    cores = {'limpa ':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m'}

# 2 mundo
# Estruturas de controle
# Fase 12 - condições aninhadas
# if carro.esquerda():
#   Bloco1
# elif carro.direita():  quantos elif s precisar
#   Bloco2
# else:
#   Bloco3

def aula12():
    nome = str(input('nome? '))
    if nome == 'Oberdan':
        print('lindo')
    elif nome == 'Pedro' or nome == 'Joao':
        print('comum')
    elif nome in 'Ana Claudia Joana':
        print('nome feminino')
    else:
        print('LASCOU')

# fase 13
def desafio036():
    print('\033[1:31:43mPROGRAMA EMPRÉSTIMO BANCÁRIO\033[m')
    valor = float(input('Valor imovel '))
    salario= float(input('Salario '))
    anos = int(input('quantos anos '))
    renda = float(salario * 0.30)
    prest = float(valor / (anos * 12))
    if prest <= renda:
        print(f"aprovado  R${(prest):.2f}")
        print(' para pagar casa de R$ {:.2f} em {} anos, a prestação será {:.2f}'.format(valor, anos, prest), end='')
    else:
        print('não aprovado ')


# desafio 39
# from datetime import date
# ano_atual = date.today().

def desafio041():
    from datetime import date
    atual = date.today().year
    nascimento = int(input('ano nascimento '))
    idade = atual - nascimento
    print(f'vc tem {idade} anos')
    if idade <= 9:
        print('menor ')
    elif idade >9 and idade <=14:
        print('infantil')
    elif idade <=19:
        print('junior ')
    else:
        print('senior ')

def desafio043():
    peso = float(input('peso? '))
    altura = float(input('altura? '))
    imc = peso / (altura ** 2)
    if imc <= 18.5:
        print('Abaixo ')
    elif imc < 25:
        print('Peso ideal ')
    elif imc < 30:
        print('Sobrepeso ')
    elif imc <= 40:
        print('Obesidade ')
    elif imc > 40:
        print('Mórbida ')
    print(f'imc = {(imc):.2f}')

def desafio045():
    from random import randint
    from time import sleep
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''
    [ 0 ] PEDRA
    [ 1 } PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('qual jogada? '))
    print('-=' * 10)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=' * 10)
    print('Computador jogou ', (itens[computador]))
    print('Jogador jogou ', (itens[jogador]))
    if computador == 0: #computador jogou pedra
        if jogador == 0:
            print('empate')
        elif jogador == 1:
            print('jogador vence')
        elif jogador == 2:
            print('computador vence')
        else:
            print('invalida')
    elif computador == 1: #computador jogou papel
        if jogador == 0:
            print('computador vence')
        elif jogador == 1:
            print('empate')
        elif jogador == 2:
            print('jogador vence')
        else:
            print('invalida')
    elif computador == 2: #cpu jogou tesoura
        if jogador == 0:
            print('jogador vence')
        elif jogador == 1:
            print('computador vence')
        elif jogador == 2:
            print('empate')
        else:
            print('invalida')
    else:
        print('invalida')

def desafio046():
    from time import sleep
    for cont in range(10, -1, -1):
        print(cont)
        sleep(0.5)
    print('buuuuummmm')

def desafio047():
    for cont in range(2, 51, 2):
        print(cont, end=' ')
    print('kbou')


def desafio049():
    #refazendo o desafio 9 = TABUADA
    num = int(input('Digite nr '))
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')


def desafio052():
    #numero primo
    num = int(input('digite o nr '))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0: # se num divisivel por contador = end='' serve para ele não pular de linha
            print('\033[33m', end='') #cores
            tot += 1
        else:
            print('\033[31m', end='')
        print(f'{c} ', end='× ')
    print(f'\n\033[m O numero {num} foi divisivel {tot} vezes')
    if tot == 2:
        print('primo ')
    else:
        print('não é primo')

def desafio053():
    # palindromo
    frase =  str(input('digite frase  ')).strip().upper() # RETIRA ESPAÇOS E POE EM MAIUSCULA
    palavras = frase.split() #separa palavras da frase
    junto = '*'.join(palavras) #junta com asteriscos
    print(f'frase = {frase}')
    print(f'palavras = {palavras}')
    print(f'junto = {junto}')
    inverso = ''
    for letra in range(len(junto) -1, -1, -1): #vai no junto começando no 19 e vai até o 0 de 1 em 1
        #print(junto[letra])
        inverso += junto[letra]
    #outra forma tira o for e coloca so o fatiamento abaixo
    fatiamento = junto[::-1]
    print(junto, inverso, fatiamento)

def desafio055():
    maior = 0
    menor = 0
    for p in range(1, 6):
        peso = float(input(f'peso {p} = '))
        if p == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print(f' maior {maior}')
    print(f' menor {menor}')


def reduztempocompilacaoexpressaoregular():
# copiado nao testado
	from timeit import timeit
	setup = """import re"""
	timeit("""re.match(r'\d{4}', '1234')""", setup)1.5645811557769775
	setup = """import re... milhar = re.compile(r'\d{4}')"""
	timeit("""milhar.match('1234')""", setup)0.4098658561706543


desafio055()









