import fitz
import cv2
import numpy as np
import os

def compare_images(image_path1, image_data2):
    # Carregar a imagem do arquivo
    image1 = cv2.imread(image_path1)
    
    # Decodificar os dados da imagem do PDF
    if isinstance(image_data2, int):
        print(f"Aviso: Imagem é um objeto 'int'.")
        return False

    try:
        image_data2 = np.frombuffer(image_data2, dtype=np.uint8)
        image2 = cv2.imdecode(image_data2, cv2.IMREAD_COLOR)
    except Exception as e:
        print(f"Erro ao decodificar imagem do PDF: {e}")
        return False

    # Verificar a similaridade usando o método de comparação de histograma
    hist1 = cv2.calcHist([image1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([image2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    
    # Definir um limiar de similaridade (ajuste conforme necessário)
    threshold = 0.8
    
    return similarity > threshold

def analyze_pdf_images(pdf_path, image_folder):
    pdf_document = fitz.open(pdf_path)

    imagens_banco_dados = ['g1.JPG', 'g2.JPG', 'g3.JPG', 'g4.JPG', 'g5.JPG', 'g6.JPG', 'g7.JPG', 'g9.JPG',
                           'g10.JPG', 'g11.JPG', 'g12.JPG', 'g13.JPG', 'i1.JPG', 'i2.JPG', 'i3.JPG', 'i4.JPG',
                           'i5.JPG', 'i6.JPG', 'i7.JPG', 'i8.JPG', 'i9.JPG', 'i10.JPG', 'i11.JPG', 'i12.JPG',
                           'i13.JPG', 'i14.JPG', 'i15.JPG', 'i16.JPG', 'i17.JPG', 'i18.JPG', 'i19.JPG', 'i20.JPG',
                           'i21.JPG', 'i22.JPG', 'i23.JPG', 'i24.JPG', 'i25.JPG', 'i26.JPG', 'i27.JPG', 'i28.JPG']

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        images_on_page = page.get_images(full=True)

        for img_index, img_info in enumerate(images_on_page):
            if not isinstance(img_info[0], fitz.Pixmap):
                print(f"Aviso: Imagem na página {page_number + 1}, Questão {img_index + 1} não possui 'get_data()'. Tipo: {type(img_info[0])}")
                continue

            try:
                base_image = img_info[0].get_data()
            except AttributeError as ae:
                print(f"Aviso: Imagem na página {page_number + 1}, Questão {img_index + 1} não possui 'get_data()'. Detalhes: {ae}")
                continue

            found_match = False
            for filename in os.listdir(image_folder):
                image_path = os.path.join(image_folder, filename)

                if compare_images(image_path, base_image):
                    found_match = True
                    if filename in imagens_banco_dados:
                        print(f"Encontrou imagem {filename} na página {page_number + 1}, Questão {img_index + 1} (Banco de Dados)")
                    else:
                        print(f"Encontrou imagem {filename} na página {page_number + 1}, Questão {img_index + 1}")

            if not found_match:
                print(f"Não encontrou correspondência para imagem na página {page_number + 1}, Questão {img_index + 1}")

    pdf_document.close()
# Exemplo de uso
pdf_path = r"C:\Users\Marilia\Desktop\CODAR TCC\enm_2019.pdf"
image_folder = r"C:\Users\Marilia\Desktop\CODAR TCC\img"
analyze_pdf_images(pdf_path, image_folder)
