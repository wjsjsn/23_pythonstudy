'''
    클래스 안에는 상태값과 기능이 존재
    상태값 : 변수, 상수
    기능 : 메서드
'''

class Person:
    name = '홍길동'
    age = 24
    score = 176.8

    def setPerson(self, name, age, score): # self : java에서 this, 생략 x
        self.name = name
        self.age = age
        self.score = score

    # 출력하는 함수
    def viewPerson(self):
        print('이름 : ', self.name)
        print('나이 : ', self.age)
        print('점수 : ', self.score)

# 클래스를 객체로 만들어야 사용 가능
if __name__ == '__main__':
    ps = Person()
    print(ps)
    print(ps.name, ',', ps.age, ',', ps.score)
    ps.viewPerson()
    print('*' * 30)

    ps.setPerson('임꺽정', 39, 196.2)
    print(ps.name, ',', ps.age, ',', ps.score)
    ps.viewPerson()
    print('*' * 30)
