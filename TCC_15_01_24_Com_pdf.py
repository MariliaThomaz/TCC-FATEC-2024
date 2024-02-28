#!/usr/bin/env python
# coding: utf-8

# In[6]:



import PyPDF2
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
    print(f"Total de páginas no PDF: {total_paginas}")

    # Extrair texto de todas as páginas
    texto_questoes = ""
    for pagina_num in range(total_paginas):
        pagina = pdf_reader.pages[pagina_num]
        texto_pagina = pagina.extract_text()
        print(f"Texto da página {pagina_num + 1}:\n{texto_pagina}")
        texto_questoes += texto_pagina

    return texto_questoes

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Números das QUESTÕES desejadas
questao_inicio = 136
questao_fim = 180

# Extrair QUESTÕES do PDF
texto_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)

# Exibir o texto das QUESTÕES
#print(f"Texto final das QUESTÕES:\n{texto_questoes}")

# Texto de entrada
texto = texto_questoes
import re

def organizar_questoes(texto):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃO \d+.*?(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Dividir o texto em parágrafos
        paragrafos = questao.strip().split('\n\n')

        # Processar cada parágrafo
        for j, paragrafo in enumerate(paragrafos, start=1):
            # Remover espaços extras no conteúdo do parágrafo
            paragrafo_limpo = re.sub(r'\s+', ' ', paragrafo.strip())
            
            # Exibir o conteúdo do parágrafo sem espaços extras
            print(f"  Parágrafo {j}: {paragrafo_limpo}")

# Chamar a função para organizar e identificar as QUESTÕES
organizar_questoes(texto_questoes)


# In[7]:


import PyPDF2
import requests
from io import BytesIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re

# Desativar os avisos de solicitação insegura
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def extrair_questoes(url, inicio, fim):
    # Fazer o download do PDF
    response = requests.get(url, verify=False)  # Desativa a verificação SSL
    pdf_file = BytesIO(response.content)

    # Inicializar o leitor de PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extrair texto de todas as páginas
    texto_questoes = ""
    for pagina_num in range(pdf_reader.numPages):
        pagina = pdf_reader.getPage(pagina_num)
        texto_pagina = pagina.extractText()
        texto_questoes += texto_pagina

    return texto_questoes

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Números das QUESTÕES desejadas
questao_inicio = 136
questao_fim = 180

# Extrair QUESTÕES do PDF
texto_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)

# Exibir o texto das QUESTÕES
#print(f"Texto final das QUESTÕES:\n{texto_questoes}")

# Texto de entrada
texto = texto_questoes

def organizar_questoes(texto):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃO \d+.*?(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Dividir o texto em parágrafos
        paragrafos = questao.strip().split('\n\n')

        # Processar cada parágrafo
        for j, paragrafo in enumerate(paragrafos, start=1):
            # Remover espaços extras no conteúdo do parágrafo
            paragrafo_limpo = re.sub(r'\s+', ' ', paragrafo.strip())
            
            # Exibir o conteúdo do parágrafo sem espaços extras
            print(f"  Parágrafo {j}: {paragrafo_limpo}")

# Chamar a função para organizar e identificar as QUESTÕES
organizar_questoes(texto_questoes)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




