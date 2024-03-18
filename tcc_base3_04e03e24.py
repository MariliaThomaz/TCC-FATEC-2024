import re
import os
import requests
from PyPDF2 import PdfReader
from io import BytesIO
from PIL import Image
import fitz
import pytesseract

# Definir a função has_content
def has_content(imagem):
    return imagem.width > 0 and imagem.height > 0

# Definir a função extrair_questoes aqui
def extrair_questoes(url, inicio, fim):
    # Seu código para extrair questões vai aqui
    pass

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Fazer o download do PDF
response = requests.get(url_pdf, verify=False)
pdf_file = BytesIO(response.content)

# Inicializar o leitor de PDF
pdf_reader = PdfReader(pdf_file)

# Definir os números de início e fim das questões
questao_inicio = 136
questao_fim = 180

# Extrair QUESTÕES do PDF
info_imagens_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)

def extrair_questoes(url, inicio, fim):
    # Fazer o download do PDF
    response = requests.get(url, verify=False)
    pdf_file = BytesIO(response.content)

    # Inicializar o leitor de PDF
    pdf_reader = PdfReader(pdf_file)
    total_paginas = len(pdf_reader.pages)

    # Extrair texto e informações sobre imagens
    info_imagens_questoes = []
    for pagina_num in range(total_paginas):
        # Extrair texto da página
        texto_pagina = pdf_reader.pages[pagina_num].extract_text()

        # Inicializar o documento PyMuPDF
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

        # Certificar-se de que a página é válida antes de acessá-la
        if pagina_num < len(doc):
            pagina_atual = doc[pagina_num]
            imagem_ref = pagina_atual.get_pixmap()
            imagem_stream = BytesIO(imagem_ref.get_bits())
            imagem_pil = Image.open(imagem_stream)

            # Verificar se a imagem contém conteúdo significativo
            if has_content(imagem_pil):
                info_imagens_questoes.append({'pagina': pagina_num + 1, 'imagem': imagem_stream})

            # Extrair texto da imagem usando pytesseract
            texto_imagem = extract_text_from_image(imagem_pil)
            print(f"Texto da imagem na página {pagina_num + 1}: {texto_imagem}")

        # Exibir o texto da página
        print(f"Texto da página {pagina_num + 1}: {texto_pagina}")

    return info_imagens_questoes


# Executar a função
info_imagens_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)
