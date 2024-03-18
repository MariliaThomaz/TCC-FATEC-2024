import PyPDF2
import re
import requests
from io import BytesIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Desativar os avisos de solicitação insegura
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def extrair_questoes(url, inicio, fim):
    # Fazer o download do PDF
    response = requests.get(url, verify=False)  # Desativa a verificação SSL
    pdf_file = BytesIO(response.content)

    # Inicializar o leitor de PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Verificar o número total de páginas no PDF
    total_paginas = len(pdf_reader.pages)
   
    # Extrair texto de todas as páginas
    texto_questoes = ""
    for pagina_num in range(total_paginas):
        pagina = pdf_reader.pages[pagina_num]
        texto_pagina = pagina.extract_text()
        texto_questoes += texto_pagina

    return texto_questoes

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Definir os números de início e fim das questões
questao_inicio = 136
questao_fim = 180

# Extrair QUESTÕES do PDF
texto_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)


# Extrair QUESTÕES do PDF
texto_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)

# Texto de entrada
texto = texto_questoes

''' 
Masca para faz tratameto nas autenativa letras repetidas
'''
def aplicar_mascara_alternativas(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    return texto_formatado

# Exemplo de uso:
texto_entrada = texto_questoes


texto_formatado = aplicar_mascara_alternativas(texto_entrada)

'''
## Função para  agrupor  o  texto
'''
texto = texto_formatado 

def aplicar_mascara_questoes(texto, inicio, fim):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'(QUESTÃO \d+.*?)(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Filtrar as questões no intervalo desejado
    questoes_no_intervalo = [questao for questao in questoes_encontradas if inicio <= int(re.search(r'QUESTÃO (\d+)', questao).group(1)) <= fim]

    # Juntar as questões no intervalo em uma única string
    texto_formatado = '\n\n'.join(questoes_no_intervalo)

    return texto_formatado

# Exemplo de uso:
texto_entrada = texto_formatado


texto_formatado = aplicar_mascara_questoes(texto_entrada, 136, 180)

'''
## Masca  para  poder  pegar  dados  intevalod  136 até 180
'''

texto_questoes = texto_formatado

def organizar_questoes(texto):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃO \d+.*?(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Remover espaços extras no conteúdo da QUESTÃO
        questao_limpa = re.sub(r'\s+', ' ', questao.strip())
        
        # Exibir o conteúdo da QUESTÃO sem espaços extras
        print(questao_limpa)

# Chamar a função para organizar e identificar as QUESTÕES
organizar_questoes(texto_questoes) 
