import travel_data as email

path_txt = 'C:/Users/Lochofo/Desktop/PAGINAS/email_sender/Include/email.txt'

destinatarios = ["eitanluc@gmail.com"]

datos = email.usuario_contrasenia(path_txt)

email.enviar_mail(datos[0], datos[1], "prueba asunto", "preguba mensaje", destinatarios)