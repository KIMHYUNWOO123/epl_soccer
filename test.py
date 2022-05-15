import sqlite3

con = sqlite3.connect("soccer.db")
cursor = con.cursor()
# cursor.execute(f"""CREATE TABLE EPL(
#             team CHAR(20) PRIMARY KEY,
#             game INT(4),
#             point INT(4),
#             win INT(4),
#             draw INT(4),
#             defeat INT(4))""")
cursor.execute("""INSERT INTO EPL
                VALUES ("Arsenal","0","0","0","0","0") """)
con.commit()
cursor.close()
con.close()
