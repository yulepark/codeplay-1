import matplotlib.pyplot as plt
import csv

f = open('pygame/yp_10.csv', 'r', encoding='utf8')
data = csv.reader(f)
yp_all = []
label_ages = ["0~9", "10~19", "20~29", "30~39", "40~49", "50~59", "60~69", "70~79", "80~89", "90~99", "100~"]

for i in data:
    yp_all.append(i)

print(len(yp_all), yp_all[10])

for da in range(len(yp_all)):
    for change in range(len(yp_all[da][3:])):
        if "," in yp_all[da][change + 3]:
            yp_all[da][change + 3] = int(yp_all[da][change + 3].replace(",", ""))
        else:
            yp_all[da][change + 3] = int(yp_all[da][change + 3])
    print(yp_all[da])

plt.pie(yp_all[10][3:], labels=label_ages, autopct="%.1f%%")
plt.show()

# for kkk in range(len(label_ages)):
#     print(f"{yp_all[10][10]} {label_ages[kkk]}세 인구 수 : {yp_all[10][kkk+3]}명")

# print(type(yp_all[0][3]))

# if "," in yp_all[0][3]:
#     yp_all[0][3] = int(yp_all[0][3].replace(",", ""))

# print(type(yp_all[0][3]))
