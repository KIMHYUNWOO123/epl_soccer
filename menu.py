#메뉴선택하면 수행해주는 함수
import database
def print_menu():
    print("-"*20)
    print("경기관리 선수관리")
    print("-"*20)
    select = input(">>>")
    if(select == "선수관리"):
        print()
        print()
        print("-"*20)
        print("추가  삭제  선수조회")
        print("-"*20)
        value = input(">>>")
        
    if(select == "경기관리"): 
        print()
        print()
        print("*"*25)
        print("경기시작 순위보기")
        print("*"*25)
        value = input(">>>")
    return value


def select_menu(value):

    if(value == "추가"):
        print("추가 할 선수의 이름, 팀, 포지션, 연봉, 스택을 입력하세요")
        value = input(">>>")
        database.add_player(value)
        

    if(value == "삭제"):
        print("삭제 할 선수의 이름을 적어주세요")
        value = input(">>>")
        database.delete_player(value)

    if value == "순위보기":
        database.rank_show()

    if value == "선수조회":
        print("조회 할 선수의 이름을 적어주세요")
        value = input(">>>")
        value = value.capitalize()
        database.player_show(value)


