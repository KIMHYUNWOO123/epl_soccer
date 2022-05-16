#데이터 베이스 관리해주는 함수
import sqlite3

def add_player(value):
    con = sqlite3.connect("soccer.db")
    cursor = con.cursor()
    cursor.execute(f"""INSERT INTO player
                        VALUES ({value})""")
    con.commit()
    cursor.close()
    con.close()
    value = value.split(",")
    value = value[0]
    value = value[1:-1]
    print(f"{value} 선수가 추가 되었습니다.")

def delete_player(value):
    print(value)
    con = sqlite3.connect("soccer.db")
    cursor = con.cursor()
    cursor.execute(f"""DELETE 
                        FROM player
                        WHERE name ='{value}'""")
    con.commit()
    cursor.close()
    con.close()
    value = value.split(",")
    print(f"{value[0]} 선수가 삭제 되었습니다.")

def rank_show():
    con = sqlite3.connect("soccer.db")
    cursor = con.cursor()
    cursor.execute("""SELECT *
                    FROM EPL
                    ORDER BY POINT ASC""")
    table = cursor.fetchall()
    no = 1
    for record in table:
        print(f"{no}위 승점: {record[2]}점 - {record[0]}")
        no += 1
    con.commit()
    cursor.close()
    con.close()

def player_show(value):
    con = sqlite3.connect("soccer.db")
    cursor = con.cursor()
    cursor.execute(f"""SELECT *
                    FROM player
                    WHERE name = "{value}" """)
    table = cursor.fetchall()
    for record in table:
        print(f"이름:{record[0]} 팀:{record[1]} 포지션:{record[2]} 연봉:{record[3]} 능력치:{record[4]}")
    con.commit()
    cursor.close()
    con.close()

def play_game():
    pass
  

