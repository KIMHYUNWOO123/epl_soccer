import random
import sqlite3
#con = sqlite3.connect("soccer.db")
#cursor = con.cursor()
#cursor.execute("""SELECT name,stat,team FROM player WHERE team = 'Tottenham' """)
#table = cursor.fetchall()
#for i in table:
#    print(i[1])
#con.commit()
#cursor.close()
#con.close()
num = random.randint(0,400)
for i in range(5):
    num = random.randint(0,400)
    print(num)