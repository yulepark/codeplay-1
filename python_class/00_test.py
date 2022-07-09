# -*- coding: utf-8 -*-
# 1. Data
#     - 변수
#     - 배열 / 자료형 : list, tuple, dictionary, set 등

# 2. 데이터 가공
#     - 조건문 if ~ else ~ 
#     - 조건 반복문 while ~
#     - 순회 반복문 for i in ~

# 3. 데이터 가공을 더 편하게
#     - 함수 def ~ (같은 코드 쓰기 귀찮으니까 코드를 정의하고 사용)
#     - 클래스 class ~ ()


# class 참치선물세트:
#     일반 = 0
#     야채 = 0
#     고추 = 0
    
    
#     def 총합(self, 이름):
#         내용물갯수 = self.일반 + self.야채 + self.고추
#         return 이름 + str(내용물갯수)
    
#     def 출력(self):
#         self.총합("담긴 참치 갯수 : ")


# 참치3호세트 = 참치선물세트() #참치 3호세트는 변수의 형태지만 인스턴스라고 부른다.

# 참치3호세트.일반 = 12
# 참치3호세트.야채 = 3
# 참치3호세트.고추 = 3

# 참치갯수 = 참치3호세트.총합("담긴 참치 갯수 :")

# print(참치갯수)


class 참치선물세트():
    def __init__(self, 일반, 야채, 고추):
        self.일반 = 일반
        self.야채 = 야채
        self.고추 = 고추
    
    def 내용물보기(self, name):
        print(name)
        print("일반참치 : " + str(self.일반))
        print("야채참치 : ", + str(self.야채))
        print("고추참치 : " + str(self.고추))

참치1호 = 참치선물세트( 10 ,3, 2)
참치1호.내용물보기("참치 1호 내용물 안내")
    


class Units:
    hp = 0
    damage = 0
    speed = 0

timo = Units()
timo.hp = 10
timo.damage = 100
timo.speed = 50

yasuo = Units()
yasuo.hp = 5
yasuo.damage = 1000
yasuo.speed = 100

print("티모 - 체력 {} | 공격력 : {} | 이속 : {}" .format(timo.hp, timo.damage, timo.speed))
