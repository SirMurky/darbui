import requests
import json
import json2table
import smtplib


f = open("lentele.txt","a") 
#gaunam tik europos duomenis
URL = "http://18.221.188.117/Darbas/EU.php"
#gaunam ne europos duomenis
URL2 = "http://18.221.188.117/Darbas/NEEU.php"
#nebutini{
location = "TIK EUROPA"
location2 = "NE EUROPA"
PARAMS = {'address':location}
PARAMS2 = {'adress':location2}
#}

def GETEU():
    #get requestas - gaunam JSON formatu duomenis
    r = requests.get(url = URL, params = PARAMS) 
    infoFromJson = json.loads(r.text)
    build_direction = "LEFT_TO_RIGHT"
    #spalva melyna nes Europa
    table_attributes = {"style": "width:100%, bgcolor:blue"}
    #kiekviena eilute perrasom i txt faila
    for item in infoFromJson:
        f.write(json2table.convert(item, 
                            build_direction=build_direction, 
                            table_attributes=table_attributes)+"\n")
def GETNOTEU():
    #get requestas - gaunam JSON formatu duomenis
    r2 = requests.get(url = URL2, params = PARAMS2) 
    infoFromJson2 = json.loads(r2.text)
    build_direction = "LEFT_TO_RIGHT"
    #spalva raudona nes ne Europa
    table_attributes = {"style": "width:100%, bgcolor:red"}
    #kiekviena eilute perrasom i txt faila
    for item in infoFromJson2:
        f.write(json2table.convert(item, 
                            build_direction=build_direction, 
                            table_attributes=table_attributes)+"\n")

#paleidziam funkcijas
GETEU()
GETNOTEU()
f.close()
#is txt failo irasytus duomenis perdedam i emaila
c = open("lentele.txt","r") 

gmail_user = 'email@gmail.com'  
gmail_password = 'password'

sent_from = gmail_user  
to = ['towhom@gmail.com']  
subject = 'Work'  
body = c.read()

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

#bandom siusti emaila
try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
#gaudom klaidas
except Exception as s:  
    print ('Something went wrong...'+str(s))