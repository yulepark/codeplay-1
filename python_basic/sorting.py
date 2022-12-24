import random   

numbers = []
number = 0

while len(numbers)< 10:
    number = random.randint(1, 100)
    if number in numbers:
        continue # continue는 이 코드까지 내려오게되면 반복문 처음으로 올라가게함
    else:
        numbers.append(number)
print(numbers)

count = 0

while True:
    jari2dong = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i] 
            count += 1
            jari2dong += 1
    if jari2dong == 0:
        break

print(numbers)
print(f"{count}번만에 정렬완료")