# Projeto de Machine Learning para identificação de Retinopatia Diabética
#
# Para realização do projeto, algumas  bibliotecas foram utilizadas, como:
#       Matplotlib(para criação de janelas gráficas)
#       Pandas(para trabalho otimizado com diversos dados)
#       cv2(para leitura de ficheitos em CSV)
#       Numpy(para otimização do processamento de muitos dados)
#
# Foram estudadas 3.662 imagens de retinas

import matplotlib.pyplot as plt
import pandas as pd
import cv2
import numpy as np

train = pd.read_csv('aula_train_set.csv')

# histograma
# >> Criar imagem
# >> Escolher grafico
# >> Guardar a imagem

fig = plt.figure(figsize=(10, 5))
plt.hist(train['diagnosis'], facecolor='black')
plt.title('Distribuição de Classes')
plt.ylabel('Unidades de Observação/ Casos')
plt.xticks([0, 1, 2, 3, 4])

plt.xlabel('Diagnóstico')

txt = f'''0 - SEM DR
1 - INICIAL
2 - MODERADA
3 - SEVERA
4 - PROLIFERATIVA
---
N = {len(train)}'''

plt.text(3, 1250, txt)
plt.savefig('Figure_1')

# Fim da análise dos dados para ver se estão todos certos em relação a classificação das RD
# Análise das imagens a nivel de qualidade e tamanho

image_stats = []
train = pd.read_csv('aula_trabalho/aula_train_set.csv')  # Nome dos ficheiros com imagens e dados adicionais

# analise imagem a imagem
for index, observation in train.iterrows():
    print(index, observation)

    # importar fotos
    img = cv2.imread(f'aula_trabalho/ulht_biomedic_images/{observation["id_code"]}.png')

    height, width, channels = img.shape
    ratio = width / height

    # print(height, width, channels, ratio, observation["diagnosis"]) # Linha utilizada para correção de alguns bugs e obervação dos dados

    # Salvar e estruturar grafico das imagens
    image_stats.append(np.array((observation['diagnosis'], height, width, channels, ratio)))

# construir DF
image_stats = pd.DataFrame(image_stats)
image_stats.columns = ['Diagnosis', 'Height', 'Width', 'Channels', 'Ratio']

# Criar Gráfico
fig = plt.figure(figsize=(15, 5))

#    Para janela grafica só foi utilizado a largura, altura e razão das imagens, por isso (1, 3, x),
#    se o diagnostico fosse necessario nesse grafico
#    seria utilizado (1, 4, x), onde x é a posição do sub-grafico

# # Diagnosis
# plt.subplot(1, 4, 1)
# plt.hist(image_stats['Diagnosis'], facecolor='k', edgecolor='w')
# plt.title('(a) Diagnóstico das Imagens')
# plt.ylabel('Número de Imagens')
# plt.xlabel('Diagnosticos')

# Width
plt.subplot(1, 3, 1)
plt.hist(image_stats['Width'], facecolor='k', edgecolor='w')
plt.title('(a) Largura das Imagens')
plt.ylabel('Número de Imagens')
plt.xlabel('Largura')

# Height
plt.subplot(1, 3, 2)
plt.hist(image_stats['Height'], facecolor='k', edgecolor='w')
plt.title('(b) Altura das Imagens')
plt.ylabel('Número de Imagens')
plt.xlabel('Altura')

# Ratio
plt.subplot(1, 3, 3)
plt.hist(image_stats['Ratio'], facecolor='k', edgecolor='w')
plt.title('(c) Razão das Imagens')
plt.ylabel('Número de Imagens')
plt.xlabel('Razão')

plt.savefig('Figure_2')