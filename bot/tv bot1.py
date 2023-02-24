from iqoptionapi.stable_api import IQ_Option
import easyimap as e
import imaplib

emailid = "tsignalmail@gmail.com"
passward = "ztipkqtxgltshpqh"
IMAP = 'imap.gmail.com'

server_e = e.connect(IMAP,emailid,passward)
server_i = imaplib.IMAP4_SSL(IMAP)
server_i.login(emailid, passward)

api=IQ_Option("techyankit199@gmail.com","ankitsaini2003")
api.connect()#connect to iqoption

curruncy = api.get_currency()
balance = api.get_balance()
Money=1/100*balance
expirations_mode=1

def place_order():
    server_e = e.connect(IMAP,emailid,passward)
    server_i = imaplib.IMAP4_SSL(IMAP)
    server_i.login(emailid, passward)
    try:
        server_i.select("inbox")
        email_e = server_e.mail(server_e.listids(limit=1, criterion=None)[0])      #selecting top 1 email
        data_e = email_e.body                                                   #taking title of the email
        str_data = data_e.split()                                              #data will come in string so splitng it and making it in list to to make readin easy
    
        if email_e.title == "Alert: ." or email_e.title == "Alert: candal stats: Any alert() function call" :
            fd = str_data[666-1].split(">")
            fd2 = fd[1].split("<")
            print(fd2)
            ACTIVES = str_data[345-1].split(">")
            
            if fd2[0] == "up":
                place_trade = api.buy(Money,ACTIVES[0],"call",expirations_mode)
                if place_trade[0] == True:
                    print("trade placed up")
                    #---------     for deleting mail ------------------
                    typ, data_i = server_i.search(None, 'FROM "noreply@tradingview.com"') #Filter by sender
                    for num in data_i[0].split():
                        #deleting the mails
                        server_i.store(num, '+FLAGS', r'(\Deleted)')
                        server_i.expunge()
                        print("E-mail deleted")
                elif place_trade[0] ==False :
                    print("BUY ERROR",place_trade[1])
                

            elif fd2[0] == "down":
                    place_trade = api.buy(Money,ACTIVES[0],"put",expirations_mode)
                    if place_trade[0] == True:
                        print("trade placed down")
                        #---------     for deleting mail ------------------
                        typ, data_i = server_i.search(None, 'FROM "noreply@tradingview.com"') #Filter by sender
                        for num in data_i[0].split():
                            #deleting the mails
                            server_i.store(num, '+FLAGS', r'(\Deleted)')
                            server_i.expunge()
                            print("E-mail deleted")
                    elif place_trade[0] ==False :
                            print("BUY ERROR",place_trade[1])
                        
                
        else :
            print("not a trade signal")

    except:
        print("NO E-mail found")

place_order()
