import PyPDF2
import requests
from io import BytesIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re

def extrair_texto_pdf(url):
    try:
        # Fazer o download do PDF com verificação SSL
        response = requests.get(url, verify=True)

        # Verificar se a solicitação foi bem-sucedida
        response.raise_for_status()

        # Criar um arquivo BytesIO para o conteúdo do PDF
        pdf_file = BytesIO(response.content)

        # Inicializar o leitor de PDF
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Extrair texto de todas as páginas
        texto_completo = ""
        for pagina_num in range(pdf_reader.numPages):
            pagina = pdf_reader.getPage(pagina_num)
            texto_pagina = pagina.extractText()
            texto_completo += texto_pagina

        return texto_completo

    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação: {e}")
        return None
    except PyPDF2.utils.PdfReadError as e:
        print(f"Erro ao ler PDF: {e}")
        return None

def organizar_questoes(texto):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃO \d+.*?(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Dividir o texto em parágrafos
        paragrafos = questao.strip().split('\n\n')

        # Processar cada parágrafo
        for j, paragrafo in enumerate(paragrafos, start=1):
            # Remover espaços extras no conteúdo do parágrafo
            paragrafo_limpo = re.sub(r'\s+', ' ', paragrafo.strip())

            # Exibir o conteúdo do parágrafo sem espaços extras
            print(f"  Parágrafo {j}: {paragrafo_limpo}")

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Extrair texto do PDF
texto_questoes = extrair_texto_pdf(url_pdf)

# Verificar se a extração foi bem-sucedida antes de continuar
if texto_questoes:
    # Chamar a função para organizar e identificar as QUESTÕES
    organizar_questoes(texto_questoes)
else:
    print("Falha na extração do texto do PDF.")
