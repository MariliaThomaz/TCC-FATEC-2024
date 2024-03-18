from wand.image import Image

def verificar_imagens_no_pdf(caminho_pdf):
    try:
        # Inicializar a lista de páginas com imagens
        paginas_com_imagens = []

        # Abrir o PDF usando a biblioteca Wand
        with Image(filename=caminho_pdf) as pdf:
            for pagina_num, pdf_page in enumerate(pdf.sequence):
                # Converter a página PDF em uma imagem
                imagem_pagina = Image(pdf_page)

                # Verificar se a imagem da página não está em branco
                if imagem_pagina.alpha_channel or imagem_pagina.mean_color_intensity > 0:
                    paginas_com_imagens.append(pagina_num + 1)

        if paginas_com_imagens:
            print(f"O PDF possui imagens nas páginas: {paginas_com_imagens}")
        else:
            print("O PDF não possui imagens.")

    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

# Caminho completo do PDF
caminho_pdf = r"C:\Program Files\Tesseract-OCR\CODAR TCC\enm_2019.pdf"

# Chamar a função para verificar imagens no PDF
verificar_imagens_no_pdf(caminho_pdf)
