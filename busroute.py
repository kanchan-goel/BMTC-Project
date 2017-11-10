from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import time
import os

  
con = sqlite3.connect("bmtc.db")
f = con.cursor()

f.execute('CREATE TABLE IF NOT EXISTS busroutes(bus_no TEXT , route_no TEXT, timing TEXT, stop TEXT, PRIMARY KEY (bus_no, route_no))'   )

    
    
print("Enter bus number")
bus=input()
print("Enter route number")
route=input()

    
    

url1="https://www.mybmtc.com/route/busstops/"+bus+"/print/"+route
req1=requests.get(url1)
data1 =req1.text
soup=BeautifulSoup(data1,"html.parser")
stop=([i.text for i in soup.find_all('span',{'id':'busstop_name'})])

url2="https://www.mybmtc.com/route/schedule/"+bus
req2=requests.get(url2)
data2 =req2.text
soup=BeautifulSoup(data2,"html.parser")
timing=[litag.text for ultag in soup.find_all('ul', {'class': 'routestime'}) for litag in ultag.find_all('li')] 

    
    

data={"bus_no":bus,
      "route_no":route,
      "timing":timing,
      "stop":stop
     }

timing = ','.join(map(str, timing)) 
stop = ','.join(map(str, stop)) 

f.execute("INSERT INTO busroutes (bus_no, route_no, timing, stop) values (? , ? , ? , ?)",(bus, route, timing, stop) )

   
    
time.ctime()
timestr = time.strftime("%d%b%Y")
route="routescrap_"+timestr

with open(route+".json", 'w') as outfile:
    json.dump(data, outfile)
    

con.commit()

f.close()
con.close()


