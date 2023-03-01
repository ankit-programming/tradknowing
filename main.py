import tv_to_mail_connector
from threading import Thread
import imaplib#for deleting file


def del_mail(pair):
    for i in range(5):
        print(i)            
        passfile = open(f'{pair} pass.txt', 'r')
        idfile = open(f'{pair} id.txt', 'r')
        emailid = idfile.read()
        passward = passfile.read()
        IMAP = 'imap.gmail.com'
        server_i = imaplib.IMAP4_SSL(IMAP)
        server_i.login(emailid, passward)

        server_i.select("inbox")   #selecting inbox for rading email
        typ, data_i = server_i.search(None, 'ALL') 
        for num in data_i[0].split():
            #deleting the mails
            server_i.store(num, '+FLAGS', r'(\Deleted)')
            server_i.expunge()
            print("E-mail deleted")


#this algo will run once in at time at app runing but
#it will deleting all mail from all ids and it will stop running

'''pair = ["eurgbp","eurjpy","eurusd","gbpusd","usdjpy"]
for i in pair:
    print(i)
    del_mail(i)'''

