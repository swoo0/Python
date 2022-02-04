import threading

def showNum():
    for i in range(55204) :
        print(i,end="")
        if i % 100 == 0:
            print()

def showAscii():
    for i in range(55204) :
        print(chr(i),end="")
        if i % 100 == 0:
            print()

# print(ord("힣"))
th = threading.Thread(target=showNum)
th2 = threading.Thread(target=showAscii)
th.start()
th2.start()
# th.join()
# th2.join()