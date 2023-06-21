# importando as configurações necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# nomeando os arquivos do excel salvos na pasta main.py
arquivo_excel_1 = '1e2.xlsx'
arquivo_excel_2 = '3.xlsx'

# declarando as variaveis e lendo as pastas dentro das planilhas
df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='Dia 1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name='Dia 2')
df_dia_3 = pd.read_excel(arquivo_excel_2)

# juntando as três planilhas em apenas uma só
df_todas_as_planilhas = pd.concat([df_dia_1, df_dia_2, df_dia_3])

# salvando a planilha consolidada acima com todas informações em um arquivo só
df_todas_as_planilhas.to_excel('consolidado.xlsx')

# mostrando apenas as informações do vendedor
print(df_todas_as_planilhas['Vendedor'])

# agrupando as informações de vendedor, e somando
lucro_dos_vendedores = df_todas_as_planilhas.groupby(['Vendedor']).sum()

print(lucro_dos_vendedores)

# mostrando apenas as informações de unidades e preço, somando, e mostrando em um novo relatório
relatorio_bonito = lucro_dos_vendedores.loc[:, 'Unidades':'Preço']

print(relatorio_bonito)

# declarando o gráfico (barras)
relatorio_bonito.plot(kind='bar')

# comando para exibir o gráfico de barras
plt.show()
