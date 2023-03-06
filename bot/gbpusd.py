import tv_to_mail_connector
from email_del import del_mail

pair = "gbpusd"
del_mail(pair)
for i in range(1,100000):
    tv_to_mail_connector.place_order(pair)