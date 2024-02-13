import os
import subprocess
import coverage
import json
import re
import math

def merge_arquivos(caminho_programa, caminho_teste, caminho):
    with open(caminho_programa, 'r') as arquivo_programa:
        programa = arquivo_programa.read()

    with open(caminho_teste, 'r') as arquivo_teste:
        teste = arquivo_teste.read()

    conteudo_final = programa + "\n" + teste
    caminho+='/arquivo_teste.py'
    with open(caminho, 'w') as arquivo_final:
        arquivo_final.write(conteudo_final)
    return caminho    

def executar_testes(caminho_programa,caminho_teste, caminho):
    if os.path.exists(caminho_programa and caminho_teste and caminho):
        '''
        comando = ['coverage', 'run', '-m', 'pytest', caminho_programa, caminho_teste ]
        subprocess.run(comando)
        saida_pytest = subprocess.run(comando, capture_output=True, text=True)
        testes_total = saida_pytest.stdout.count("collected")
        testes_passados = saida_pytest.stdout.count("passed")
        testes_falhados = saida_pytest.stdout.count("failed")
        '''

        # executa os testes usando o pytest e gera o relatório JSON
        arquivo_teste= merge_arquivos(caminho_programa, caminho_teste, caminho)
        resultados={}
        #comando = ['pytest', '--json=reportPytest.json', caminho_programa, arquivo_teste]
        comando = ['pytest', '--json=reportPytest.json', arquivo_teste]
        subprocess.run(comando)

        # leitura do relatório JSON gerado pelo pytest
        with open('reportPytest.json', 'r') as file:
            resultados_json = json.load(file)
            testes_total =resultados_json['report']['summary']['num_tests']
            testes_passados = resultados_json['report']['summary']['passed']
            testes_falhados=0
            if testes_total!= testes_passados:
                testes_falhados = resultados_json['report']['summary']['failed']
            

        # gera o relatorio do coverage no formato json  
        subprocess.run(['coverage', 'run','-m', 'pytest', f'{arquivo_teste}']) 
        subprocess.run(['coverage', 'json','-o', 'resultadoCoverage.json'])             
        
        with open('resultadoCoverage.json', 'r') as file:
            resultados_json = json.load(file)
            
            #porcentagem_cobertura = resultados_json['totals']['percent_covered']
            porcentagem_cobertura = resultados_json['files'][f'{arquivo_teste}']['summary']['percent_covered']


        
        # gera o relatorio de cobertura
        subprocess.run(['coverage', 'report', f'{arquivo_teste}'])

        resultados['total']= testes_total
        resultados['passados']= testes_passados
        resultados['falhados']= testes_falhados
        resultados['cobertura']= round(porcentagem_cobertura, 0)
        print(resultados)
        return resultados 

    else:
        print(f'O arquivo do programa/teste não foi encontrado.')
def percorre_diretorio(diretorio_programa,diretorio_teste, nome_programa, nome_teste):
    caminho_programa=''
    caminho_teste=''
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
def metrica_correcao_testes(diretorio_programa, diretorio_teste, caminho):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'professor', 'aluno')
    resultados = executar_testes(caminho_programa, caminho_teste, caminho)
    retorno= resultados['passados']/resultados['total']
    return round(retorno,2)
    
# executa o programa de referencia do professor com os testes do aluno(mede a cobertura do codigo(coverage))
def metrica_completude_testes(diretorio_programa, diretorio_teste, caminho):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'professor', 'aluno')
    resultados = executar_testes(caminho_programa, caminho_teste, caminho)
    retorno = round((resultados['cobertura']/100),2)
    return retorno
    
# executa os testes do professor com o programa do aluno(taxa de sucesso * cobertura do codigo)
def metrica_correcao_programa(diretorio_programa, diretorio_teste, caminho):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'aluno', 'professor')
    resultados = executar_testes(caminho_programa, caminho_teste, caminho)
    retorno = (resultados['passados']/resultados['total']) * (resultados['cobertura']/100)
    return round(retorno,2)
    
# executa o programa e os testes do aluno( mede a taxa de sucesso(total_passados/total_testes))
def metrica_efetividade_testes(diretorio_programa, diretorio_teste, caminho):
    caminho_programa, caminho_teste = percorre_diretorio(diretorio_programa, diretorio_teste, 'aluno', 'aluno')
    resultados = executar_testes(caminho_programa, caminho_teste, caminho)
    retorno = resultados['passados']/resultados['total']
    return round(retorno, 2)
    
if __name__ == '__main__':
    
    
    diretorio_programa = 'src/turma01/professor'
    diretorio_teste = 'src/turma01/aluno08'
    caminho= 'src/turma01/aluno08'
    saida_metrica = metrica_correcao_testes(diretorio_programa, diretorio_teste, caminho)
    print('*-*-*-*-**-Metrica*-*-*-*-*-*-*-**-*-**-')
    print(saida_metrica)
    