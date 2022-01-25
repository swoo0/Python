import random

user = ""
com = ""
result = ""

user = input("홀/짝을 고르시오")

result = random.random()*2

print(result)

if result < 1.5:
    com = "홀"
else:
    com = "짝"

if user == com:
    result = "승리!"
else:
    result = "패배!"


print(f"user : {user}")
print(f"com : {com}")
print("결과:",result)