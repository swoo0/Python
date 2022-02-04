import random

user = ""
com = ""
result = ""

arr = ["가위", "바위", "보" ]


user = input("가위 바위 보를 선택하세요")

rnd = int(random.random()*3)
com = arr[rnd]

# if (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "바위") :
#         result = "유저 승리 !"
# elif (user == "가위" and com == "바위") or (user == "바위" and com == "보") or (user == "보" and com == "가위") :
#         result = "유저 패배 !!!"
# else :
#     result = "무승부!"
   
   
if com == "가위" and user == "가위" :   result = "비김"  
if com == "가위" and user == "바위" :   result = "이김"  
if com == "가위" and user == "보"   :   result = "짐"  
   
if com == "바위" and user == "가위" :   result = "짐"  
if com == "바위" and user == "바위" :   result = "비김"  
if com == "바위" and user == "보"   :   result = "이김"  
   
if com == "보"   and user == "가위" :   result = "이김"  
if com == "보"   and user == "바위" :   result = "짐"  
if com == "보"   and user == "보"   :   result = "비김"  


print("유저 : ", user)
print("컴 : ", com)
print(result)