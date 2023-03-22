class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        print(f'''안녕하세요 저는 {self.name}입니다. 저는 {self.age}살이구 제 키는 {self.height}cm입니다.''')

    def yell(self):
        print('아?')

class Developer(Person):
    keyboard = '기계식'
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def yell(self):
        print('어?')

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

    def introduce(self):
        print(f'''안녕하세요 저는 {self.name}입니다. 저는 {self.age}살이구 제 키는 {self.height}cm입니다. 저는 {self.disease}병을 앓고 있어요..''')

class ProductManger(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def yell(self):
        print('개발자님 여기 오류있어요')
    def aging(self):
        self.age +=2
        self.height -= 5
        print('개발자를 새로 뽑아야하나..')
        Developer.keyboard = '멤브레인'

d1 = Developer('유개발', 27, 180)
d2 = Designer('유아이', 23, 176, '허리디스크')
p1 = ProductManger('유기획', 25, 181)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()
print(d1.keyboard)
