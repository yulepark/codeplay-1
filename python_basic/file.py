'''
open명령어는 외부에 파일을 만들거나 읽고 쓸 수 있는 객체를 생성하는 클래스.
파일명을 적으면, 없던 파일은 새로 생성하고, 있는 파일은 그 파일을 다시 가져온다.
w = write(쓰기) / a = add(내용추가) / r = read(내용읽기) 세가지 모드를 가진다.
'''
f = open("test.txt", "a", encoding = "UTF-8")
f.write("피자 8분전"+ "\n") #개행문자
f.write("콜라는 없다"+ "\n")
f.close()
words = []
for i in f.readlines():
    words.append(i.strip())
print(words)
f.close()