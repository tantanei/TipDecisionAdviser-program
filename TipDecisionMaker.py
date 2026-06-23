import random

class GenTipDeter:
    def __init__(self,aboutService,yourFeel):
        self.__serPoint=aboutService
        self.__feel=yourFeel

    def CalculateBase(self)
        self__TeamRate=12+2*(self.__serPoint-3)+(self.__feel-3)+round(random.random()*3)*0.5
        
    def getTips(self):
        return self__TeamRate

class Restaurant(self,aboutService,aboutStaff,yourFeel):
    def __init__(self,aboutService,yourFeel):
        super().__init__()
        self.__staPoint=aboutStaff

    def CalculateBase(self): 
        self__TeamRate=10+1.5*(self.__serPoint-3)+1.5*(self.__staPoint-3)+(self.__feel-3)+round(random.random()*3)*0.5

    def getTips(self):
        return self__TeamRate


class Delivery(GenTipDeter):
    def __init__(self,aboutService,yourFeel):
        super().__init__()
        self.__staPoint=aboutStaff

    def CalculateBase(self): 
        self__TeamRate=8+2*(self.__serPoint-3)+0.8*(self.__feel-3)+round(random.random()*3)*0.5

    def getTips(self):
        return self__TeamRate
try:
    
    case = int(input("어떤 종류의 서비스인가요 1.식당 홀서비스 팁  2. 배달 팁  3. 기타 팁 "))
    if (case==1):
        service=int(input("제공받은 음식이 만족스럽나요? 5점 만점(정수입력)"))
        staff=int(input("서빙하는 직원은 만족스럽나요? 5점 만점(정수입력)"))
        Feeling=int(input("당신의 오늘 하루는 어떠 신가요? 5점 만점(정수입력)"))
    elif(case==2 or case==3):
        service=int(input("제공받은 음식이 만족스럽나요? 5점 만점(정수입력)"))
        Feeling=int(input("당신의 오늘 하루는 어떠 신가요? 5점 만점(정수입력)"))
    else:
        raise "InputError"

except ValueError:
    print("정수를 입력해주세요")
except "InputError":
    print("잘못된 수를 입력하셨습니다. case는 1~3 점수는 1~5사이에 정수를 입력해주세요!")
        
        

        
        
    
    
 

