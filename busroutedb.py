import sqlite3
conn = sqlite3.connect("bmtc.db")
c = conn.cursor()

c.execute("SELECT * FROM busroutes")
data = c.fetchall()
print("bus_no, route_no, timing, stop")
for row in data:
    print(row)

conn.commit()

c.close()
conn.close()
