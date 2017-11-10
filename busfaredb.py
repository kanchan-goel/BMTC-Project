import sqlite3
conn = sqlite3.connect("bmtc.db")
c = conn.cursor()

c.execute("SELECT * FROM fares")
data = c.fetchall()
print("Stage, Adults, Child, Senior_Citizen")
for row in data:
    print(row)

conn.commit()

c.close()
conn.close()
