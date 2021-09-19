import pandas as pd
import matplotlib.pyplot as plt

lista = []

for c in range(0 , 2):
    lista.append(list())
    nome = (input("Nome: "))
    prova_1 = (float(input("P1: ")))
    prova_2 = (float(input("P2: ")))
    lista[c].append(nome)
    lista[c].append(prova_1)
    lista[c].append(prova_2)
    lista[c].append((prova_1 + prova_2) / 2)


print(lista)
dados = pd.DataFrame(lista)
x = [lista[0][0], lista[1][0]]
y = [lista[0][3] , lista[1][3]]
print(x)
print(y)


plt.figure(figsize=(5,5))
plt.bar(x , y , color="dodgerblue" , edgecolor="darkblue" , linewidth=2)

plt.savefig("teste.png")
#plt.show()
