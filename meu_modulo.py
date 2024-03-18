# meu_modulo.py

import fitz  # PyMuPDF
import re

def extrair_dados_perguntas_alternativas_com_imagens(caminho_pdf):
    pdf_document = fitz.open(caminho_pdf)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]
        texto_pagina = pagina.get_text()

        # Procurar padrões de perguntas e alternativas
        padrao_pergunta = re.compile(r'\b(Q\d{1,3}\. .+?)\b', re.DOTALL)
        padrao_alternativas = re.compile(r'\b([ABCDE]\. .+?)\b', re.DOTALL)

        perguntas = padrao_pergunta.findall(texto_pagina)
        alternativas = padrao_alternativas.findall(texto_pagina)

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'texto_pagina': texto_pagina,
            'perguntas': perguntas,
            'alternativas': alternativas,
            'contem_imagens': contem_imagens
        }

        # Adicionar informações à lista
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()

    return informacoes_pdf

def limpar_duplicatas(resultados):
    resultados_limpos = []

    for resultado in resultados:
        perguntas_unicas = []
        alternativas_unicas = set()  # Usar um conjunto para garantir unicidade

        for pergunta, alternativa in zip(resultado['perguntas'], resultado['alternativas']):
            if alternativa not in alternativas_unicas:
                perguntas_unicas.append(pergunta)
                alternativas_unicas.add(alternativa)

        resultado_limpo = {
            'numero_pagina': resultado['numero_pagina'],
            'texto_pagina': resultado['texto_pagina'],
            'perguntas': perguntas_unicas,
            'alternativas': list(alternativas_unicas),  # Converter conjunto de volta para lista
            'contem_imagens': resultado['contem_imagens']
        }

        resultados_limpos.append(resultado_limpo)

    return resultados_limpos

def extrair_dados_perguntas_alternativas_com_imagens(caminho_pdf):
    pdf_document = fitz.open(caminho_pdf)
    informacoes_pdf = []

    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]
        texto_pagina = pagina.get_text()

        # Procurar padrões de perguntas e alternativas
        padrao_pergunta = re.compile(r'\b(Q\d{1,3}\. .+?)\b', re.DOTALL)
        padrao_alternativas = re.compile(r'\b([ABCDE]\. .+?)\b', re.DOTALL)

        perguntas = padrao_pergunta.findall(texto_pagina)
        alternativas = padrao_alternativas.findall(texto_pagina)

        # Verificar se a página contém imagens
        imagens = pagina.get_images(full=True)
        contem_imagens = any(isinstance(imagem[2], (str, bytes)) and re.search(rb'XObject:\s+Image', imagem[2]) for imagem in imagens)

        # Armazenar informações sobre a página
        informacoes_pagina = {
            'numero_pagina': pagina_num + 1,
            'perguntas_alternativas': []  # Usar uma lista para armazenar perguntas e alternativas
        }

        for pergunta in perguntas:
            alternativas_unica = set()  # Usar um conjunto para garantir unicidade
            for alternativa in alternativas:
                if alternativa.startswith(pergunta):
                    # Máscara para tratar alternativas repetidas A, B, C, D, E
                    alternativa_mascarada = alternativa[:2]
                    alternativas_unica.add(alternativa_mascarada)

            informacoes_pergunta = {
                'pergunta': pergunta,
                'alternativas': list(alternativas_unica),
            }
            informacoes_pagina['perguntas_alternativas'].append(informacoes_pergunta)

        informacoes_pagina['contem_imagens'] = contem_imagens
        informacoes_pdf.append(informacoes_pagina)

    pdf_document.close()
    return informacoes_pdf