def samhaengsi(words):
    poem = []
    word_in = ""
    for word in words:
        print(f"{word} - ")
        while True:
            word_in = input("제시어로 시작하는 한줄 쓰기 =>")
            if word == word_in[0]:
                poem.append(word_in)
                break
            else:
                print("제시어 입력이 틀림. 다시하세요")

    for i in range(3):
        print(f"{words[i]} : {poem[i]}")

samhaengsi(input("삼행시 지을 글자를 넣어라 : "))