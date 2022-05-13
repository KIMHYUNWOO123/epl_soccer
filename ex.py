from lib2to3.pgen2.token import NAME
import sqlite3

con = sqlite3.connect("soccer.db")
cursor = con.cursor()

cursor.execute("DROP TABLE IF EXISTS player")
cursor.execute("""CREATE TABLE player
                (name CHAR(16) PRIMARY KEY,
                country CHAR(16),
                team CHAR(20),
                age  INT(2),
                height INT(3) ,
                position CHAR(16),
                income INT(16))""")
con.commit()
cursor.close()
con.close()