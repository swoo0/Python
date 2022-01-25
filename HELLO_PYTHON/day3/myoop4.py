class Xi:
    def __init__(self):
        self.welth = 10
    
    def myexport(self, quantity):
        self.welth += quantity
    
    def myimport(self, quantity):
        self.welth -= quantity
        
    def hanhanyoug(self):
        print("못가져가")
        
class Baiden:
    def __init__(self):
        self.millitary_power = 10
    
    def makePower(self):
        self.millitary_power += 1
    
class TaeHyoung(Xi, Baiden):
    # def __init__(self):
        # super(TaeHyoung, self).__init__()
    def __init__(self):
        Xi.__init__(self)
        Baiden.__init__(self)
        
    def cry(self):
        print("응애")

if __name__ == '__main__':
    th = TaeHyoung()
    
    print("th welth", th.welth)
    print("th power", th.millitary_power)
    th.cry()

    th.myexport(1)
    th.makePower()
    
    print("th welth", th.welth)
    print("th power", th.millitary_power)
    th.cry()