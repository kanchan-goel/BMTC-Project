from bs4 import BeautifulSoup
import requests
import os
import json
import sqlite3
import time


con = sqlite3.connect("bmtc.db")
f = con.cursor()

f.execute('CREATE TABLE IF NOT EXISTS fares(Stage INTEGER, Adults INTEGER, Child INTEGER, Senior_Citizen INTEGER)')

  
    

print("Enter fare type")
faretype=input()

if (faretype=='Ac'):
    url1="https://www.mybmtc.com/ac-service?fareid=acs&qt-home_quick_tab_bottom=2"
elif (faretype=='General'):
    url1="https://www.mybmtc.com/general-service?fareid=gns&qt-home_quick_tab_bottom=2"
else:
    print("Please enter valid fare type")
    os._exit(1)


data = []
req1=requests.get(url1)
data1 =req1.text
soup=BeautifulSoup(data1,"html.parser")
table=soup.find_all('table')[:2]
for i in table:
    sdata=[]
    rows = i.find_all('tr')[1:]

    for row in rows:
   
        cols = row.find_all('td')
        
       
       

        trow = {}
        trow["Fare Stage Number"]=cols[0].get_text()
        trow["Adults"]=cols[1].get_text()
        trow["Child"]=cols[2].get_text()
        try:
            trow["Senior Citizen"]=cols[3].get_text()
        except:
            trow["Senior Citizen"]="0"
        
        sdata.append(trow)
        
        f.execute("INSERT INTO fares (Stage, Adults, Child, Senior_Citizen) values (? , ? , ? , ?)", (trow["Fare Stage Number"],trow["Adults"],trow["Child"],trow["Senior Citizen"] )  )
        
            
    data.append(sdata)

time.ctime()
timestr = time.strftime("%d%b%Y")
fare="farescrap_"+timestr

with open(fare+'.json', 'w') as outfile:
    json.dump(data, outfile)

con.commit()

f.close()
con.close()

