# REQUIREMENTS FOR PROJECT

Flask == 0.12.2

Python == 2.7.6

Python == 3.4.3 

SQLite == 3.8.2 

beautifulsoup4

# STRUCTURE TO BE FOLLOWED



 **BMTC-Project->Templates**->bmtc.html
                             
      ->bmtc.db
                             
      ->busroute.py
      
      ->busfare.py
      
      ->busroutedb.py
      
      ->busfaredb.py
      
      ->ER-route.pdf
      
      ->ER-fare.pdf
      
      ->farescrap_10Nov2017.json
      
      ->routescrap_10Nov2017.json
      
      ->program.py
   
# **BUILD INSTRUCTIONS**
clone the project:- using **git clone https://github.com/kanchan-goel/BMTC-Project/ **
1. To fetch, parse the bus stops and timings, and store them in json file and database, run busroute.py using **python3 busroute.py** [input example: bus_no could be: 217 and route_no could be 3F]
2. To fetch, parse the fares list, and store them in json file and database, run fbusare.py using **python3 busfare.py**
[valid input types are: Ac and General]
3. To fetch the data from database, run busroutedb.py and busfaredb.py, using **python3 busroutedb.py** and **python3 busfaredb.py**, respectively.
4. To represent the data on the webpage, run app.py using **python program.py**. Go to browser and run http://127.0.0.1:5000/
Then, enter bus_no=217 and route_no=3F(for example) and whoosh! the data is visible on the webpage!!!
**P.S.:- for data to be visible, it must be in the db, and insert query is in busroute.py, so, before running program.py, run busroute.py**


    
    
