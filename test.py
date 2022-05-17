# import sqlite3
import random

from database import end_of_season


# con = sqlite3.connect("soccer.db")
# cursor = con.cursor()
# # cursor.execute(f"""INSERT INTO player
# #                 VALUES("Kepa" ,"Chelsea" , "GK" , 22000, 91)""")
# # cursor.execute(f"""INSERT INTO player
# #                 VALUES("Lukaku","Chelsea", "FW", 25000, 96)""")
# # cursor.execute(f"""INSERT INTO player
# #                 VALUES("Silva" , "Chelsea" ,"DF" , 24000, 93)""")
# # cursor.execute(f"""INSERT INTO player
# #                 VALUES("Kante" , "Chelsea" , "MF", 28000, 98)""")
# # cursor.execute(f"""INSERT INTO player
# #                 VALUES("Jorginho" , "Chelsea" , "MF" ,23000, 92 )""")
# cursor.execute("""UPDATE EPL SET num = 6 WHERE team = 'Chelsea' """)
# con.commit()
# cursor.close()
# con.close()

end_of_season()