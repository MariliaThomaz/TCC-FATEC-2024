import fitz  # PyMuPDF

# Função para verificar a presença de imagens nas questões
def verificar_imagens_no_pdf(caminho_pdf):
    # Inicializar o leitor de PDF
    pdf_reader = fitz.open(caminho_pdf)

    for pagina_num in range(pdf_reader.page_count):
        # Extrair informações da página
        pagina = pdf_reader[pagina_num]

        # Verificar se a página possui imagens
        imagens = pagina.get_images(full=True)
        
        if imagens:
            print(f"Status da imagem na página {pagina_num + 1}: Contém imagem")
        else:
            print(f"Status da imagem na página {pagina_num + 1}: Não contém imagem")

    # Fechar o leitor de PDF
    pdf_reader.close()

# Caminho completo do PDF
caminho_pdf = r"C:\Program Files\Tesseract-OCR\CODAR TCC\enm_2019.pdf"

# Chamar a função para verificar imagens no PDF
verificar_imagens_no_pdf(caminho_pdf)
