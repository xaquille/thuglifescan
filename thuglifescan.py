from bs4 import BeautifulSoup
import datetime
import os
import requests
import string
import json
import pyfiglet
import mysql.connector

#Database Connected
db = mysql.connector.connect(
    host="localhost",
    user="userDb",
    passwd="PassDb",
    database="nmap_report"
)
if db.is_connected():
    print("db connect bro")

#Banner
ascii_banner = pyfiglet.figlet_format("ThugLifeScan")
print ("#" * 60)
print(ascii_banner)
print('\t\tnemosecurity.com')
print ("#" * 60)


def cok(str):
    return str.strip().encode('utf-8')

fuck = datetime.date.today()
os.system('tanggal=$(date +"%F") && nmap -sV -iL list_IP.txt -oX nmap_$tanggal.xml > asu.txt && xsltproc nmap_$tanggal.xml -o nmap_$tanggal.html')

report = 'nmap_'+str(fuck)+'.html'

soup = BeautifulSoup(open(str(report)),"html.parser")
div = soup.find_all('div', class_='unhidden')

for d in div:
    table = d.find("table")
    tr_attributes_open = table.find_all("tr", class_="open")

    ul_ip = d.find("ul")
    li_ip = str(ul_ip.find_all()).replace('[<li>','').replace('(ipv4)','').replace('</li>]','').replace('\\n','')
    

    print('\n')
    print ("-" * 60)
    print('\t\t'+li_ip.strip())
    print ("-" * 60)
    
    for tr in tr_attributes_open:
        td_attributes = tr.find_all("td")

        port = td_attributes[0].text
        port = port.strip()

        service = td_attributes[3].text
        service = service.strip()

        product = td_attributes[5].text
        product = product.strip()
        new_prod = product.replace('httpd','').replace('imapd','').replace('pop3d','').replace('smtpd','')

        version = td_attributes[6].text
        version = version.strip()
        version = version.replace('Ubuntu','').replace('4ubuntu0.3','').replace('4ubuntu2.8','')

        cursor = db.cursor()
        asu = """INSERT INTO nmap (ip, port, service, product, version) VALUES (%s, %s, %s, %s, %s)"""
        shit = (li_ip.strip(), port, service, new_prod, version)

        # for val in values:
        cursor.execute(asu, shit)
        db.commit()

        print("{} data ditambahkan".format(len(shit)))

        anjing=''

        if new_prod==anjing:
            # print('product isinya space doank!')
            pass
        else:
            if version==anjing:
                # print('Product and Version not detect')
                pass
            else:
                print ("*" * 60)
                # print('IP\t= '+li_ip.strip())
                print('port\t= ' + port)
                print('service\t= '+ service)
                print ('product\t= ' + new_prod)
                print ('version\t= ' + version)

                url = "https://www.exploit-db.com/search?q="
                antiBot = {
                    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0",
                    "Referer" : "https://www.exploit-db.com/search?q=",
                    "X-Requested-With" : "XMLHttpRequest"
                    }


                id_url = url + str(new_prod)+' '+str(version)
                print('Link\t= '+id_url)


                response = requests.get(id_url, headers=antiBot)
                online = response.content
                json_response = json.loads(online)
                print ("*" * 60)
                trecord = json_response["recordsTotal"]

                if trecord==0:
                    print("AMAN KOMANDAN!")
                    print('\n')
                else:
                    suck = json_response
                    for id in suck["data"]:
                        link_id = (id["id"])
                        link_db = "https://www.exploit-db.com/raw/"+str(link_id)
                        desc = (id["description"][1]).replace('&#039;', "'").replace('&lt;','<')

                        cursor = db.cursor()
                        sql = """INSERT INTO ip (ip_address, port, product, version, title, link) VALUES (%s, %s, %s, %s, %s, %s)"""
                        values = (li_ip.strip(), port, product, version, desc, link_db)

                        cursor.execute(sql, values)
                        db.commit()

                        print("{} data ditambahkan".format(len(values)))
                       
                    
                    print ("*" * 60)
                    print('\n')

os.system('tanggal=$(date +"%F") && rm nmap_$tanggal.xml && rm asu.txt')