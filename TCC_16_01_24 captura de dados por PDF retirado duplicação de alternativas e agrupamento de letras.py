#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2

def extrair_questoes(caminho_pdf, inicio, fim):
    # Inicializar o leitor de PDF
    with open(caminho_pdf, 'rb') as pdf_file:
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

# Caminho local do PDF
caminho_pdf = r'C:\Users\Marilia\Desktop\Fatec\TCC\2019_PV_impresso_D2_CD6.pdf'

# Números das QUESTÕES desejadas
questao_inicio = 136
questao_fim = 180

# Extrair QUESTÕES do PDF local
texto_questoes = extrair_questoes(caminho_pdf, questao_inicio, questao_fim)

# Exibir o texto das QUESTÕES
print(f"Texto final das QUESTÕES:\n{texto_questoes}")

# Texto de entrada
texto = texto_questoes


# In[ ]:





# In[ ]:


import re

def aplicar_mascara_alternativas(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    return texto_formatado

# Exemplo de uso:
texto_entrada = texto_questoes


texto_formatado = aplicar_mascara_alternativas(texto_entrada)

print("Texto original:")
#print(texto_entrada)

print("\nTexto formatado:")
print(texto_formatado)


# In[ ]:


texto1 = texto_formatado


# In[4]:


def organizar_questoes(texto):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃO \d+.*?(?=QUESTÃO \d+|$)', texto1, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Remover espaços extras no conteúdo da QUESTÃO
        questao_limpa = re.sub(r'\s+', ' ', questao.strip())
        
        # Exibir o conteúdo da QUESTÃO sem espaços extras
        print(questao_limpa)

organizar_questoes(texto_questoes)


# In[ ]:


texto_questoes


# In[ ]:


def organizar_questoes(texto1):
    # Lista para armazenar as QUESTÕES limpas
    questoes_limpas = []

    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃO \d+.*?(?=QUESTÃO \d+|$)', texto1, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Remover espaços extras no conteúdo da QUESTÃO
        questao_limpa = re.sub(r'\s+', ' ', questao.strip())

        # Adicionar a QUESTÃO limpa à lista
        questoes_limpas.append(questao_limpa)

        # Exibir o conteúdo da QUESTÃO sem espaços extras
        print(questao_limpa)

    return questoes_limpas

# Chamar a função para organizar e identificar as QUESTÕES
questoes_limpas = organizar_questoes(texto_questoes)
print(texto_questoes)


# In[ ]:


import re

def aplicar_mascara_questoes(texto2, inicio, fim):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'(QUESTÃO \d+.*?)(?=QUESTÃO \d+|$)', texto2, re.DOTALL)

    # Filtrar as questões no intervalo desejado
    questoes_no_intervalo = [questao for questao in questoes_encontradas if inicio <= int(re.search(r'QUESTÃO (\d+)', questao).group(1)) <= fim]

    # Juntar as questões no intervalo em uma única string
    texto_formatado = '\n\n'.join(questoes_no_intervalo)

    return texto_formatado

# Exemplo de uso:
texto_entrada = 


texto_formatado = aplicar_mascara_questoes(texto_entrada, 136, 180)

print("Texto original:")
#print(texto_entrada)

print("\nTexto formatado:")
print(texto_formatado)


# In[ ]:




