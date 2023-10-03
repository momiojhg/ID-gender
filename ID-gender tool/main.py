import numpy as np
import pandas as pd


gender = pd.read_excel(io=r"C:\Users\lusicheng\Desktop\副本1_附件1：上海赛区第十五届全国大学生数学竞赛报名信息表.xlsx", sheet_name=3, header=0, usecols="C", skiprows=1)
gender = np.array(gender)
gender.tolist()
gender_1 = []
for i in gender:
    gender_1.append(i[0])
print(gender_1)

card = pd.read_excel(io=r"C:\Users\lusicheng\Desktop\副本1_附件1：上海赛区第十五届全国大学生数学竞赛报名信息表.xlsx", sheet_name=3, header=0, usecols="E", skiprows=1)
card = np.array(card)
card.tolist()
numb = []
for i in card:
    numb.append(int(i[0][16]))
print(numb)
for i in range(len(card)):
    if (numb[i] % 2 == 0 and gender[i] != "女"):
        print("error")
    elif (numb[i] % 2 == 1 and gender[i] != "男"):
        print("error")
    else :
        continue