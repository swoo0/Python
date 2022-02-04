class Animal:
    def __init__(self):
        self.myLife = 100
        self.myAge = 0
    
    def getAge(self):
        self.myAge += 1
        self.myLife -= 1
    

class Human(Animal):
    def __init__(self):
        super().__init__()
        # Animal.__init__(self)    
        self.skill_lang = 1
        
    def exp(self, mama):
        self.skill_lang += mama

if __name__ == '__main__':
    hum = Human()
    
    print("hum", hum.myLife)
    print("hum", hum.myAge)
    print("hum", hum.skill_lang)
    
    hum.getAge()
    hum.exp(100)

    print("hum", hum.myLife)
    print("hum", hum.myAge)
    print("hum", hum.skill_lang)