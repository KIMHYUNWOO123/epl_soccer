import sqlite3
from turtle import position

con = sqlite3.connect("soccer.db")
cursor = con.cursor()
cursor.execute("""SELECT name, position, stat FROM player WHERE team = 'Tottenham' """)
table = cursor.fetchall()
player = ["", "", "", "", "", ""]
stat = [0,]

i = 0
for record in table:
    player[i] = record[0]
    stat[i] = record[2]
    if record[1] == "FW":
        stat[i] = int(stat[i]/10)
        stat[i] += 5
    if record[1] == "MF":
        stat[i] = int(stat[i]/10)
        stat[i] += 3
    if record[i] == "DF":
        stat[i] = int(stat[i]/10)
        stat[i] += 1
    if record[i] == "GK":
        stat[i] = 0
    
for chance in goal:
    
        
    i += 1
con.commit()
cursor.close()
con.close()


