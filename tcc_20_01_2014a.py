
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

def exibir_resultados(resultados):
    for resultado in resultados:
        print(f"Texto da Página {resultado['numero_pagina']}:\n{resultado['texto']}\n")
        display(Markdown(f"<font color='red'>Contém imagens: {resultado['contem_imagens']}</font>\n"))

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2020_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo os resultados
exibir_resultados(resultados)





def aplicar_mascara_alternativas(resultados):
    # Encontrar todas as alternativas duplicadas e substituir por uma única letra
    for resultado in resultados:
        resultado['texto'] = re.sub(r'([A-E])\s*\1', r'\1', resultado['texto'])

    return resultados


resultados = extrair_texto_e_imagens(pdf_path)

# Aplicar a máscara de alternativas
resultados_formatados = aplicar_mascara_alternativas(resultados)

# Exibindo os resultados formatados
exibir_resultados(resultados_formatados)





from IPython.display import display, Markdown

def exibir_questoes_com_imagens(resultados):
    for resultado in resultados:
        if resultado['contem_imagens']:
            print(f"Texto da Questão:\n{resultado['texto']}\n")
            display(Markdown(f"<font color='red'>Contém imagens: Sim</font>\n"))

# Substitua o caminho do PDF pelo caminho local do seu PDF
pdf_path = r'C:\Users\Marilia\Desktop\Fatec\TCC\2023_PV_impresso_D2_CD5.pdf'
resultados = extrair_texto_e_imagens(pdf_path)

# Exibindo apenas o texto das questões que contêm imagens
exibir_questoes_com_imagens(resultados)



