from flask import Flask, render_template, request
import sqlite3 

def retrieve(busno,routeno):
    con = sqlite3.connect("bmtc.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM busroutes where bus_no=? and route_no=?",(busno,routeno))
    users = cur.fetchall()
    con.close()
    return users

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method=='POST':
        busno = request.form['bus_no']
        routeno = request.form['route_no']	
   	users = retrieve(busno,routeno)
	return render_template('bmtc.html', users=users)
    else:
        return render_template('bmtc.html')

if __name__ == "__main__":
    program.run()
