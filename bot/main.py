import tv_bot1
import imaplib

emailid = "tsignalmail@gmail.com"
passward = "ztipkqtxgltshpqh"
IMAP = 'imap.gmail.com'

server_i = imaplib.IMAP4_SSL(IMAP)
server_i.login(emailid, passward)

for i in range(1,5):
    print("in for loop")
    server_i.select("inbox")
    typ, data_i = server_i.search(None, 'ALL') #Filter by sender
    try:
        for num in data_i[0].split():
            #deleting the mails
            server_i.store(num, '+FLAGS', r'(\Deleted)')
            server_i.expunge()
            print("E-mail deleted")

    except:
        print("NO MAIL IN INBOX")

while True:
    tv_bot1.place_order()

