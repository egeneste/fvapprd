import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def enviar(para, tipo, fecha, temperatura, humedad, image, commentario="" ):

    emisor = 'misterley@gmail.com'
    password = 'tyJfyl26'
    receptor = [para, 'misterley@live.com']

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('misterley@gmail.com', password)

    foto = image
    mensaje = 'Se ha detectado una amenaza \n:Tipo'+tipo+'\nFecha: '+fecha+'\nTemperatura hambiental: '+temperatura+'\nHumedad :'+humedad+'\n' + commentario


    msg = MIMEMultipart()
    msg['Subject'] = "Alerta Forest Vigiance"
    msg['From'] = emisor
    msg['To'] = para.join(receptor)

    msg.attach(MIMEText(mensaje, 'plain'))
    #cabezera = 'To: ' + Para + '\n' + 'De: ' + De + 'Objeto: Alerta'
    servidor.sendmail(emisor, receptor, msg.as_string())
    print('msg sent')
    servidor.close()

def sensorFailmsg(para, commentario):

    emisor = 'misterley@gmail.com'
    password = 'tyJfyl26'
    receptor = [para, 'misterley@live.com', 'misterley@live.com']

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('misterley@gmail.com', password)


    mensaje =  commentario


    msg = MIMEMultipart()
    msg['Subject'] = "Alerta Forest Vigiance"
    msg['From'] = emisor
    msg['To'] = para.join(receptor)

    msg.attach(MIMEText(mensaje, 'plain'))
    #cabezera = 'To: ' + Para + '\n' + 'De: ' + De + 'Objeto: Alerta'
    servidor.sendmail(emisor, receptor, msg.as_string())
    print('msg sent')
    servidor.close()

'''

6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "YOUR EMAIL"
toaddr = "EMAIL ADDRESS YOU SEND TO"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"
 
body = "TEXT YOU WANT TO SEND"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "NAME OF THE FILE WITH ITS EXTENSION"
attachment = open("PATH OF THE FILE", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

'''