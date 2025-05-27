
import smtplib
from email.message import EmailMessage

#Configurar email e senha
EMAIL_ADDRESS = 'email@gomail.com'
EMAIL_PASSWORD = 'Pass'

#Criar um email

msg = EmailMessage(" Hello ")
msg['Assunto'] = 'Teste envio Python'
msg['De'] = 'email@gomail.com'
msg['Para'] = 'emailtest@gomail.com'
msg.set_content(' Test Mail by Python ')

# Enviar um email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
