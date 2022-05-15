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
    value = value[0]
    value = value[1:-1]
    print(f"{value} 선수가 삭제 되었습니다.")
    


  

