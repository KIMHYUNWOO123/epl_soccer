#메뉴선택하면 수행해주는 함수
import gamedatabase
def print_menu():
    print("-"*30)
    print("경기관리 팀관리 선수관리")
    print("-"*30)
    select = input(">>>")
    if(select == "선수관리"):
        print()
        print()
        print("-"*30)
        print("추가  삭제  선수조회 득점순위")
        print("-"*30)
        value = input(">>>")
    if select == "팀관리":
        print()
        print()
        print("#"*30)
        print("소속선수  팀스탯  구단운영비")
        print("#"*30)
        value = input(">>>")
    if(select == "경기관리"): 
        print()
        print()
        print("*"*25)
        print("경기시작 순위보기 역대우승")
        print("*"*25)
        value = input(">>>")
    return value


def select_menu(value):

    if(value == "추가"):
        print("추가 할 선수의 이름, 팀, 포지션, 연봉, 스택을 입력하세요")
        value = input(">>>")
        gamedatabase.add_player(value)
        

    if(value == "삭제"):
        print("삭제 할 선수의 이름을 적어주세요")
        value = input(">>>")
        gamedatabase.delete_player(value)

    if value == "순위보기":
        gamedatabase.rank_show()

    if value == "선수조회":
        print("조회 할 선수의 이름을 적어주세요")
        value = input(">>>")
        gamedatabase.player_show(value)

    if value == "소속선수":
        print("조회 할 팀 명을 적어주세요")
        value = input(">>>")
        gamedatabase.team_show(value)
    
    if value == "팀스탯":
        print("조회 할 팀 명을 적어주세요")
        value = input(">>>")
        gamedatabase.team_avg_stat(value)

    if value == "구단운영비":
        print("조회 할 팀 명을 적어주세요")
        value = input(">>>")
        gamedatabase.team_sum_income(value)
    if value == "경기시작":
        gamedatabase.play_game()

    if value == "역대우승":
        gamedatabase.win_career()

    if value == "득점순위":
        gamedatabase.goal_rank()

