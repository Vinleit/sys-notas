import win32com.client as win32

#Criar integração com o e-mail
outlook = win32.Dispatch('outlook.application')

#criar um e-mail
email = outlook.CreateItem(0)

#Configurar informações do e-mail
email.To = "josievinileite@gmail.com"
email.Subject = "Teste de automatização"
email.HTMLBody = f"""
<h1>Automatizando e-mails com python</h1>

"""

#Enviando um anexo
anexo = "C:/Users/vinicius/Desktop/teste.xlsx"
email.Attachments.Add(anexo)

#Enviar o e-mail
email.Send()
print("O e-mail foi enviado com sucesso")
