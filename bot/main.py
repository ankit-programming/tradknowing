'''while True:
    exec(open("tv bot1.py").read())'''


import tv_bot1
import imaplib

emailid = "tsignalmail@gmail.com"
passward = "ztipkqtxgltshpqh"
IMAP = 'imap.gmail.com'

server_i = imaplib.IMAP4_SSL(IMAP)
server_i.login(emailid, passward)

server_i.select("inbox")

typ, data_i = server_i.search(None, 'FROM "noreply@tradingview.com"') #Filter by sender

for num in data_i[0].split():
    #deleting the mails
    server_i.store(num, '+FLAGS', r'(\Deleted)')
    server_i.expunge()
    print("E-mail deleted")

while True:
    tv_bot1.place_order()

