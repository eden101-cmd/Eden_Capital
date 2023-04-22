# here we will do the action of sending an email
#ssl.create_default_context() -> This function is typically used in Python applications that
# require secure communication over the internet,
# such as HTTPS web connections or secure email protocols like SMTPS or IMAPS.
import smtplib
import ssl
import os
#"neuhigeusieyftqj"
def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "coheneden100@gmail.com"
    password = "neuhigeusieyftqj"
    #
    receiver = "coheneden100@gmail.com"
    context = ssl.create_default_context()

    # with the syntax of """\ Subject we created a subject to our mail.
    with smtplib.SMTP_SSL(host, port, context=context) as server:  # we have to add the context arg or it wont work!
        server.login(username, password)
        server.sendmail(username, receiver, message)

