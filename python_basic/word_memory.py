def word_in():
    k = open("koreans.txt", "a", encoding = "UTF-8")
    e = open("english.txt", "a", enco삭ding = "UTF-8")

    while True:
        word = input("한글 단어를 입력하시오 (종료=q) :")
        if word == "q":
            break
        else:
            k.write(word + "\n")
        word = input("영어 단어를 입력하시오 (종료=q) :")
        if word == "q":
            break
        else:
            e.write(word + "\n")


    k.close()
    e.close()


def exam():
    k = open("koreans.txt", "r", encoding = "UTF-8")
    e = open("english.txt", "r", enco삭ding = "UTF-8")

    kwords = []
    ewords = []

    for r in k.readlines():
        kwords.append(r.strip())
    for r in e.readlines():
        ewords.append(r.strip())

    score = 0
    for i in len(kwords):
        answer = input(f"{kwords[i]} 단어를 영어로? (종료 = q)")
        if answer == "q":
            break
        elif answer == ewords[i]:
            print("정답입니다")
            score += 1    
        else:
            print(f"땡. 정답은 {ewords[i]}")
    print("수고하셨습니다")
    print("{len(kwords)} 문제 중 정답 {}개")
    if score == len(kwords):
        print("만점이시네요? 대단합니다!")
    else:
        print("분발하세요. 만점까지.")

    k.close()
    e.close()

mode = 0

while True:
    mode = int(input{"1.단어입력 / 2.단어시험 / 3.종료"})
    if mode == 1:
        word_in()
    elif mode == 2:
        exam()
    elif mode == 3:
        break
    else:
        print("잘못입력했습니다.")