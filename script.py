import os
import subprocess
import coverage
import json


def executar_testes(diretorio, arquivo_teste):
    caminho_arquivo = os.path.join(diretorio, arquivo_teste)

    if os.path.exists(caminho_arquivo):
        comando = ['coverage', 'run', '-m', 'pytest', caminho_arquivo]
        subprocess.run(comando)
        
        saida_pytest = subprocess.run(comando, capture_output=True, text=True)
        testes_passados = saida_pytest.stdout.count("passed")
        testes_falhados = saida_pytest.stdout.count("failed")
        print(testes_falhados)
        print(testes_passados)
        

        subprocess.run(['coverage', 'json', '-o', 'resultado.json'])

        with open('resultado.json', 'r') as file:
            resultado_json = json.load(file)
        print(resultado_json)
    else:
        print(f'O arquivo de teste {caminho_arquivo} não foi encontrado.')
'''
def executar_testes(diretorio, arquivo_teste):
    caminho_arquivo = os.path.join(diretorio, arquivo_teste)

    if os.path.exists(caminho_arquivo):
        comando=['pytest','--json-report', caminho_arquivo]
        subprocess.run(comando)
        print(comando)
         # Lê o relatório JSON gerado pelo pytest-json
        with open('.report.json', 'r') as file:
            resultados_json = json.load(file)

        
        print(resultados_json)
    
    else:
        print(f'O arquivo de teste {caminho_arquivo} não foi encontrado.')        
'''
if __name__ == '__main__':
    diretorio = '/home/dks01/implementacaoTcc/src'
    arquivo_teste = 'testeCoverageParidade.py'

    executar_testes(diretorio, arquivo_teste)
    