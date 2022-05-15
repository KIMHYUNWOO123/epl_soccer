#메뉴선택하면 수행해주는 함수
import database
def print_menu():
    print("-"*20)
    print("추가  삭제  수정")
    print("-"*20)
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

