a = input("첫 수를 적으세요")

b = input("둘째 수를 적으세요")

c = input("배수를 적으세요")

aa = int(a)
bb = int(b)
cc = int(c)

# arr = range(aa, bb+1)

sum = 0
for i in range(aa, bb+1):
    if i % cc == 0 :
        sum += i

print(f"{a}에서 {b}까지 {c}배수의 합은 {sum} 입니다.")
print("{}에서 {}까지 {}배수의 합은 {} 입니다.".format(aa, bb, cc, sum))