class InputError(Exception):
    pass
import random

class TipDetermine:
    def __init__(self,aboutService,yourFeel):
        self.serPoint=aboutService
        self.feel=yourFeel
        self.TipRate = 0

    def CalculateBase(self):
        self.TipRate=12+2*(self.serPoint-3)+(self.feel-3)+round(random.random()*3)*0.5
        
    def getTips(self):
        return self.__TeamRate

class Restaurant(TipDetermine):
    def __init__(self,aboutService,aboutStaff,yourFeel):
        super().__init__(aboutService, yourFeel)
        self.staPoint=aboutStaff
        self.__TipRate = 0

    def CalculateBase(self): 
        self.__TipRate=10+1.5*(self.serPoint-3)+1.5*(self.staPoint-3)+(self.feel-3)+round(random.random()*3)*0.5

    def getTips(self):
        return self.__TipRate


class Delivery(TipDetermine):
    def __init__(self,aboutService,yourFeel):
        super().__init__(aboutService, yourFeel)
        self.__TipRate = 0

    def CalculateBase(self): 
        self.__TipRate=8+2*(self.serPoint-3)+0.8*(self.feel-3)+round(random.random()*3)*0.5

    def getTips(self):
        return self.__TipRate
try:
    
    case = int(input("어떤 종류의 서비스인가요 1.식당 홀서비스 팁  2. 배달 팁  3. 기타 팁 "))
    if (case==1):
        service=int(input("제공받은 음식이 만족스럽나요? 5점 만점(정수입력)"))
        staff=int(input("서빙하는 직원은 만족스럽나요? 5점 만점(정수입력)"))
        Feeling=int(input("당신의 오늘 하루는 어떠 신가요? 5점 만점(정수입력)"))
        a=Restaurant(service,staff,Feeling)
    elif(case==2):
        service=int(input("제공받은 음식이 만족스럽나요? 5점 만점(정수입력)"))
        Feeling=int(input("당신의 오늘 하루는 어떠 신가요? 5점 만점(정수입력)"))
        a=Delivery(service,Feeling)
    elif(case==3):
        service=int(input("제공받은 음식이 만족스럽나요? 5점 만점(정수입력)"))
        Feeling=int(input("당신의 오늘 하루는 어떠 신가요? 5점 만점(정수입력)"))
        a=TipDetermine(service,Feeling)
    else:
        raise InputError

    

except ValueError:
    print("정수를 입력해주세요")
except InputError:
    print("잘못된 수를 입력하셨습니다. case는 1~3 점수는 1~5사이에 정수를 입력해주세요!")
        
        

        
        
    
    
 

