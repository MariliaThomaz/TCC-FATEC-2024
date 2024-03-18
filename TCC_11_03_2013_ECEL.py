import os
from PIL import Image

# Caminho da pasta
pasta_imagens = r"C:\Users\Marilia\Desktop\CODAR TCC\foto"

# Percorrer os arquivos da pasta
for numero_imagem in range(1, 31):
  # Criar o nome do arquivo
  arquivo_imagem = f"imagem{numero_imagem:02d}.jpg"

  # Verificar se o arquivo existe
  if not os.path.isfile(os.path.join(pasta_imagens, arquivo_imagem)):
    continue

  # Abrir a imagem
  imagem = Image.open(os.path.join(pasta_imagens, arquivo_imagem))

  # Verificar se a imagem possui características de gravura
  # (Adicione suas regras de análise aqui)

  # Se for uma gravura, imprimir a questão
  if ...:
    print(f"Questão {numero_imagem}: Contém gravuras.")
  else:
    print(f"Questão {numero_imagem}: Não contém gravuras.")
