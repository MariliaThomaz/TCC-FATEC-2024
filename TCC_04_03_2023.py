#conda activate NewVirtualE

import PyPDF2
import requests
from io import BytesIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import fitz  # PyMuPDF
from IPython.display import Markdown, display

# Desativar os avisos de solicitação insegura
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def extrair_questoes(url, inicio, fim):
    # Fazer o download do PDF
    response = requests.get(url, verify=False)  # Desativa a verificação SSL
    pdf_file = BytesIO(response.content)

    # Inicializar o leitor de PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Verificar o número total de páginas no PDF
    total_paginas = len(pdf_reader.pages)
    print(f"Total de páginas no PDF: {total_paginas}")

    # Extrair texto de todas as páginas
    texto_questoes = ""
    for pagina_num in range(total_paginas):
        pagina = pdf_reader.pages[pagina_num]
        texto_pagina = pagina.extract_text()
        print(f"Texto da página {pagina_num + 1}:\n{texto_pagina}")
        texto_questoes += texto_pagina

    return texto_questoes


def organizar_questoes_com_imagens(texto, inicio, fim):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'QUESTÃO \d+.*?(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
        # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Remover espaços extras no conteúdo da QUESTÃO
        questao_limpa = re.sub(r'\s+', ' ', questao.strip())
        
        # Exibir o conteúdo da QUESTÃO sem espaços extras
        print(questao_limpa)

        # Verificar se a página contém imagens
        paginas_questao = fitz.Document("pdf", BytesIO(response.content))
        pagina_questao = paginas_questao[i - 1]

        imagens = pagina_questao.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Exibir mensagem indicando se contém imagens
        if contem_imagens:
            display(Markdown(f"<font color='red'>Contém imagens</font>"))
        else:
            display(Markdown("Não contém imagens"))


# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Definir os números de início e fim das questões
questao_inicio = 136
questao_fim = 180

# Extrair QUESTÕES do PDF
texto_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)

# Chamar a função para organizar, identificar e verificar imagens nas QUESTÕES
organizar_questoes_com_imagens(texto_questoes, questao_inicio, questao_fim)
