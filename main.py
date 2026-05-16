#1° instalamos as duas bibliotecas necessarias para execução e visualização da atividade

import matplotlib.pyplot as plt  #Bibloteca para a criação de visualizações estáticas, animadas e interativas de dados
from pandas import read_csv #Biblioteca para leitura e edição do arquivo csv


series = read_csv("USD_BRL_hist.csv", header=0, index_col=0, parse_dates=True, dayfirst=True) #Leitura do CSV 

#GRÁFICO LINHA 
plt.figure()
plt.plot(series.index, series["USD_BRL"]) # .index recebe o valor da primeira informação da tabela series que nesse caso é a "Data" ou Eixo X
plt.title("Grafico 1 - Linhas")

#GRÁFICO BARRAS
plt.figure()
plt.bar(series.index, series["USD_BRL"]) # a caluna "USD_BRL" seria o eixo Y das tabelas
plt.title("Gráfico 2 - Barras")

#GRÁFICO DISPERÇÂO
plt.figure()
plt.scatter(series.index, series["USD_BRL"])
plt.title("Gráfico 3 - Disperção")

plt.show()#Exibe os gráficos  
