import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_mail_pdf(file_path):
    host = "smtp.gmail.com"
    port = 465
    username = "coheneden100@gmail.com"
    password = "neuhigeusieyftqj"
    receiver = "coheneden100@gmail.com"
    context = ssl.create_default_context()

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = username
    message["To"] = receiver
    message["Subject"] = "PDF file attachment"

    # Add body to email
    message.attach(MIMEText("here is the buying report of the client.", "plain"))

    # Open PDF file in binary mode
    with open(file_path, "rb") as pdf_file:
        # Add PDF file as application/octet-stream
        # Email client can usually download this automatically as attachment
        pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header("Content-Disposition", "attachment", filename="pdf_file.pdf")
        message.attach(pdf_attachment)

    # Login to SMTP server and send email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.as_string())
