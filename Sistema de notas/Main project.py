from PySimpleGUI import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import win32com.client as win32
import os.path


#LAYOUT DO INICIO
sg.theme("SystemDefault")
layout_inicio = [
    [sg.Text("Turma:" , font="Helvetica") , sg.Input(key="Turma" , size=(35 , 0))],
    [sg.Text("Quantas notas?" , font="Helvetica")],
    [sg.Radio("2 Notas" , font="Helvetica", key="2_notas" , group_id="Notas") , sg.Radio("3 notas" , font="Helvetica" , key="3_notas" , group_id="Notas")],
    [sg.Button("Continuar" , font="Helvetica" , key="Continuar")]
]

#JANELA
janela_inicio = sg.Window("Cadastro de Notas" , layout=layout_inicio , element_justification="center")

#Eventos DO INICIO

turma = str()

while True:
    eventos , valores = janela_inicio.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == "Continuar":
        turma = valores["Turma"]

        if valores["2_notas"]:
            janela_inicio.close()

            # LAYOUT DO MAIN
            sg.theme("SystemDefault")
            layout_main = [
                [sg.Text("Nome:", font="Helvetica"), sg.Input(key="Nome", size=(48, 0))],
                [sg.Text("P1:", font="Helvetica"), sg.Input(key="P1", size=(50, 0))],
                [sg.Text("TB:", font="Helvetica"), sg.Input(key="TB", size=(50, 0))],
                [sg.Button("Adicionar", size=(35, 0), font="Helvetica", ),
                 sg.Button("Salvar e encerrar", size=(15, 0) , font="Helvetica")]
            ]

            # JANELA
            janela_main = sg.Window("Cadastro de Notas", layout=layout_main)

            # EVENTOS DA MAIN
            nomes_e_notas = [["NOME", "P1", "TB", "MÉDIA"], ]
            c = 1
            while True:
                eventos, valores = janela_main.read()
                if eventos == sg.WIN_CLOSED:
                    break

                if eventos == "Adicionar":
                    nomes_e_notas.append(list())
                    nomes_e_notas[c].append(valores["Nome"])
                    nomes_e_notas[c].append(float(valores["P1"]))
                    nomes_e_notas[c].append(float(valores["TB"]))
                    nomes_e_notas[c].append((float(valores["P1"]) + float(valores["TB"])) / 2)
                    c += 1
                    janela_main.FindElement("Nome").Update('')
                    janela_main.FindElement("P1").Update('')
                    janela_main.FindElement("P1").Update('')
                    janela_main.FindElement("TB").Update('')

                if eventos == "Salvar e encerrar":
                    janela_main.close()


                    # EXCEL
                    dados = pd.DataFrame(nomes_e_notas)
                    dados.to_excel(excel_writer=f"Planilha {turma}.xlsx", sheet_name="pg.1", index=False, header=False)

                    # GRÁFICO
                    x_nomes = []
                    for c in range(1, len(nomes_e_notas)):
                        x_nomes.append(nomes_e_notas[c][0])

                    y_media = []
                    for c in range(1, len(nomes_e_notas)):
                        y_media.append(nomes_e_notas[c][3])

                    plt.bar(x_nomes, y_media, color="cyan" , edgecolor="darkblue" , linewidth=2)
                    plt.title(f"Gráfico dos alunos do {turma}")
                    plt.xlabel("NOMES")
                    plt.ylabel("NOTAS")
                    plt.savefig(f"Grafico {turma}.png")

                    # # MANDANDO POR E-MAIL
                    # outlook = win32.Dispatch("outlook.application")
                    # email = outlook.CreateItem(0)
                    #
                    # email.To = "josievinileite@gmail.com"
                    # email.Subject = "Notas da turma"
                    # email.HTMLBody = """"
                    # <p>Segue em anexo as notas da turma e o gráfico de desempenho</p>
                    # """
                    #
                    # anexo_excel = f"{os.path.abspath(f'Planilha {turma}.xlsx')}"
                    # email.Attachments.Add(anexo_excel)
                    #
                    # anexo_grafico = f"{os.path.abspath(f'Grafico {turma}.png')}"
                    # email.Attachments.Add(anexo_grafico)
                    #
                    # email.Send()


        elif valores["3_notas"]:
            janela_inicio.close()

            # LAYOUT DO MAIN
            sg.theme("SystemDefault")
            layout_main = [
                [sg.Text("Nome:", font="Helvetica"), sg.Input(key="Nome", size=(48, 0))],
                [sg.Text("P1:", font="Helvetica"), sg.Input(key="P1", size=(50, 0))],
                [sg.Text("P2:", font="Helvetica"), sg.Input(key="P2", size=(50, 0))],
                [sg.Text("TB:", font="Helvetica"), sg.Input(key="TB", size=(50, 0))],
                [sg.Button("Adicionar", size=(35, 0), font="Helvetica"),
                 sg.Button("Salvar e encerrar", size=(15, 0) , font="Helvetica")]
            ]

            # JANELA
            janela_main = sg.Window("Cadastro de Notas", layout=layout_main)

            # EVENTOS DA MAIN
            nomes_e_notas = [["NOME", "P1", "P2", "TB", "MÉDIA"], ]
            c = 1
            while True:
                eventos, valores = janela_main.read()
                if eventos == sg.WIN_CLOSED:
                    break

                if eventos == "Adicionar":
                    nomes_e_notas.append(list())
                    nomes_e_notas[c].append(valores["Nome"])
                    nomes_e_notas[c].append(float(valores["P1"]))
                    nomes_e_notas[c].append(float(valores["P2"]))
                    nomes_e_notas[c].append(float(valores["TB"]))
                    nomes_e_notas[c].append(float(valores["P1"]) + float(valores["P2"]) + float(valores["TB"]) / 3)
                    c += 1
                    janela_main.FindElement("Nome").Update('')
                    janela_main.FindElement("P1").Update('')
                    janela_main.FindElement("P2").Update('')
                    janela_main.FindElement("TB").Update('')

                if eventos == "Salvar e encerrar":
                    janela_main.close()

                    # EXCEL

                    dados = pd.DataFrame(nomes_e_notas)
                    dados.to_excel(excel_writer=f"Planilha {turma}.xlsx", sheet_name="pg.1", index=False, header=False)

                    # GRÁFICO
                    x_nomes = []
                    for c in range(1, len(nomes_e_notas)):
                        x_nomes.append(nomes_e_notas[c][0])

                    y_media = []
                    for c in range(1, len(nomes_e_notas)):
                        y_media.append(nomes_e_notas[c][4])

                    plt.bar(x_nomes , y_media, color="cyan" , edgecolor="darkblue" , linewidth=2)
                    plt.title(f"Gráfico dos alunos do {turma}")
                    plt.xlabel("NOMES")
                    plt.ylabel("NOTAS")
                    plt.savefig(f"Grafico {turma}.png")

                    # # MANDANDO POR E-MAIL
                    # outlook = win32.Dispatch("outlook.application")
                    # email = outlook.CreateItem(0)
                    #
                    # email.To = "josievinileite@gmail.com"
                    # email.Subject = "Notas da turma"
                    # email.HTMLBody = """"
                    # <p>Segue em anexo as notas da turma e o gráfico de desempenho</p>
                    # """
                    #
                    # anexo_excel = f"{os.path.abspath(f'Planilha {turma}.xlsx')}"
                    # email.Attachments.Add(anexo_excel)
                    #
                    # anexo_grafico = f"{os.path.abspath(f'Grafico {turma}.png')}"
                    # email.Attachments.Add(anexo_grafico)
                    #
                    # email.Send()