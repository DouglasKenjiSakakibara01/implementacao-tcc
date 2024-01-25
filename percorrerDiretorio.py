import os

def percorre_diretorio(diretorio, nome):
    
    for raiz, dir, arquivos in os.walk(diretorio):
        for arq in arquivos:
            if arq.startswith(nome) and arq.endswith("programa.py"):
                caminho_programa = os.path.join(raiz, arq)
    for raiz, dir, arquivos in os.walk(diretorio):
        for arq in arquivos:
            if arq.startswith(nome) and arq.endswith("teste.py"):
                caminho_teste = os.path.join(raiz, arq)            

    return caminho_programa, caminho_teste



if __name__ == '__main__':
    
    diretorio = '/home/dks01/implementacao-tcc/src'
    caminho_programa, caminho_teste = percorre_diretorio(diretorio, 'aluno')

    print(caminho_programa)
    print(caminho_teste)
    