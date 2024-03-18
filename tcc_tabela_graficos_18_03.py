import PyPDF2
import re
import requests
from io import BytesIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Desativar os avisos de solicitação insegura
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Função para extrair questões do PDF
def extrair_questoes(url, inicio, fim):
    # Fazer o download do PDF
    response = requests.get(url, verify=False)  # Desativa a verificação SSL
    pdf_file = BytesIO(response.content)

    # Inicializar o leitor de PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Verificar o número total de páginas no PDF
    total_paginas = len(pdf_reader.pages)
   
    # Extrair texto de todas as páginas
    texto_questoes = ""
    for pagina_num in range(total_paginas):
        pagina = pdf_reader.pages[pagina_num]
        texto_pagina = pagina.extract_text()
        texto_questoes += texto_pagina

    return texto_questoes

# URL do PDF
url_pdf = "https://download.inep.gov.br/enem/provas_e_gabaritos/2023_PV_impresso_D2_CD5.pdf"

# Definir os números de início e fim das questões
questao_inicio = 136
questao_fim = 180

# Extrair QUESTÕES do PDF
texto_questoes = extrair_questoes(url_pdf, questao_inicio, questao_fim)

# Função para organizar e analisar as questões
def organizar_questoes(texto):
    # Usar regex para encontrar todas as QUESTÕES no texto
    questoes_encontradas = re.findall(r'(QUESTÃO \d+.*?)(?=QUESTÃO \d+|$)', texto, re.DOTALL)

    # Processar cada QUESTÃO
    for i, questao in enumerate(questoes_encontradas, start=1):
   # Exibir número da QUESTÃO
        print(f"\nQUESTÃO {i}")

        # Remover espaços extras no conteúdo da QUESTÃO
        questao_limpa = re.sub(r'\s+', ' ', questao.strip())

        # Analisar elementos visuais na QUESTÃO
        imagens = re.findall(r'\[IMAGEM:(.*?)\]', questao_limpa, re.DOTALL)
        tabelas = re.findall(r'\[TABELA:(.*?)\]', questao_limpa, re.DOTALL)
        graficos = re.findall(r'\[GRAFICO:(.*?)\]', questao_limpa, re.DOTALL)

        # Exibir informações sobre imagens
        if imagens:
            print("Esta questão contém imagens:")
            for imagem in imagens:
                print(f"Imagem: {imagem}")

        # Exibir informações sobre tabelas
        if tabelas:
            print("Esta questão contém tabelas:")
            for tabela in tabelas:
                print(f"Tabela: {tabela}")

        # Exibir informações sobre gráficos
        if graficos:
            print("Esta questão contém gráficos:")
            for grafico in graficos:
                print(f"Gráfico: {grafico}")

# Chamar a função para organizar e analisar as QUESTÕES
organizar_questoes(texto_questoes)