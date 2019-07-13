import smtplib

# Details

subject = 'iyaanazeez757@gmail.com'
smtp_user = 'iyaanazeez757@gmail.com'
smtp_password = 'iyaan7571892'

def send_mail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_user, smtp_password)

    except:
        print('Could not connect. . . . . ')
    
   


