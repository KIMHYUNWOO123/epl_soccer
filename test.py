import sqlite3

con = sqlite3.connect("soccer.db")
cursor = con.cursor()
# cursor.execute(f"""INSERT INTO player
#                 VALUES("Kepa" ,"Chelsea" , "GK" , 22000, 91)""")
# cursor.execute(f"""INSERT INTO player
#                 VALUES("Lukaku","Chelsea", "FW", 25000, 96)""")
# cursor.execute(f"""INSERT INTO player
#                 VALUES("Silva" , "Chelsea" ,"DF" , 24000, 93)""")
# cursor.execute(f"""INSERT INTO player
#                 VALUES("Kante" , "Chelsea" , "MF", 28000, 98)""")
# cursor.execute(f"""INSERT INTO player
#                 VALUES("Jorginho" , "Chelsea" , "MF" ,23000, 92 )""")
cursor.execute("""UPDATE player
                SET income = "22000", stat = 93
                WHERE name = "Dier" """)
con.commit()
cursor.close()
con.close()

