

import fitz
import requests  # Adicione esta linha para importar o módulo requests
from io import BytesIO
from PIL import Image
import pytesseract
import cv2
import numpy as np
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def verificar_imagem_na_questao(texto_questao, imagem_stream, threshold=1):
    if "contém imagem" in texto_questao.lower():
        return "Contém imagem (indicado no texto)"

    try:
        imagem_np = cv2.imdecode(np.frombuffer(imagem_stream.getvalue(), dtype=np.uint8), 1)
    except Exception as e:
        print(f"Erro ao decodificar a imagem: {e}")
        return "Não contém imagem (erro na decodificação)"

    if imagem_np is not None:
        imagem_cinza = cv2.cvtColor(imagem_np, cv2.COLOR_BGR2GRAY)
        _, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)
        porcentagem_pixels_brancos = (cv2.countNonZero(imagem_binaria) / imagem_binaria.size) * 100

        print(f"Porcentagem de pixels brancos: {porcentagem_pixels_brancos}%")

        if porcentagem_pixels_brancos > threshold:
            return "Contém imagem"
        else:
            return "Não contém imagem (poucos pixels brancos)"
    else:
        return "Não contém imagem (imagem não é válida)"

def extrair_texto_e_imagem(pagina):
    texto_pagina = pagina.get_text()
    imagem_stream = None

    try:
        if pagina.get_images():
            imagem_ref = pagina.get_pixmap()
            if hasattr(imagem_ref, 'get_bits'):
                imagem_stream = BytesIO(imagem_ref.get_bits())
                imagem_pil = Image.open(imagem_stream)
                texto_imagem = pytesseract.image_to_string(imagem_pil, lang='por')
                status_imagem = verificar_imagem_na_questao(texto_pagina, imagem_stream)

                if "Contém imagem" in status_imagem:
                    print(f"Status da imagem na página: {status_imagem}")
    except Exception as e:
        print(f"Erro ao extrair imagem: {e}")

    return texto_pagina, imagem_stream

def verificar_imagens_no_pdf(url, threshold=1):
    response = requests.get(url, verify=False)
    pdf_file = BytesIO(response.content)
    pdf_reader = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for pagina_num in range(pdf_reader.page_count):
        pagina = pdf_reader[pagina_num]
        texto_pagina, imagem_stream = extrair_texto_e_imagem(pagina)

    pdf_reader.close()

# Chamar a função com a URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"
verificar_imagens_no_pdf(url_pdf)
