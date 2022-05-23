with open('links.txt', 'r', encoding="utf8") as arquivo:
    url = [linha.strip() for linha in arquivo]
    print(url)
    '''
    for linha in arquivo:
        print(linha, end=(''))'''
