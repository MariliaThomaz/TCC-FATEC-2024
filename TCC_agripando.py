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

        # Aplicar a máscara nas alternativas
        texto_pagina = aplicar_mascara_alternativas(texto_pagina)

        # Aplicar a máscara nas questões
        texto_pagina = aplicar_mascara_questoes(texto_pagina, 136, 180)

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
            texto_imagem = pytesseract.image_to_string(imagem_pil, lang='por')  # Use o OCR do Tesseract para extrair texto da imagem
            print(f"Texto da imagem na página {pagina_num + 1}: {texto_imagem}")

            # Organizar o texto
            texto_organizado = organizar_texto(texto_pagina)
            print(f"Texto organizado na página {pagina_num + 1}: {texto_organizado}")

            # Remover alternativas duplicadas
            alternativas_sem_duplicatas = remover_duplicatas(texto_organizado)
            print(f"Alternativas sem duplicatas na página {pagina_num + 1}: {alternativas_sem_duplicatas}")

        # Exibir o texto da página
        print(f"Texto da página {pagina_num + 1}: {texto_pagina}")

    return info_imagens_questoes

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Definir os números de início e fim das questões
questao_inicio = 136
questao_fim = 180

# Executar a função
info_imagens_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)