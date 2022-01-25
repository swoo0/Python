a = input("첫 수를 적으세요")
b = input("둘째 수를 적으세요")

aa = int(a)
bb = int(b)


arr = range(aa, bb+1)

sum = 0

for i in arr:
    sum += i
    
print(f"{a}에서 {b}까지 합은 {sum} 입니다.")
# print("{}에서 {}까지 합은 {} 입니다.".format(aa, bb, sum))
