def guguDan():
    for dan in range(2, 9+1):
        for i in range(1, 9+1):
            print("{} * {} = {}".format(dan, i, dan*i))
            
guguDan()