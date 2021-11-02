from PySimpleGUI import PySimpleGUI as sg

#LAYOUT
sg.theme("reddit")
layout = [
    [sg.Text("Nome:") , sg.Input(key="Nome")],
    [sg.Text("P1:") , sg.Input(key="P1")],
    [sg.Text("P2:") , sg.Input(key="P2")],
    [sg.Text("TB:") , sg.Input(key="TB")],
    [sg.Button("Adicionar" , size=(50,0))]
]

#JANELA
janela = sg.Window("Tela de Notas" , layout)

#Lendo os eventos
nomes_e_notas = []
c = 0
while True:
    eventos , valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == "Adicionar":
        nomes_e_notas.append(list())
        nomes_e_notas[c].append(valores["Nome"])
        nomes_e_notas[c].append(float(valores["P1"]))
        nomes_e_notas[c].append(float(valores["P2"]))
        nomes_e_notas[c].append(float(valores["TB"]))
        nomes_e_notas[c].append((float(valores["P1"]) + float(valores["P2"]) + float(valores["TB"])) / 3)
        c += 1
        janela.FindElement("Nome").Update('')
        janela.FindElement("P1").Update('')
        janela.FindElement("P2").Update('')
        janela.FindElement("TB").Update('')
    print(nomes_e_notas)
