import re
import requests
from io import BytesIO
from pdf2image import convert_from_bytes
import pytesseract
import os

# Caminho absoluto completo para o diretório tessdata
tessdata_dir = 'C:\\Program Files\\Tesseract-OCR\\tessdata'

# Obtém o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo ao diretório do script
tessdata_dir_relative = os.path.join(script_dir, 'tessdata').replace("\\", "/")

os.environ['TESSDATA_PREFIX'] = tessdata_dir

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Desativar os avisos de solicitação insegura
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def main():
    # Restante do código...

 if __name__ == "__main__":
    main()
