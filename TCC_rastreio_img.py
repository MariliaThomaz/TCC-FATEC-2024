import re
import os
import requests
from PyPDF2 import PdfReader
from io import BytesIO
from PIL import Image
import fitz
import pytesseract
import cv2
import numpy as np
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Definir a função has_content
def has_content(imagem):
    return imagem.width > 0 and imagem.height > 0

# Função para organizar o texto
def organizar_texto(texto):
    # Substituir múltiplos espaços por apenas um espaço
    texto_formatado = re.sub(r'\s+', ' ', texto)

    # Remover espaços antes e depois de quebras de linha
    texto_formatado = re.sub(r'\s*\n\s*', '\n', texto_formatado)

    # Substituir espaços antes e depois de pontuações
    texto_formatado = re.sub(r'\s*([.,;?!])\s*', r'\1 ', texto_formatado)

    return texto_formatado.strip()

# Função para remover alternativas duplicadas
def remover_duplicatas(alternativas):
    # Separar as alternativas
    alternativas_separadas = alternativas.split()

    # Remover duplicatas
    alternativas_sem_duplicatas = list(set(alternativas_separadas))

    # Ordenar as alternativas novamente
    alternativas_sem_duplicatas.sort()

    # Juntar as alternativas em uma única string
    return ' '.join(alternativas_sem_duplicatas)

# Função para verificar a presença de imagens nas questões
def verificar_imagem_na_questao(texto_questao, imagem_stream):
    # Verificar se o texto ou a imagem indicam a presença de imagem
    if "contém imagem" in texto_questao.lower():
        return "Contém imagem (indicado no texto)"
    
    # Converter a imagem para um array numpy usando OpenCV
    try:
        imagem_np = cv2.imdecode(np.frombuffer(imagem_stream.getvalue(), dtype=np.uint8), 1)
    except Exception as e:
        print(f"Erro ao decodificar a imagem: {e}")
        return "Não contém imagem (erro na decodificação)"

    # Verificar se a imagem é válida
    if imagem_np is not None:
        # Converter a imagem para tons de cinza
        imagem_cinza = cv2.cvtColor(imagem_np, cv2.COLOR_BGR2GRAY)

        # Aplicar uma limiarização para binarizar a imagem
        _, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

        # Calcular a porcentagem de pixels brancos (representando conteúdo significativo)
        porcentagem_pixels_brancos = (cv2.countNonZero(imagem_binaria) / imagem_binaria.size) * 100

        print(f"Porcentagem de pixels brancos: {porcentagem_pixels_brancos}%")

        # Determinar se a imagem contém conteúdo significativo com base na porcentagem
        if porcentagem_pixels_brancos > 1:
            return "Contém imagem"
        else:
            return "Não contém imagem (poucos pixels brancos)"
    else:
        return "Não contém imagem (imagem não é válida)"


# Função para extrair texto e imagem de uma página do PDF
# Alteração na função extrair_texto_e_imagem
def extrair_texto_e_imagem(pagina):
    # Extrair texto da página
    texto_pagina = pagina.extract_text()

    # Inicializar a imagem como None (nenhuma imagem)
    imagem_stream = None
    texto_imagem = None

    # Tentar extrair informações da imagem da página
    try:
        # Verificar se a página possui uma imagem antes de tentar obter o pixmap
        if pagina.get_images():
            imagem_ref = pagina.get_pixmap()
            imagem_stream = BytesIO(imagem_ref.get_bits())
            imagem_pil = Image.open(imagem_stream)

            # Extrair texto da imagem usando pytesseract
            texto_imagem = pytesseract.image_to_string(imagem_pil, lang='por')

    except Exception as e:
        print(f"Erro ao extrair imagem: {e}")

    return texto_pagina, imagem_stream, texto_imagem





# Função para aplicar a máscara nas alternativas
def aplicar_mascara_alternativas(texto):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    texto_formatado = re.sub(r'([A-E])\s*\1', r'\1', texto)

    return texto_formatado

# Função para aplicar a máscara nas questões
def aplicar_mascara_questoes(texto, inicio, fim):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'(QUESTÃO \d+.*?)(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Filtrar as questões no intervalo desejado
    questoes_no_intervalo = [questao for questao in questoes_encontradas if inicio <= int(re.search(r'QUESTÃO (\d+)', questao).group(1)) <= fim]

    # Juntar as questões no intervalo em uma única string
    texto_formatado = '\n\n'.join(questoes_no_intervalo)

    return texto_formatado

# Função para extrair questões
# Função para extrair questões
def extrair_questoes(url, inicio, fim):
    # Fazer o download do PDF
    response = requests.get(url, verify=False)
    pdf_file = BytesIO(response.content)

    # Inicializar o leitor de PDF
    pdf_reader = PdfReader(pdf_file)

    # Extrair texto e informações sobre imagens
    info_imagens_questoes = []

    for pagina_num, pagina in enumerate(pdf_reader.pages, start=1):
        # Extrair texto da página
        texto_pagina, imagem_stream, texto_imagem = extrair_texto_e_imagem(pagina)

        # Aplicar a máscara nas alternativas
        texto_pagina = aplicar_mascara_alternativas(texto_pagina)

        # Aplicar a máscara nas questões
        texto_pagina = aplicar_mascara_questoes(texto_pagina, inicio, fim)

        # Organizar o texto
        texto_organizado = organizar_texto(texto_pagina)

        # Remover alternativas duplicadas
        alternativas_sem_duplicatas = remover_duplicatas(texto_organizado)

        # Verificar se a questão contém imagem
        status_imagem = verificar_imagem_na_questao(texto_organizado, imagem_stream)

        print(f"Status da imagem na página {pagina_num}: {status_imagem}")

        if status_imagem == "Contém imagem":
            info_imagens_questoes.append({'pagina': pagina_num, 'imagem': imagem_stream, 'status': 'Contém imagem'})
        else:
            info_imagens_questoes.append({'pagina': pagina_num, 'imagem': None, 'status': 'Não contém imagem'})

    return info_imagens_questoes



# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Definir os números de início e fim das questões
questao_inicio = 136
questao_fim = 180

# Executar a função
info_imagens_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)
