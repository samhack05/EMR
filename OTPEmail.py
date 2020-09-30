# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# sender_email = "python.ayush@gmail.com"
# password = 'emr123coolpsu'
#
# def sendotpmail(receiver_email, subject,htmlbodytext):
#     message = MIMEMultipart("alternative")
#     message["Subject"] = subject
#     message["From"] = sender_email
#     message["To"] = receiver_email
#
#     html = htmlbodytext
#     """
#     <html>
#       <body>
#         <p>Hi,<br>
#            How are you?<br>
#            <a href="http://www.realpython.com">Real Python</a>
#            has many great tutorials.
#         </p>
#       </body>
#     </html>
#     """
#
#     part2 = MIMEText(html, "html")
#
#     message.attach(part2)
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(
#             sender_email, receiver_email, message.as_string()
#         )
#
# sendotpmail(receiver_email='ayushsaxena210@gmail.com', subject="testing",htmlbodytext="<h1>hey</h1><h6>ayush</h6>")



import clx.xms
import requests

client = clx.xms.Client(service_plan_id='4624b9e22f10426ab93a4af867697b7e', token='983398f58b1c4ee18076d851867234b2')

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = '447537432321'
create.recipients = {'91 7007578720'}
create.body = '32478 This is a test message from your Sinch account fuck u'

try:
  batch = client.create_batch(create)
except (requests.exceptions.RequestException,
  clx.xms.exceptions.ApiException) as ex:
  print('Failed to communicate with XMS: %s' % str(ex))
