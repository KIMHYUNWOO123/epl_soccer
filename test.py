
import sqlite3

from database import end_of_season

con = sqlite3.connect("soccer.db")
cursor = con.cursor()
# cursor.execute("""SELECT GF,GA FROM EPL WHERE team = 'Tottenham' """)
# table = cursor.fetchall()
# print(table[0][0],table[0][1])
end_of_season()
con.commit()
cursor.close()
con.close()
