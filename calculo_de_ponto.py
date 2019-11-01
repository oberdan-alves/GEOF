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

    phrase = ocr.image_to_string(Image.open('Ponto141020191.jpg'), lang='por')
    #print(phrase)

    #texto = []
    #padrao = re.findall(r'\d{2}/\d{2}/\d{4}', phrase)
    #padrao1 = re.findall(r'021 - Atraso a Compensar (BH ', phrase)
    padrao1 = re.search(r'(021)( - )(\w+)( )(\w+)( )(\w+)([(])(\w+)', phrase)
    #padrao1 = re.findall(r'\w+S', '(\d\d)/(\d\d)/(\d\d\d\d)')
    #emissao_string = padrao.search('Ponto141020191.pdf')
    #print(padrao)
    print(padrao1)
    #print(padrao1)

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


