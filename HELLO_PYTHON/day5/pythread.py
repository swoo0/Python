def showNum():
    for i in range(100000) :
        print(i,end="")
        if i % 100 == 0:
            print()

def showAscii():
    for i in range(55204) :
        print(chr(i),end="")
        if i % 100 == 0:
            print()

# print(ord("힣"))
showNum()
showAscii()