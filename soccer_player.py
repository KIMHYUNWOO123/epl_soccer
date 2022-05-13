import sqlite3
class Soccer_player:
    def __init__(self, name,  country, team, age, height, position, income):
        self.name = name
        self.country = country
        self.age = age
        self.team = team
        self.height = height
        self.postion = position
        self.income = income

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
        

        con.execute(f"""INSERT INTO player VALUES ('{self.name}','{self.country}','{self.team}', '{self.age}', '{self.height}','{self.postion}','{self.income}')""")
        con.commit()
        cursor.close()
        con.close()
