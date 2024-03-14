import yagmail

def usuario_contrasenia(ruta):
    with open(ruta, 'r') as archivo:
        return archivo.readlines()

def enviar_mail(mail, contrasenia, asunto, mensaje, destinatarios):
    yag = yagmail.SMTP(user=mail, password=contrasenia)
    return yag.send(destinatarios, asunto, mensaje)