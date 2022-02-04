class Animal:
    def __init__(self, myAge):
        print("생성자", myAge)
        self.myLife = 100
        self.myAge = myAge
    
    def getAge(self):
        self.myAge += 1
        self.myLife -= 1
    
    def __del__(self):
        print("소멸자", self.myAge)

print("myoop", __name__)

if __name__ == '__main__':
    ani = Animal(5)

