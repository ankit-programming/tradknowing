from iqoptionapi.stable_api import IQ_Option
import easyimap as e #for reading email
import imaplib#for deleting file
import time

api=IQ_Option("techyankit199@gmail.com","ankitsaini2003")
api.connect()#connect to iqoption 
balance = api.get_balance()#to get balance of account
Money=1/100*balance #for traing with 1% of capital we have
expirations_mode=1
#curruncy = api.get_currency()#to knoe which curruncey we are using in account

pair = "usdjpy"
try:#opening id and pass file 
    passfile = open(f'{pair} pass.txt', 'r')
    idfile = open(f'{pair} id.txt', 'r')
except:
    print("FILE   ERROR","\n","ID and PASS FILE cant find")
    print("make file name:-","'curruncy pair name' id ","\n","'curruncy pair name' pass ")

emailid = idfile.read()#"tsignalmail@gmail.com"
passward = passfile.read()#"ztipkqtxgltshpqh"
IMAP = 'imap.gmail.com'
server_e = e.connect(IMAP,emailid,passward)
server_i = imaplib.IMAP4_SSL(IMAP)
server_i.login(emailid, passward)

def place_order():

    try:
        server_i.select("inbox")   #selecting inbox for rading email
        email_e = server_e.mail(server_e.listids(limit=1, criterion=None)[0])      #selecting top 1 email
        data_e = email_e.body                                                   #taking title of the email
        str_data = data_e.split() 
        data_e_t = email_e.title
        title= data_e_t.split()                                               #data will come in string so splitng it and making it in list to to make readin easy
    
        if title[0] == "Alert:":#setting condition for taking only "." titeld email
            fd = str_data[666-1].split(">")  #email will have many element in list in which 666 is having our signal so we will split it and use only "BUY" or "SELL"
            fd2 = fd[1].split("<")
            ACTIVES = str_data[345-1].split(">") #for taking curruncy pair name from data
            
            if fd2[0] == "up":
                place_trade = api.buy(Money,ACTIVES[0],"call",expirations_mode) #for placiing trade in  iq option broker
                if place_trade[0] == True:
                    print("trade placed up")
                    #---------     for deleting mail ------------------
                    typ, data_i = server_i.search(None, 'FROM "noreply@tradingview.com"') #Filter by sender email id
                    '''for num in data_i[0].split():
                        #deleting the mails
                        server_i.store(num, '+FLAGS', r'(\Deleted)')
                        server_i.expunge()
                        print(pair,"E-mail deleted")'''
                elif place_trade[0] ==False :
                    print("BUY ERROR",place_trade[1])
                

            elif fd2[0] == "down":
                    place_trade = api.buy(Money,ACTIVES[0],"put",expirations_mode)
                    if place_trade[0] == True:
                        print("trade placed down")
                        #---------     for deleting mail ------------------
                        typ, data_i = server_i.search(None, 'FROM "noreply@tradingview.com"') #Filter by sender
                        '''for num in data_i[0].split():
                            #deleting the mails
                            server_i.store(num, '+FLAGS', r'(\Deleted)')
                            server_i.expunge()
                            print("E-mail deleted")'''
                    elif place_trade[0] ==False :
                            print("BUY ERROR",place_trade[1])
                        
        
        else :
            print("not a trade signal")

    except:
        print("NO E-mail found")

start = time.time()
for i in range(5):
     print(i)
     place_order()
     
end = time.time()

print("out of def ",end-start)




def place_order_or():
    pair = "usdjpy"
    try:#opening id and pass file 
        passfile = open(f'{pair} pass.txt', 'r')
        idfile = open(f'{pair} id.txt', 'r')
    except:
        print("FILE   ERROR","\n","ID and PASS FILE cant find")
        print("make file name:-","'curruncy pair name' id ","\n","'curruncy pair name' pass ")

    emailid = idfile.read()#"tsignalmail@gmail.com"
    passward = passfile.read()#"ztipkqtxgltshpqh"
    IMAP = 'imap.gmail.com'
    server_e = e.connect(IMAP,emailid,passward)
    server_i = imaplib.IMAP4_SSL(IMAP)
    server_i.login(emailid, passward)

    try:
        server_i.select("inbox")   #selecting inbox for rading email
        email_e = server_e.mail(server_e.listids(limit=1, criterion=None)[0])      #selecting top 1 email
        data_e = email_e.body                                                   #taking title of the email
        str_data = data_e.split() 
        data_e_t = email_e.title
        title= data_e_t.split()                                               #data will come in string so splitng it and making it in list to to make readin easy
    
        if title[0] == "Alert:":#setting condition for taking only "." titeld email
            fd = str_data[666-1].split(">")  #email will have many element in list in which 666 is having our signal so we will split it and use only "BUY" or "SELL"
            fd2 = fd[1].split("<")
            ACTIVES = str_data[345-1].split(">") #for taking curruncy pair name from data
            
            if fd2[0] == "up":
                place_trade = api.buy(Money,ACTIVES[0],"call",expirations_mode) #for placiing trade in  iq option broker
                if place_trade[0] == True:
                    print("trade placed up")
                    #---------     for deleting mail ------------------
                    typ, data_i = server_i.search(None, 'FROM "noreply@tradingview.com"') #Filter by sender email id
                    '''for num in data_i[0].split():
                        #deleting the mails
                        server_i.store(num, '+FLAGS', r'(\Deleted)')
                        server_i.expunge()
                        print(pair,"E-mail deleted")'''
                elif place_trade[0] ==False :
                    print("BUY ERROR",place_trade[1])
                

            elif fd2[0] == "down":
                    place_trade = api.buy(Money,ACTIVES[0],"put",expirations_mode)
                    if place_trade[0] == True:
                        print("trade placed down")
                        #---------     for deleting mail ------------------
                        typ, data_i = server_i.search(None, 'FROM "noreply@tradingview.com"') #Filter by sender
                        '''for num in data_i[0].split():
                            #deleting the mails
                            server_i.store(num, '+FLAGS', r'(\Deleted)')
                            server_i.expunge()
                            print("E-mail deleted")'''
                    elif place_trade[0] ==False :
                            print("BUY ERROR",place_trade[1])
                        
        
        else :
            print("not a trade signal")

    except:
        print("NO E-mail found")


start = time.time()
for i in range(5):
     print(i)
     place_order()
     
end = time.time()

print("in def ",end-start)
