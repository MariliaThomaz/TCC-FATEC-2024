import fitz  # Using PyMuPDF
from PIL import Image
import pytesseract

def extract_images_and_text(pdf_path):
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]

        images = page.get_images(full=True)  # Get images with metadata

        # Handle the case where there are no images on the page
        if not images:
            print(f"Página {page_number + 1} não contém imagens.")
            continue

        for img_index, img_matrix in enumerate(images):
            # Ensure img_matrix is iterable before unpacking
            if not isinstance(img_matrix, (list, tuple)):
                print(f"Página {page_number + 1}, imagem {img_index + 1}: Formato de imagem não suportado.")
                continue

            try:
                img_width, img_height = img_matrix[0]  # Access width and height
                img = Image.frombytes("RGB", [img_width, img_height], img_matrix.samples)

                # Perform OCR
                text = pytesseract.image_to_string(img)

                # Process text and image (your custom logic goes here)
                print(f"Imagem {img_index + 1}: {text}")

                # Optionally save the image to disk
                img.save(f"imagem_{img_index + 1}.png")

            except Exception as e:
                print(f"Erro ao processar imagem {img_index + 1}: {e}")

    pdf_document.close()

if __name__ == "__main__":
    pdf_path = r'C:\Users\Marilia\Desktop\CODAR TCC\enm_2019.pdf'  # Replace with your path
    extract_images_and_text(pdf_path)
