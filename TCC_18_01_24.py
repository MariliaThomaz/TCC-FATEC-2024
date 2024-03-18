#!/usr/bin/env python
# coding: utf-8

import re
import requests
from io import BytesIO
import fitz  # PyMuPDF

# Desativar os avisos de solicitação insegura
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def extrair_questoes(pdf_bytes, inicio, fim):
    # Inicializar o leitor de PDF
    pdf_document = fitz.open("pdf", pdf_bytes)

    # Verificar o número total de páginas no PDF
    total_paginas = pdf_document.page_count
    #print(f"Total de páginas no PDF: {total_paginas}")

    # Extrair texto de todas as páginas
    texto_questoes = ""
    for pagina_num in range(total_paginas):
        pagina = pdf_document[pagina_num]
        texto_pagina = pagina.get_text()
        #print(f"Texto da página {pagina_num + 1}:\n{texto_pagina}")
        texto_questoes += texto_pagina

    pdf_document.close()

    return texto_questoes

# Função para aplicar máscara nas alternativas
def aplicar_mascara_alternativas(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)
    return texto_formatado

# Função para aplicar máscara nas questões
def aplicar_mascara_questoes(texto, inicio, fim):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'(Unidade \d+.*?)(?=Unidade \d+|$)', texto, re.DOTALL)

    # Filtrar as questões no intervalo desejado
    questoes_no_intervalo = [questao for questao in questoes_encontradas if inicio <= int(re.search(r'QUESTÃO (\d+)', questao).group(1)) <= fim]

    # Juntar as questões no intervalo em uma única string
    texto_formatado = '\n\n'.join(questoes_no_intervalo)

    return texto_formatado

# Função para organizar e identificar as QUESTÕES
def organizar_questoes(texto):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃo \d+.*?(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Remover espaços extras no conteúdo da QUESTÃO
        questao_limpa = re.sub(r'\s+', ' ', questao.strip())

        # Exibir o conteúdo da QUESTÃO sem espaços extras
        print(questao_limpa)

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Definir os números de início e fim das questões
questao_inicio = 136
questao_fim = 180

# Fazer o download do PDF
response = requests.get(url_pdf, verify=False)  # Desativa a verificação SSL
pdf_bytes = BytesIO(response.content)

# Chamar a função para extrair as QUESTÕES
texto_questoes = extrair_questoes(pdf_bytes, questao_inicio, questao_fim)

# Exibir o texto das QUESTÕES
print(f"Texto final das QUESTÕES:\n{texto_questoes}")

# Máscara para poder pegar dados no intervalo de 136 até 180
texto_formatado = aplicar_mascara_questoes(texto_questoes, 136, 180)

print("\nTexto após aplicar máscara de questões:")
print(texto_formatado)

# Aplicar máscara para tratamento nas alternativas com letras repetidas
texto_formatado_alternativas = aplicar_mascara_alternativas(texto_formatado)

print("\nTexto formatado com máscara de alternativas:")
print(texto_formatado_alternativas)

# Exemplo de uso:
texto_entrada = texto_formatado_alternativas
texto_questoes = aplicar_mascara_questoes(texto_entrada, 136, 180)

print("\nTexto formatado final:")
print(texto_questoes)

# Chamar a função para organizar e identificar as QUESTÕES
organizar_questoes(texto_questoes)
