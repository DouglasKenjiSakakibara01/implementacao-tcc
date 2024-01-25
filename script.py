import os
import subprocess
import coverage
import json
import re

def executar_testes(caminho_programa,caminho_teste):
    if os.path.exists(caminho_programa and caminho_teste):
        '''
        comando = ['coverage', 'run', '-m', 'pytest', caminho_programa, caminho_teste ]
        subprocess.run(comando)
        saida_pytest = subprocess.run(comando, capture_output=True, text=True)
        testes_total = saida_pytest.stdout.count("collected")
        testes_passados = saida_pytest.stdout.count("passed")
        testes_falhados = saida_pytest.stdout.count("failed")
        '''
        # executa os testes usando o pytest e gera o relatório JSON
        resultados={}
        comando = ['pytest', '--json=reportPytest.json', caminho_programa, caminho_teste]
        subprocess.run(comando)

        # leitura do relatório JSON gerado pelo pytest
        with open('reportPytest.json', 'r') as file:
            resultados_json = json.load(file)
            testes_total =resultados_json['report']['summary']['num_tests']
            testes_passados = resultados_json['report']['summary']['passed']
            testes_falhados = resultados_json['report']['summary']['failed']

        # gera o relatorio do coverage no formato json
        subprocess.run(['coverage', 'json', '-o', 'resultadoCoverage.json'])

        with open('resultadoCoverage.json', 'r') as file:
            resultado_json = json.load(file)
            porcentagem_cobertura = resultado_json['totals']['percent_covered']
        
        # gera o relatorio de cobertura
        subprocess.run(['coverage', 'report', '-m'])

        resultados['total']= testes_total
        resultados['passados']= testes_passados
        resultados['falhados']= testes_falhados
        resultados['cobertura']= round(porcentagem_cobertura, 2)
        #print(resultado)
        return resultados

    else:
        print(f'O arquivo do programa/teste não foi encontrado.')
def percorre_diretorio(diretorio_programa,diretorio_teste, nome_programa, nome_teste):
    
    for raiz, dir, arquivos in os.walk(diretorio_programa):
        for arq in arquivos:
            # percorre o diretorio e busca um arquivo comece com o nome passado como parametro e termina com programa.py
            if arq.startswith(nome_programa) and arq.endswith("programa.py"):
                caminho_programa = os.path.join(raiz, arq)
    for raiz, dir, arquivos in os.walk(diretorio_teste):
        for arq in arquivos:
            # percorre o diretorio e busca um arquivo comece com o nome passado como parametro e termina com teste.py
            if arq.startswith(nome_teste) and arq.endswith("teste.py"):
                caminho_teste = os.path.join(raiz, arq)            

    return caminho_programa, caminho_teste

# executa o programa de referencia do professor com os testes do aluno( mede a taxa de sucesso(total_passados/total_testes))
def metrica_correcao_testes(diretorio_programa, diretorio_teste):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'professor', 'aluno')
    resultados = executar_testes(caminho_programa, caminho_teste)
    retorno= resultados['total']/resultados['passados']
    return retorno
    
# executa o programa de referencia do professor com os testes do aluno(mede a cobertura do codigo(coverage))
def metrica_completude_testes(diretorio_programa, diretorio_teste):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'professor', 'aluno')
    resultados = executar_testes(caminho_programa, caminho_teste)
    retorno = resultados['cobertura']
    return retorno
    
# executa os testes do professor com o programa do aluno(taxa de sucesso * cobertura do codigo)
def metrica_correcao_programa(diretorio_programa, diretorio_teste):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'aluno', 'professor')
    resultados = executar_testes(caminho_programa, caminho_teste)
    retorno = (resultados['passados']/resultados['total']) * (resultados['cobertura']/100)
    return round(retorno,2)
    
# executa o programa e os testes do aluno( mede a taxa de sucesso(total_falhados/total_testes))
def metrica_efetividade_testes(diretorio_programa, diretorio_teste):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'aluno', 'aluno')
    resultados = executar_testes(caminho_programa, caminho_teste)
    retorno = resultados['falhados']/resultados['total']
    return round(retorno, 2)
    
if __name__ == '__main__':
    
    '''
    diretorio = '/home/dks01/implementacao-tcc/src'
    caminho_programa, caminho_teste = percorre_diretorio(diretorio, 'aluno')
    resultados = executar_testes(caminho_programa, caminho_teste)
    resultados = list(resultados)
    print(resultados)
    '''
    caminho_programa = '/home/dks01/implementacao-tcc/src/'
    caminho_teste = '/home/dks01/implementacao-tcc/src/'
    saida_metrica = metrica_efetividade_testes(caminho_programa, caminho_teste)
    print('*-*-*-*-**-Metrica*-*-*-*-*-*-*-**-*-**-')
    print(saida_metrica)