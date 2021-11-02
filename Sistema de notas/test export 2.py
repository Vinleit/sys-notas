import pandas as pd

nomes_e_notas = []
contador = 0

while True:
    nome = str(input("Nome: "))
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    nomes_e_notas.append(list())
    nomes_e_notas[contador].append(nome)
    nomes_e_notas[contador].append(nota_1)
    nomes_e_notas[contador].append(nota_2)
    nomes_e_notas[contador].append((nota_1 + nota_2) / 2)
    contador += 1
    continuar = " "

    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break

dados = pd.DataFrame(nomes_e_notas)
print(dados[2][1])  #PRIMEIRO É A COLUNA, E DEPOOISS Q É A LINHA
print(dados)

dados = pd.DataFrame(nomes_e_notas)
dados.to_excel(excel_writer='agora_vai.xlsx' , sheet_name="pg_nomes")
