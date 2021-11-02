import os.path
#
# print(os.path.isdir("teste.xlsx"))
# print(os.path.isfile("teste.xlsx"))
# print(os.path.exists("teste.xlsx"))
# print(os.path.getsize("teste.xlsx"))    #Vê o tamanho do arquivo
print(os.path.abspath("teste.xlsx"))    #Vê o caminho absoluto e adiciona o nome do arquivo no final
print(os.path.realpath("teste.xlsx"))