from meu_modulo import extrair_dados_perguntas_alternativas_com_imagens, limpar_duplicatas

# Substitua o caminho do PDF pelo caminho local do seu PDF
caminho_pdf_local_2023 = r"C:\Users\Marilia\Desktop\CODAR TCC\2023_PV_impresso_D2_CD5.pdf"
caminho_pdf_local_2021 = r"C:\Users\Marilia\Desktop\CODAR TCC\2021_PV_impresso_D2_CD5.pdf"

# Extraindo dados e exibindo resultados para 2023
resultados_2023 = extrair_dados_perguntas_alternativas_com_imagens(caminho_pdf_local_2023)
for resultado in resultados_2023:
    print(f"Página {resultado['numero_pagina']}:")
    
    # Exibindo o texto da página
    print(f'texto_pagina.{texto_pagina}')
    
    # Exibindo perguntas e alternativas
    for pergunta_alternativa in resultado['perguntas_alternativas']:
        print(f"Pergunta: {pergunta_alternativa['pergunta']}")
        print(f"Alternativas: {', '.join(pergunta_alternativa['alternativas'])}\n")
    
    print(f"Contém imagens: {resultado['contem_imagens']}\n")

# Extraindo dados e exibindo resultados para 2021 com limpeza de duplicatas
resultados_2021 = extrair_dados_perguntas_alternativas_com_imagens(caminho_pdf_local_2021)
resultados_limpos_2021 = limpar_duplicatas(resultados_2021)
for resultado in resultados_limpos_2021:
    print(f"Página {resultado['numero_pagina']}:")
    
    for pergunta_alternativa in resultado['perguntas_alternativas']:
        print(f"Pergunta: {pergunta_alternativa['pergunta']}")
        print(f"Alternativas: {', '.join(pergunta_alternativa['alternativas'])}\n")
    
    print(f"Contém imagens: {resultado['contem_imagens']}")
    print()
