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
