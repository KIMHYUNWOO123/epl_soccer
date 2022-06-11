import sqlite3
import paho.mqtt.client as mqtt
import threading
import gamedatabase

client = mqtt.Client()
con = sqlite3.connect("soccer.db")
cursor = con.cursor()
andorid_msg = ""
def mqtt_():
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        client.subscribe("android")

    def on_message(client, userdata, msg):
        global andorid_msg
        andorid_msg  = msg.payload.decode("utf-8")
        print(andorid_msg)
        
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("172.30.1.22")
    client.loop_forever()

t = threading.Thread(target=mqtt_)
t.start()

while(1):
    if(andorid_msg == "rank"):
        text = "SELECT team, point FROM EPL ORDER BY POINT DESC"
        fetched_table = gamedatabase.execute_fetch(text)
        rank = ""
        for t in fetched_table:
            # team = "," + team + str(t[0]) 
            # point = "," + point +str(t[1]) 
            rank = rank + f"{t[0]},{t[1]},"
        andorid_msg = ""
        client.publish("game", "rank,"+rank)
        print(rank)
    if(andorid_msg == "play"):
        text = "SELECT game FROM EPL WHERE team = 'Tottenham' "
        fetched_table = gamedatabase.execute_fetch(text)
        for record in fetched_table:
            game_num = record[0]
        if game_num == 10:
            print("리그 종료")
            team_ = ""
            team_ = gamedatabase.winner()
            text = "SELECT name FROM player ORDER BY goal DESC"
            fetched_table = gamedatabase.execute_fetch(text)
            text = "SELECT goal FROM player ORDER BY goal DESC"
            goal = gamedatabase.execute_fetch(text)
            team_ = team_ + f",{fetched_table[0][0]},{goal[0][0]}"
            client.publish("game", "winner," + team_)
            gamedatabase.end_of_season()
        if game_num <= 9:
            team = f"game,{game_num}"
            for i in range(0,6,2):
                print("------------------------")
                stat1 = gamedatabase.num_trans_stat(gamedatabase.game[game_num][i])
                stat2 = gamedatabase.num_trans_stat(gamedatabase.game[game_num][i+1])
                team1 = gamedatabase.num_trans_team(gamedatabase.game[game_num][i])
                team2 = gamedatabase.num_trans_team(gamedatabase.game[game_num][i+1])
                goal1 = gamedatabase.rand_goal(stat1)
                goal2 = gamedatabase.rand_goal(stat2)
                if goal1 > goal2:
                    gamedatabase.win(gamedatabase.game[game_num][i])
                    gamedatabase.defeat(gamedatabase.game[game_num][i+1]) 
                    team = team + f",{team1} {goal1} vs {goal2} {team2}  ({team1} Win)"
                if goal1 == goal2:
                    gamedatabase.draw(gamedatabase.game[game_num][i])
                    gamedatabase.draw(gamedatabase.game[game_num][i+1])
                    team = team + f",{team1} {goal1} vs {goal2} {team2}  (Draw)"
                if goal1 < goal2:
                    gamedatabase.defeat(gamedatabase.game[game_num][i])
                    gamedatabase.win(gamedatabase.game[game_num][i+1])
                    team = team + f",{team1} {goal1} vs {goal2} {team2}  ({team2} win)"
                gamedatabase.goal_for(team1, goal1)
                gamedatabase.goal_for(team2, goal2)
                gamedatabase.goal_against(team1, goal2)
                gamedatabase.goal_against(team2, goal1)
                gamedatabase.goal_diffefence(team1)
                gamedatabase.goal_diffefence(team2)
                sqc = ">>>"
                gamedatabase.goal_player(sqc,team1,goal1)
                sqc = "<<<"
                gamedatabase.goal_player(sqc,team2,goal2)
            client.publish("game", team)
            print(team)
        andorid_msg = ""


