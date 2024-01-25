import os
import subprocess
import coverage
import json

def executar_testes(caminho_programa,caminho_teste):
    if os.path.exists(caminho_programa and caminho_teste):
        comando = ['coverage', 'run', '-m', 'pytest', caminho_programa, caminho_teste ]
        subprocess.run(comando)
        
        saida_pytest = subprocess.run(comando, capture_output=True, text=True)
        
        testes_total = saida_pytest.stdout.count("collected")
        testes_passados = saida_pytest.stdout.count("passed")
        testes_falhados = saida_pytest.stdout.count("failed")
        print(testes_falhados)
        print(testes_passados)
        
        # gera o relatorio do coverage no formato json
        subprocess.run(['coverage', 'json', '-o', 'resultado.json'])

        with open('resultado.json', 'r') as file:
            resultado_json = json.load(file)
            porcentagem_cobertura = resultado_json['totals']['percent_covered']
        print("Porcentagem de cobertura:"+ str(porcentagem_cobertura))
    
        
        # gera o relatorio de cobertura
        subprocess.run(['coverage', 'report', '-m'])

        return testes_total, testes_passados, testes_falhados, porcentagem_cobertura

    else:
        print(f'O arquivo do programa/teste não foi encontrado.')
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
    '''
    diretorio = '/home/dks01/implementacao-tcc/src'
    arquivo_programa = 'aluno01_programa.py'
    arquivo_teste = 'aluno01_teste.py'
    '''
    diretorio = '/home/dks01/implementacao-tcc/src'
    caminho_programa, caminho_teste = percorre_diretorio(diretorio, 'aluno')
    executar_testes(caminho_programa, caminho_teste)
    