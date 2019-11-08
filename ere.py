s = 'Regular expressions can contain both special and ordinary characters'
print(s[10:25])
print(s)

def buscainformacoesnaimagem():

    import re
    import pytesseract as ocr
    from PIL import Image

    phrase = ocr.image_to_string(Image.open('Ponto141020191.jpg'), lang='por')
    #print(phrase)
    # FUNCIONOU padrao1 = re.search(r'(021)( - )(\w+)( )(\w+)( )(\w+)( )([(])(\w+)', phrase)
    cont = re.findall(r'(021)', phrase)
    print(len(cont))

    print('cont => ', cont)
    padrao1: Optional[Match[str]] = re.search(r'(negat.([)]))( )(\w+)(:)(\w+)', phrase)
    padrao2: Optional[Match[str]] = re.findall(r'(negat.([)]))( )(\w+)(:)(\w+)', phrase)
    print('padrao 2 => lista ', padrao2)
    #if padrao1:
    #if padrao1 is not None:
    for encontroupadrao in padrao2:
        #padrao1: Optional[Match[str]] = re.search(r'(negat.([)]))( )(\w+)(:)(\w+)', phrase)
        print('padrao1 group => ',padrao1.group(4,5,6))
        #print('padrao2 group => ',padrao2.group(4,5,6))
        print('padrao1 => ',padrao1)
        banconegativo = padrao1.group(4)+padrao1.group(5)+padrao1.group(6)
        print('banconegativo =>', banconegativo)
        continue

buscainformacoesnaimagem()

def buscainformacoesnaimagem():


    import re
    import pytesseract as ocr
    from PIL import Image
    from datetime import datetime

    phrase = ocr.image_to_string(Image.open('Ponto141020191.jpg'), lang='por')
    #print(phrase)
    # FUNCIONOU padrao1 = re.search(r'(021)( - )(\w+)( )(\w+)( )(\w+)( )([(])(\w+)', phrase)
    cont = re.findall(r'(021)', phrase)
    print(len(cont))

    print('cont => ', cont)
    padrao1: Optional[Match[str]] = re.search(r'(negat.([)]))( )(\w+)(:)(\w+)', phrase)
    padrao2: Optional[Match[str]] = re.findall(r'(negat.([)]))( )(\w+)(:)(\w+)', phrase)
    print('padrao 2 => lista ', padrao2)
    datetime_format = '%H:%M'
    oma = str
    for x in range(0, len(cont)):
        ###print('padrao2 group => ',padrao2[x][3:6])
        #print('padrao2 group => ',padrao2[1][3:6])
        #print('padrao2 group => ',padrao2.group(4,5,6))
        ##print('padrao1 => ',padrao1)
        #banconegativo = padrao1.group(4)+padrao1.group(5)+padrao1.group(6)
        #banconegativo = padrao2[x][3]+padrao2[x][4]+padrao2[x][5]+padrao2[x][6]
        banconegativo = padrao2[x][3]+padrao2[x][4]+padrao2[x][5]
        print('banconegativo =>', banconegativo)
        ###print('tipo banconegativo => ', type(banconegativo))
        convertestrtoint = datetime.strptime(banconegativo, '%H:%M').time()
        ###print("tipo convertstrtoint => ", type(convertestrtoint))
        print('banco negativo em horas convertstrtoint => ', convertestrtoint)

        somabanconegativo = datetime.strptime(banconegativo, datetime_format)
        ###somabanconegativo = banconegativo + somabanconegativo
        print('soma ', somabanconegativo)
        continue

buscainformacoesnaimagem()

from datetime import timedelta
from typing import Optional, Match

import datedelta as datedelta


def convertepdfparaimagem():

    from pdf2image import convert_from_path

    pages = convert_from_path('Ponto14102019.pdf', 300)
    pdf_file = 'Ponto14102019.pdf'[:-4]
    cont = 1
    for page in pages:
        page.save(f"{pdf_file}{cont}.jpg", "JPEG")
        cont = cont + 1
    print('\nImagens criadas com sucesso')
    print(pages)


def buscainformacoesnaimagem():


    import re
    import pytesseract as ocr
    from PIL import Image
    from datetime import datetime

    phrase = ocr.image_to_string(Image.open('Ponto141020191.jpg'), lang='por')
    #print(phrase)
    # FUNCIONOU padrao1 = re.search(r'(021)( - )(\w+)( )(\w+)( )(\w+)( )([(])(\w+)', phrase)
    cont = re.findall(r'(021)', phrase)
    print(len(cont))

    print('cont => ', cont)
    padrao1: Optional[Match[str]] = re.search(r'(negat.([)]))( )(\w+)(:)(\w+)', phrase)
    padrao2: Optional[Match[str]] = re.findall(r'(negat.([)]))( )(\w+)(:)(\w+)', phrase)
    print('padrao 2 => lista ', padrao2)
    datetime_format = '%H:%M'
    oma = str
    for x in range(0, len(cont)):
        ###print('padrao2 group => ',padrao2[x][3:6])
        #print('padrao2 group => ',padrao2[1][3:6])
        #print('padrao2 group => ',padrao2.group(4,5,6))
        ##print('padrao1 => ',padrao1)
        #banconegativo = padrao1.group(4)+padrao1.group(5)+padrao1.group(6)
        #banconegativo = padrao2[x][3]+padrao2[x][4]+padrao2[x][5]+padrao2[x][6]
        banconegativo = padrao2[x][3]+padrao2[x][4]+padrao2[x][5]
        print('banconegativo =>', banconegativo)
        ###print('tipo banconegativo => ', type(banconegativo))
        convertestrtoint = datetime.strptime(banconegativo, '%H:%M').time()
        ###print("tipo convertstrtoint => ", type(convertestrtoint))
        print('banco negativo em horas convertstrtoint => ', convertestrtoint)

        somabanconegativo = datetime.strptime(banconegativo, datetime_format)
        ###somabanconegativo = banconegativo + somabanconegativo
        print('soma ', somabanconegativo)
        continue

buscainformacoesnaimagem()




#
#reader = PyPDF2.PdfFileReader('Ponto141020191.pdf', 'rb')
#p = reader.getPage(0)
#text = p.extractText()
#print (text)


#pdf_file = open('Ponto14102019.pdf', 'rb')
#pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#pag = pdf_reader.getPage(0)

#tesseract d:\GIT_PYCHARM\Ponto141020191.jpg -l ara -psm 3 d:\GIT_PYCHARM\test_ara pdf

def __init__(self, dia, mes, ano):
    self.dia = dia
    self.mes = mes
    self.ano = ano
    self.listareferencia = []
    self.referencia = 0
    self.datapag = 'CERTIDÕES PARA {}/{}/{}'.format(self.dia, self.mes, self.ano)
    self.empresas = []
    #self.pdf_dir = '//hrg-74977/GEOF/CERTIDÕES/Certidões/'

def confere_data():
    import re
    import time

    texto = []
    padrao = re.compile('(\d\d)/(\d\d)/(\d\d\d\d)')
    padrao1 = re.findall(r'\w+S', '(\d\d)/(\d\d)/(\d\d\d\d)')
    emissao_string = padrao.search('Ponto141020191.pdf')
    #texto.append(emissao_string.split()[2])
    #emissao = texto[0]
    #data_de_emissao = time.strptime(emissao, "%d/%m/%Y")
    #payday = f'{self.dia}/{self.mes}/{self.ano}'
    #data_do_pagamento = time.strptime(payday, "%d/%m/%Y")
    #return data_do_pagamento >= data_de_emissao and data_do_pagamento <= data_de_vencimento
    print(padrao)
    print(padrao1)
    #print(emissao)
    #print(data_de_emissao)
    #print(payday)
    #print(data_do_pagamento)





/*/*/*/*//*/+
import re
from typing import Any, Tuple, Union

import pytesseract as ocr
from PIL import Image
from pdf2image import convert_from_path

class Ponto():
    def __init__(self, arquivo, nome):
        self.horasNeg = []
        self.horasExc = []
        self.arquivo = f'{arquivo}'
        self.imagemFolha1 = ''
        self.imagemFolha2 = ''
        self.nome = nome
        self.horastotais = 0
        self.minutostotais = 0
    def convertepdfparaimagem(self):
        pages = convert_from_path(self.arquivo+'.pdf', 300)
        cont = 1
        for page in pages:
            self.imagemFolha1 = f'{self.arquivo}-{cont}-{self.nome}'
            page.save(f"{self.imagemFolha1}.jpg", "JPEG")
            cont = cont + 1
        print('\nImagem criada com sucesso')


    def buscainformacoesnaimagem(self):

        for i in range(1, 4):
            phrase = ocr.image_to_string(Image.open(f'{self.arquivo}-{i}-{self.nome}.jpg'), lang='por')
            cont = re.findall(r'(021)', phrase)
            #print(phrase)
            cont2 = re.findall(r'(011)', phrase)
            print(f'lista do cont = {cont}')
            print(f'quantidade da lista de cont  = {len(cont)}')

            #padrao1 = re.findall(r'(negat\.[)])( )(\w+)(:)(\w+)', phrase)
            padrao1 = re.findall(r'(\w.+)', phrase)
            #padrao1 = re.findall(r'\w.+', phrase)
            print(f'lista do padrao {padrao1}')
            print(f'quantidade da lista do padrao {len(padrao1)}')
            if padrao1 != None:
                for x in range(0, len(cont)):
                    print(f'Primeiro elemnto = {x}')
                    #banconegativo = padrao1[x][2]+padrao1[x][3]+padrao1[x][4]
                    banconegativo = padrao1[x][2] # 0]+padrao1[x][1]+padrao1[x][2]
                    self.horasNeg.append(banconegativo)
                    #continue
                print(f'horas negativas = {self.horasNeg}')

    '''            padrao2 = re.findall(r'(zadas)( )(\w+)(:)(\w+)', phrase)
            print(padrao2)
            if padrao2 != None:
                for x in range(0, len(cont2)):
                    bancopositivo = padrao2[x][2]+padrao2[x][3]+padrao2[x][4]
                    self.horasExc.append(bancopositivo)
                    #continue
                print(f'horas positivas = {self.horasExc}')
    '''

    def calcular_horas(self, saldoH, saldoM):

        horasex = []
        horasneg = []

        for i in self.horasExc:
            eita = i.split(':')
            horasex.append(eita)

        for b in self.horasNeg:
            eita = b.split(':')
            horasneg.append(eita)

        hpos = 0
        hneg = 0
        mpos = 0
        mneg = 0

        for x in range(0, len(self.horasExc)-1):
            hpos += int(horasex[x][0])
            mpos += int(horasex[x][1])

        for x in range(0, len(self.horasNeg)-1):
            hneg -= int(horasneg[x][0])
            mneg -= int(horasneg[x][1])

        #print(f'TOTAL DE HORAS POSITIVAS: {hpos}')
        #print(f'TOTAL DE MINUTOS POSITIVOS: {mpos}')
        #print(f'TOTAL DE HORAS NEGATIVAS: {hneg}')
        #print(f'TOTAL DE MINUTOS NEGATIVOS: {mneg}')

        HORAS_TOTAIS = hpos + hneg + saldoH
        #print(f'HORAS: {HORAS_TOTAIS}')

        MINUTOS_TOTAIS = mpos + mneg + saldoM
        #print(f'MINUTOS TOTAIS: {MINUTOS_TOTAIS}')
        hor = divmod(MINUTOS_TOTAIS, 60)

        #print(f'{hor}\n')
        HORAS_TOTAIS += hor[0]
        a = '=-'*10
        print(f'{a}\n{self.nome}\n{a}\nHoras: {HORAS_TOTAIS}\nMin: {hor[1]}\n')

/*/*/*/*///*/*+
