import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
filename="report.txt"
f=open(filename,"rb")


msg=MIMEMultipart()

part=MIMEBase('application',"octet-stream")
part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition","attachment; filename= "+filename)

msg.attach(part)
text=msg.as_string()

mail =smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('arbitrageterry@gmail.com','m4r14n0p0l15')
mail.sendmail("arbitrageterry@gmail.com","arbitrageterry@gmail.com",text)
mail.quit()