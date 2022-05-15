import sqlite3
class Soccer_player:
    def __init__(self, name, team, position, income, stat):
        self.name = name
        self.team = team
        self.postion = position
        self.income = income
        self.stat = stat

    def injury(self):
        self.income -= 1000
    
    def mvp(self):
        self.income += 2000
    
    def transfer(self, team, income):
        self.team = team
        self.income = income

    def save_db(self):
        con = sqlite3.connect("soccer.db")
        cursor = con.cursor()
        
        cursor.execute("""DROP TABLE IF EXISTS player """)
        cursor.execute("""CREATE TABLE player (
                        name CHAR(16) PRIMARY KEY,
                        team CHAR(20),
                        position CHAR(16),
                        income INT(4),
                        stat INT(4))""")
        cursor.execute(f"""INSERT INTO player VALUES ('{self.name}','{self.team}','{self.postion}','{self.income}', '{self.stat}')""")
        con.commit()
        cursor.close()
        con.close()
