# 직업 데이터


job = {
    "knight" : {
        "name" : "기사",
        "hp" : 100,
        "np" : 100,
        "skil" : "slash",
        "skil_damage" : 30,
        "M1" : 20
    },
    "bowman" : {
        "name" : "궁수",
        "hp" : 80,
        "np" : 100,
        "skil" : "longshot",
        "skil_damage" : 40,
        "M1" : 15
    },
    "wizard" : {
        "name" : "마법사",
        "hp" : 65,
        "np" : 120,
        "skil" : "fireball",
        "skil_damage" : 50,
        "M1" : 20
    },
    "GOD" : {
        "name" : "개발자 모드",
        "hp" : 99999999999,
        "np" : 99999999999,
        "skill" : "GOD's slash",
        "skill_damage" : 999999999999999,
        "M1" : 999999999
    }
}

# 몹 데이터


enemy = {
    "goblin" : {
        "name" : "고블린",
        "hp" : 50,
        "np" : 0,
        "M1" : 10
    },

    "hopgoblin" : {
        "name" : "홉고블린",
        "hp" : 100,
        "np" : 50,
        "skil" : "smash",
        "skil_damage" : 40,
        "M1" : 30

    }
}


# 닉네임 정하기


while True : 
    nickname = input("닉네임을 입력해주세요")
    if nickname.isalnum():
        ac = input("정말 닉네임을" + nickname + "으로 정하겠습니까?\n Y/N")
        if ac == "Y":
            print("닉네임 설정이 완료되었습니다!")
            break
        elif ac == "N":
            continue
        else : 
            print("올바른 선택지를 입력해주세요")



# 직업 정하기


while True :
    player = input("멋진 이름이 생겼으니 직업을 선택해보죠! 어떤 직업을 선택하시겠습니까?\n (knight,bowman,wizard)")

    if player in job :
        pla = input("정말 이 직업을 선택하시겠습니까? \n Y/N")
        if pla == "Y":
            print("탁월한 선택이시군요!",nickname,"님 당신의 직업은",player,"입니다!")
            break
        elif pla == "N":
            continue
        else :
            print("올바른 선택지를 골라주세요!")


# 전투 시작 ( 기습 이벤트 )


def start(player,enemy):

        choice = input("적" + enemy["name"] + "과 마주했다\n 1.공격한다\n2.기습한다\n선택 : ")
        if choice == "1" :
            enemy["hp"] -= job[player]["M1"]
            if enemy["hp"] <= 0 :
                print("승리했다!")
            else :
                print(enemy["name"],"의 HP는", enemy["hp"],"가 되었다!")
        elif choice == "2" :
            if enemy["hp"] >= 0:
                enemy["hp"] -= job[player]["M1"] * 2
                print(enemy["name"],"의 HP는", enemy["hp"],"가 되었다!")
            else :
                print("승리했다!")
            
        else :
            print("올바른 선택지를 입력해주세요\n")
        


# 잡몹 기습 전투 구현


def battle(player,enemy):
    start(player,enemy)
    if enemy["hp"] <= 0:
        exit()
    while True:

        choice2 = input("1.공격한다\n2.스킬을 사용한다\n선택 : ")

        if choice2 == "1":
            enemy["hp"] -= job[player]["M1"]
            print(enemy["name"],"의 HP는", enemy["hp"],"가 되었다!")

            if enemy["hp"] <= 0:
                print(enemy["name"],"이 쓰러졌다.\n승리했다!")
                break

            else :
                job[player]["hp"] -= enemy["M1"]
                print("고블린의 반격이 날라왔다.",nickname,"의 hp는",player["hp"],"가 되었다")

        elif choice2 == "2":
            enemy["hp"] -= job[player]["skil_damage"]
            print(enemy["name"],"의 HP는", enemy["hp"],"가 되었다!")

            if enemy["hp"] <= 0:
                print(enemy["name"],"이 쓰러졌다.\n승리했다!")
                break

            else :
                job[player]["hp"] -= enemy["M1"]
                print("고블린의 반격이 날라왔다.",nickname,"의 hp는",player["hp"],"가 되었다")

        else :
            print("올바른 선택지를 입력해주세요")
            continue


# Test


battle(player,enemy["goblin"])