
class Person:
    def __init__(self,name_param):  # self 는 알아서 자기 자신을 가져오기 위한 정보일 뿐. 굳이 파라미터로 넘기는거 X
        self.name= name_param

        print("hihi",self,self.name)


    def talk(self):
        print("안녕하세요 저는",self.name,"입니다")
person_1 = Person("유재석")
person_1.talk()


person_2 = Person("박명수")
