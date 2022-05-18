from socket import gaierror
import sqlite3
from turtle import position

from sympy import print_rcode

from database import end_of_season

con = sqlite3.connect("soccer.db")
cursor = con.cursor()
cursor.execute("""SELECT goal FROM player ORDER BY goal DESC""")
table = cursor.fetchall()
print(table[0][0])

con.commit()
cursor.close()
con.close()
