import fitz
from PIL import Image
from PyPDF2 import PdfReader  # Substitua PdfFileReader por PdfReader
import pytesseract


def extract_images_and_text(pdf_path):
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        
        images = page.get_images(full=True)
        for img_index, img_info in enumerate(images):
            img_matrix = page.get_pixmap()  # Remove the 'image=img_info[0]' argument

            
            # Convertendo a matriz de imagem para uma imagem PIL
            img = Image.frombytes("RGB", [img_matrix.width, img_matrix.height], img_matrix.samples)
            
            # Reconhecimento de texto na imagem usando Tesseract OCR
            text = pytesseract.image_to_string(img)
            
            # Verificar se há palavras-chave relacionadas a figuras
            if 'figura' in text.lower():
                print(f"Gravura encontrada na página {page_number + 1}, imagem {img_index + 1}")

    pdf_document.close()

if __name__ == "__main__":
    # Substitua 'seu_arquivo.pdf' pelo caminho do seu PDF
    pdf_path = r'C:\Users\Marilia\Desktop\CODAR TCC\enm_2019.pdf'

    extract_images_and_text(pdf_path)

    import fitz  # Assuming you're using PyMuPDF

def extract_images_and_text(pdf_path):
  doc = fitz.open(pdf_path)
  for page in doc:
    images = page.get_images()  # List of image dictionaries
    text = page.get_text("text")  # Extract text

    # Process images and text based on your requirements

if __name__ == "__main__":
  pdf_path = "C:/Users/Marilia/Desktop/CODAR TCC/enm_2019.pdf"  # Replace with your path
  extract_images_and_text(pdf_path)
