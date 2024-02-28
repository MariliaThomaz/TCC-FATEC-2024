#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import fitz  # PyMuPDF
import re
import requests
from IPython.display import Markdown
def extrair_texto_e_imagens(pdf_url):
    # Baixar o PDF temporariamente desativando a verificação SSL
    response = requests.get(pdf_url, verify=False)
    with open("temp_pdf.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)

    pdf_document = fitz.open("temp_pdf.pdf")
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': contem_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

# Substitua o URL do PDF pelo caminho local ou URL do seu PDF
pdf_url = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"
resultados = extrair_texto_e_imagens(pdf_url)

# Exibindo os resultados
for resultado in resultados:
   # print(f"Página {resultado['numero_pagina']}:")
    Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>")
   # print(f"Texto:\n{resultado['texto']}\n")


# In[4]:


import fitz  # PyMuPDF
import re
import requests
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_url):
    # Baixar o PDF temporariamente desativando a verificação SSL
    response = requests.get(pdf_url, verify=False)
    with open("temp_pdf.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)

    pdf_document = fitz.open("temp_pdf.pdf")
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': contem_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

# Substitua o URL do PDF pelo caminho local ou URL do seu PDF
pdf_url = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"
resultados = extrair_texto_e_imagens(pdf_url)

# Exibindo os resultados
for resultado in resultados:
    display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>"))


# In[ ]:


import fitz  # PyMuPDF
import re
import requests
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_url):
    # Baixar o PDF temporariamente desativando a verificação SSL
    response = requests.get(pdf_url, verify=False)
    with open("temp_pdf.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)

    pdf_document = fitz.open("temp_pdf.pdf")
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': contem_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

# Substitua o URL do PDF pelo caminho local ou URL do seu PDF
pdf_url = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"
resultados = extrair_texto_e_imagens(pdf_url)

# Exibindo os resultados
for resultado in resultados:
    
    print(f"Texto da Página {resultado['numero_pagina']}:\n{resultado['texto']}\n")
    display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>"))


# In[2]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': contem_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo os resultados
for resultado in resultados:
    print(f"{resultado['texto']}")
    display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>"))


# ## Masca  para  faz  tratameto nas  autenativa  letras  repetidas

# In[3]:


import re
texto = texto_questoes
def aplicar_mascara_alternativas(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    return texto_formatado

# Exemplo de uso:
texto_entrada = texto_questoes


texto_formatado = aplicar_mascara_alternativas(texto_entrada)


print("\nTexto formatado:")
print(texto_formatado)


# In[4]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Aplicar máscara às alternativas no texto
        texto_pagina_formatado = aplicar_mascara_alternativas(texto_pagina)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina_formatado,  # Usar o texto formatado
            'contem_imagens': contem_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def aplicar_mascara_alternativas(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    return texto_formatado

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo os resultados
for resultado in resultados:
    print(f"{resultado['texto']}")
    display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>"))


# In[5]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Aplicar máscara às alternativas e identificar questões
        texto_pagina_formatado, questoes = aplicar_mascaras_e_identificar_questoes(texto_pagina)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina_formatado,  # Usar o texto formatado
            'contem_imagens': contem_imagens,
            'questoes': questoes  # Lista de questões identificadas
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def aplicar_mascaras_e_identificar_questoes(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    # Encontrar padrões que representam o início e o fim de cada questão
    padrao_questao = re.compile(r'(\d{1,2}\. [^\d]+)')
    questoes = padrao_questao.findall(texto_formatado)

    return texto_formatado, questoes

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo os resultados
for resultado in resultados:
    print(f"Página {resultado['numero_pagina']}:")
    print(f"{resultado['texto']}\n")
    display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>"))
    print(f"Questões Identificadas: {resultado['questoes']}\n")


# In[6]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        
        # Identificar questões com imagens
        questoes_com_imagens = identificar_questoes_com_imagens(texto_pagina)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': len(questoes_com_imagens) > 0,
            'questoes_com_imagens': questoes_com_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def identificar_questoes_com_imagens(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    # Encontrar padrões que representam o início de cada questão
    padrao_questao = re.compile(r'(\d{1,2}\. [^\d]+)')

    # Encontrar todas as questões com imagens
    questoes_com_imagens = []
    for match in padrao_questao.finditer(texto_formatado):
        inicio_questao = match.group(1)
        # Verificar se há imagens na questão
        if re.search(r'XObject:\s+Image', texto_formatado[match.end():]):
            questoes_com_imagens.append(inicio_questao)

    return questoes_com_imagens

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo os resultados
for resultado in resultados:
    print(f"Página {resultado['numero_pagina']}:")
    print(f"{resultado['texto']}\n")
    display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>"))
    print(f"Questões com Imagens: {resultado['questoes_com_imagens']}\n")


# In[7]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        
        # Identificar questões com imagens
        questoes_com_imagens = identificar_questoes_com_imagens(texto_pagina)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': len(questoes_com_imagens) > 0,
            'questoes_com_imagens': questoes_com_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def identificar_questoes_com_imagens(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    # Encontrar padrões que representam o início de cada questão
    padrao_questao = re.compile(r'(\d{1,2}\. [^\d]+)')

    # Encontrar todas as questões com imagens
    questoes_com_imagens = []
    for match in padrao_questao.finditer(texto_formatado):
        inicio_questao = match.group(1)
        # Verificar se há imagens na questão
        if re.search(r'XObject:\s+Image', texto_formatado[match.end():]):
            questoes_com_imagens.append(inicio_questao)

    return questoes_com_imagens

def exibir_questoes_com_imagens(resultados):
    for resultado in resultados:
        for questao_com_imagem in resultado['questoes_com_imagens']:
            display(Markdown(f"**Página {resultado['numero_pagina']}, Questão {questao_com_imagem}**\n{resultado['texto']}"))
            display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>\n"))

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo as questões com imagens
exibir_questoes_com_imagens(resultados)


# In[8]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        
        # Identificar questões com imagens
        questoes_com_imagens = identificar_questoes_com_imagens(texto_pagina)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': len(questoes_com_imagens) > 0,
            'questoes_com_imagens': questoes_com_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def identificar_questoes_com_imagens(texto):
    # Encontrar padrões que representam o início de cada questão
    padrao_questao = re.compile(r'(\d{1,2}\. [^\d]+)')

    # Encontrar todas as questões com imagens
    questoes_com_imagens = []
    for match in padrao_questao.finditer(texto):
        inicio_questao = match.group(1)
        # Verificar se há imagens na questão
        if re.search(r'XObject:\s+Image', texto[match.end():]):
            questoes_com_imagens.append(inicio_questao)

    return questoes_com_imagens

def exibir_questoes_com_imagens(resultados):
    for resultado in resultados:
        for questao_com_imagem in resultado['questoes_com_imagens']:
            display(Markdown(f"**Página {resultado['numero_pagina']}, Questão {questao_com_imagem}**\n{resultado['texto']}"))
            display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>\n"))

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo as questões com imagens
exibir_questoes_com_imagens(resultados)


# In[9]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        
        # Identificar questões com imagens
        questoes_com_imagens = identificar_questoes_com_imagens(texto_pagina, imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': len(questoes_com_imagens) > 0,
            'questoes_com_imagens': questoes_com_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def identificar_questoes_com_imagens(texto, imagens):
    # Encontrar padrões que representam o início de cada questão
    padrao_questao = re.compile(r'(\d{1,2}\. [^\d]+)')

    # Encontrar todas as questões com imagens
    questoes_com_imagens = []
    for match in padrao_questao.finditer(texto):
        inicio_questao = match.group(1)
        
        # Verificar se há imagens na questão
        fim_questao = texto.find('\n', match.end())
        imagens_na_questao = any(imagem[0] >= match.start() and imagem[0] <= fim_questao for imagem in imagens)
        
        if imagens_na_questao:
            questoes_com_imagens.append(inicio_questao)

    return questoes_com_imagens

def exibir_questoes_com_imagens(resultados):
    for resultado in resultados:
        for questao_com_imagem in resultado['questoes_com_imagens']:
            display(Markdown(f"**Página {resultado['numero_pagina']}, Questão {questao_com_imagem}**\n{resultado['texto']}"))
            display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>\n"))

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo as questões com imagens
exibir_questoes_com_imagens(resultados)


# In[10]:


import fitz  # PyMuPDF
import re
from IPython.display import display, Markdown

def extrair_texto_e_imagens(pdf_path):
    pdf_document = fitz.open(pdf_path)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]

        # Extrair o texto da página
        texto_pagina = pagina.get_text()

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        
        # Identificar questões com imagens
        questoes_com_imagens = identificar_questoes_com_imagens(texto_pagina, imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto': texto_pagina,
            'contem_imagens': len(questoes_com_imagens) > 0,
            'questoes_com_imagens': questoes_com_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def identificar_questoes_com_imagens(texto, imagens):
    # Encontrar padrões que representam o início de cada questão
    padrao_questao = re.compile(r'(\d{1,2}\. [^\d]+)')

    # Encontrar todas as questões com imagens
    questoes_com_imagens = []
    for match in padrao_questao.finditer(texto):
        inicio_questao = match.group(1)
        
        # Verificar se há imagens associadas à questão
        imagens_na_questao = any(imagem[0] >= match.start() and imagem[0] <= match.end() for imagem in imagens)
        
        if imagens_na_questao:
            questoes_com_imagens.append(inicio_questao)

    return questoes_com_imagens

def exibir_questoes_com_imagens(resultados):
    for resultado in resultados:
        for questao_com_imagem in resultado['questoes_com_imagens']:
            display(Markdown(f"**Página {resultado['numero_pagina']}, Questão {questao_com_imagem}**\n{resultado['texto']}"))
            display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>\n"))

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo as questões com imagens
exibir_questoes_com_imagens(resultados)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




