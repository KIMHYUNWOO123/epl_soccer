#데이터 베이스 관리해주는 함수
import sqlite3
import numpy as np
import random
from pyparsing import restOfLine

from regex import D
game = np.zeros((10,6))
game = [[1, 2, 3, 4, 5, 6], [2, 6, 1, 3, 4, 5], [3, 6, 2, 5, 1, 4], [1, 6, 2, 4, 3, 5], [2, 3, 1, 5, 4, 6], 
        [6, 5, 4, 3, 2, 1], [5, 4, 6, 2, 3, 1], [5, 2, 4, 1, 6, 3], [5, 3, 4, 2, 6, 1], [5, 1, 6, 4, 3, 2]]

def execute_nofetch(text):
    con = sqlite3.connect("soccer.db")
    cursor = con.cursor()
    cursor.execute(f"""{text}""")
    con.commit()
    cursor.close()
    con.close()

def execute_fetch(text):
    con = sqlite3.connect("soccer.db")
    cursor = con.cursor()
    cursor.execute(f"""{text}""")
    table = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return table


def add_player(value):
    text = f"INSERT INTO player VALUES ({value})"
    execute_nofetch(text)
    value = value.split(",")
    value = value[0]
    value = value[1:-1]
    print(f"{value} 선수가 추가 되었습니다.")

def delete_player(value):
    text = f"DELETE FROM player WHERE name ='{value}'"
    execute_nofetch(text)
    value = value.split(",")
    print(f"{value[0]} 선수가 삭제 되었습니다.")

def rank_show():
    text = "SELECT * FROM EPL ORDER BY POINT DESC"
    fetched_table = execute_fetch(text)
    no = 1
    for record in fetched_table:
        print(f"{no}위 승점: {record[2]}점 - {record[0]}")
        no += 1
        

def player_show(value):
    text = f"SELECT * FROM player WHERE name = '{value}' "
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        print(f"이름:{record[0]} 팀:{record[1]} 포지션:{record[2]} 연봉:{record[3]} 능력치:{record[4]}")


def play_game():
    text = "SELECT game FROM EPL WHERE team = 'Tottenham' "
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        game_num = record[0]
    if game_num == 10:
        print("리그 종료")
        team = winner()
        print(f"우승팀은 ***{team}*** ")
        rank_show()
        end_of_season()
        return 0
    print(f"{game_num+1}번째 경기 결과")
    for i in range(0,6,2):
        stat1 = num_trans_stat(game[game_num][i])
        stat2 = num_trans_stat(game[game_num][i+1])
        team1 = num_trans_team(game[game_num][i])
        team2 = num_trans_team(game[game_num][i+1])
        goal1 = rand_goal(stat1)
        goal2 = rand_goal(stat2)
        if goal1 > goal2:
            win(game[game_num][i])
            defeat(game[game_num][i+1]) 
            print(f"{team1} {goal1} vs {goal2} {team2}  ({team1} Win) ") 
        if goal1 == goal2:
            draw(game[game_num][i])
            draw(game[game_num][i+1])
            print(f"{team1} {goal1} vs {goal2} {team2}  (Draw) ") 
        if goal1 < goal2:
            defeat(game[game_num][i])
            win(game[game_num][i+1])
            print(f"{team1} {goal1} vs {goal2} {team2}  ({team2} win) ") 

def winner():
    text = "SELECT * FROM EPL ORDER BY point DESC"
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        return record[0]
def end_of_season():
    for i in range(1,7):
        text = f"UPDATE EPL SET game = 0, point = 0, win = 0, draw = 0, defeat = 0 WHERE num = {i}"
        execute_nofetch(text)

def win(num):
    text = f"UPDATE EPL SET win = win + 1, point =  point + 3, game =  game + 1 WHERE num = {num}"
    execute_nofetch(text)

def draw(num):
    text = f"UPDATE EPL SET draw = draw + 1, point = point + 1, game = game + 1 WHERE num = {num}"
    execute_nofetch(text)

def defeat(num):
    text = f"UPDATE EPL SET defeat = defeat + 1, game = game + 1 WHERE num = {num}"
    execute_nofetch(text)

def num_trans_stat(num):
    team = num_trans_team(num)
    text = f"SELECT AVG(stat) FROM player WHERE team = '{team}' "
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        return record[0]

def num_trans_team(num):
    text = f"SELECT team FROM EPL WHERE num = '{num}'"
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        return record[0]

def rand_goal(stat):
    stat = int(stat)
    goal = 0
    for i in range(5):
        if 0 <= random.randint(0,300) <= stat:
            goal += 1
    return goal     

def team_show(value):
    text = f"SELECT * FROM player WHERE team = '{value}' ORDER BY position ASC "
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        print(f"{record[2]} - {record[0]} ")

def team_avg_stat(value):
    text = f"SELECT AVG(stat) FROM player WHERE team = '{value}' "
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        print (f"팀스탯:{record[0]}")
def team_sum_income(value):
    text = f"SELECT SUM(income) FROM player WHERE team = '{value}' "
    fetched_table = execute_fetch(text)
    for record in fetched_table:
        print (f"구단운영비:{record[0]}만원")

