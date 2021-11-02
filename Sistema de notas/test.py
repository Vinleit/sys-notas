import pandas as pd
import matplotlib.pyplot as plt
import numpy
import openpyxl

tabela_excel = pd.read_excel(r"C:\Users\vinicius\Desktop\teste.xlsx", engine='openpyxl')
dados = pd.DataFrame(tabela_excel)

#print(dados["NOTA"])
# print(tabela_excel)
plt.hist(dados["NOTA"])
plt.show()

#plt.title("Um titulo aqui")  #Dá pra fazer um titulo com ele
#plt.savefig("teste.png")  #--> Ele faz o download do gráfico q eu plotei
#plt.savefig("teste.png", transparent=True) #Ele faz o gráfico transparente
#print(tabela_excel["IDADE"] [1]) -->Pega um item especifico da lista