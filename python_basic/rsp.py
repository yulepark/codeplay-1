import random

user = 0

com = 0

computer = ["가위", "바위", "보"]

running = True

user = input("무엇을 낼꺼니? (가위, 바위, 보 중 선택)")

com = computer[random.randint(0,2)]

print(f"컴 : {com} / 유저 : {user}")

if computer == user :
    print("비김")
else: 
    if user == "가위":
        if computer == "보":
            print("너가 이겼어")
        else:
            print("너가 졌어")
    if user == "바위":
        if computer == "보":
            print("너가 졌어")
        else:
            print("너가 이겼어")
    if user == "보":
        if computer == "가위":
            print("너가 졌어")
        else:
            print("너가 이겼어")