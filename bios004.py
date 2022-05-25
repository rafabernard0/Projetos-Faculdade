import csv
import statistics
import matplotlib.pyplot as plt

# 1 - Recolher o nome dos ficheiro e define uma variavel global
ficheiros = 'dados_hidratação_Rafael', 'dados_hidratação_Tiago', 'dados_hidratação_Gabriel', 'dados_hidratação_Joel'
dados_gerais_hidra, dados_gerais_oleo = {}, {}

# 2 - Tratar cada ficheiro e adicionar à variável global
for item in ficheiros:
    item += '.csv'

    data = open(item)

    linhas = csv.reader(data, delimiter=';')
    dados_HA, dados_HB, time = [], [], [0, 20, 40, 60, 80]
    dados_HA_c, dados_HB_c = [], []
    all_dados_hidra, all_dados_oleo = list(), list()
    # dados_HA = hidratação do braço A | dados_HB = hidratação do braço B (todos no 1º tempo)
    # dados_HA_T1 e dados_HB_T1 são os dados da hidratação no 2º tempo de medição

    dados_OA, dados_OB, dados_OA_c, dados_OB_c = [], [], [], []  # Referente a Oleosidade

    for i, linha in enumerate(linhas):

        if 1 < i < 7:
            el = linha[2].replace(',', '.')
            dados_HA.append(float(el))

            # O mesmo if funcionça porque estão na mesma posição

            el = linha[4].replace(',', '.')
            dados_HB.append(float(el))

        if 7 <= i < 13:
            el = linha[2].replace(',', '.')
            dados_HA_c.append(float(el))

            el = linha[4].replace(',', '.')
            dados_HB_c.append(float(el))

        # Calculos para a Oleosidade

        if 1 < i < 7:
            el = linha[3].replace(',', '.')
            dados_OA.append(float(el))

            # Para dos dados no braço B

            el = linha[5].replace(',', '.')
            dados_OB.append(float(el))

        if 7 <= i < 13:
            el = linha[3].replace(',', '.')
            dados_OA_c.append(float(el))

            el = linha[5].replace(',', '.')
            dados_OB_c.append(float(el))

    else:
        # Salva todos os dados puxados do ecxel nos lugares certos sem repetição. Para hidra antes e depois
        all_dados_hidra.append(dados_HA[:])
        all_dados_hidra.append(dados_HB[:])
        all_dados_hidra.append(dados_HA_c[:])
        all_dados_hidra.append(dados_HB_c[:])

        # Salva para a oleosidade

        all_dados_oleo.append(dados_OA[:])
        all_dados_oleo.append(dados_OB[:])
        all_dados_oleo.append(dados_OA_c[:])
        all_dados_oleo.append(dados_OB_c[:])

        # Calcular media e desvio padrão para Hidratação
        media1 = statistics.mean(dados_HA)  # Hidratação Braço A t0
        media2 = statistics.mean(dados_HB)  # Hidratação Braço B t0
        media3 = statistics.mean(dados_HA_c)  # Hidratação Braço A t1
        media4 = statistics.mean(dados_HB_c)  # Hidratação Braço B t1 (Braço com Hidratante)

        des_pad1 = round(statistics.stdev(dados_HA), 2)  # Desvio Padrão Braço A t0
        des_pad2 = round(statistics.stdev(dados_HB), 2)  # Desvio Padrão Braço B t0
        des_pad3 = round(statistics.stdev(dados_HA_c), 2)  # Desvio Padrão Braço A t1
        des_pad4 = round(statistics.stdev(dados_HB_c), 2)  # Desvio Padrão Braço B t1 (Com hidra)

        # Calcular media e desvio padrão para Oleosidade
        media5 = statistics.mean(dados_OA)  # Oleosidade Braço A t0
        media6 = statistics.mean(dados_OB)  # Oleosidade Braço B t0
        media7 = statistics.mean(dados_OA_c)  # Oleosidade Braço A t1
        media8 = statistics.mean(dados_OB_c)  # Oleosidade Braço B t1 (Braço com Hidratante)

        des_pad5 = round(statistics.stdev(dados_OA), 2)  # Desvio Padrão Braço A t0
        des_pad6 = round(statistics.stdev(dados_OB), 2)  # Desvio Padrão Braço B t0
        des_pad7 = round(statistics.stdev(dados_OA_c), 2)  # Desvio Padrão Braço A t1
        des_pad8 = round(statistics.stdev(dados_OB_c), 2)  # Desvio Padrão Braço B t1 (Com hidratante)

        all_dados_hidra.append([media1, media2, media3, media4])
        all_dados_hidra.append([des_pad1, des_pad2, des_pad3, des_pad4])

        all_dados_oleo.append([media5, media6, media7, media8])
        all_dados_oleo.append([des_pad5, des_pad6, des_pad7, des_pad8])

        # Adicionar dados à variável global
        dados_gerais_hidra[item] = all_dados_hidra
        dados_gerais_oleo[item] = all_dados_oleo

print(dados_gerais_hidra)
print(dados_gerais_oleo)


# 3 - Preparar gráficos

fig, axs = plt.subplots(1, 4, figsize=(10, 5))
fig.suptitle('Dados Hidratação')

for i, ax in enumerate(axs):
    file_name = ficheiros[i] + '.csv'
    ax.boxplot([dados_gerais_hidra.get(file_name)[0], dados_gerais_hidra.get(file_name)[1], dados_gerais_hidra.get(file_name)[2], dados_gerais_hidra.get(file_name)[3]], labels=['A', 'B', 'A_c', 'B_c'])

    title = file_name.split('_')[2]
    ax.set_title(title)

    ax.set_ylim(10, 40)

# Graficos Oleosidade

fig, axs = plt.subplots(1, 4, figsize=(10, 5))
fig.suptitle('Dados Oleosidade')

for i, ax in enumerate(axs):
    file_name = ficheiros[i] + '.csv'
    ax.boxplot([dados_gerais_oleo.get(file_name)[0], dados_gerais_oleo.get(file_name)[1], dados_gerais_oleo.get(file_name)[2], dados_gerais_oleo.get(file_name)[3]], labels=['A', 'B', 'A_c', 'B_c'])

    title = file_name.split('_')[2]
    ax.set_title(title)

    ax.set_ylim(0, 20)

plt.show()

# Os dados que estão como A e B se referem ao tempo 0 e os dados que estão como A_c e B_c são do segundo tempo
# Levando em consideração que não foi posto hidratante no braço A, somente no B
