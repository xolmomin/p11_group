# # csv, yaml, json, xml, xlsx, docx
#
# # csv
# data = []
# import csv
# with open('../districts.csv') as f:
#     f.readline()
#     for i in csv.reader(f):
#         data.append({
#             'id': int(i[0]),
#             'name': i[1],
#             'region_id': int(i[2])
#         })
#
# # # yaml, yml
# # # pip3 install pyyaml
# # import yaml
# # with open('districts.yml', 'w') as f:
# #     yaml.dump(data, f)
# #
# # # json
# # import json
# # with open('districts.json', 'w') as f:
# #     json.dump(data, f, indent=2)
#
#
# # import pandas as pd
# #
# # data = pd.read_csv('../districts.csv')
# #
# # for i in data.shape:
# #     print(i)

# encode, decode
import base64
# text, binary


# # image->text
with open('../python.png', 'rb') as f:
    data = f.read()
    data = base64.b64encode(data).decode('utf-8')

with open('b-data.txt', 'w') as f:
    f.write(data)


# # text->image
with open('b-data.txt') as f:
    d = f.read()
    d = base64.b64decode(d)
    with open('rasm.png', 'wb') as file:
        file.write(d)


import smtplib
from email.message import EmailMessage
import smtplib

msg = EmailMessage()
msg["Subject"] = "File yuborish"
msg["From"] = "me <sender@example.org>"
msg["To"] = "recipient <victim@example.net>"
with open("data.txt") as fp:
    msg.add_attachment(fp.read(), maintype="text", subtype="txt")

port = 465
host = 'smtp.gmail.com'
email = 'smtp@gmail.com'
password = ''
to_email = ''
msg = '123'

# array & hashing, stack, linked list

# sqlalchemy
# psycopg2
# sqlite3

with smtplib.SMTP_SSL(host, port) as server:
    server.login(email, password)
    # server.send(msg)
    server.sendmail(email, to_email, msg)


# a = 123
#
# print(fr'hello\n{a}')
#
# print(rf'hello\n{a}')
# print(r'hello\n{a}')
# print(b'hello')
# print(f'hello\n{a}')
