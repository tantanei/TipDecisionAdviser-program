class InputError(Exception):
    pass
import random

class TipDetermine:
    def __init__(self,aboutService,yourFeel):
        self.serPoint=aboutService
        self.feel=yourFeel
        self.__TipRate = 0

    def CalculateBase(self):
        self.__TipRate=12+2*(self.serPoint-3)+(self.feel-3)+round(random.random()*3)*0.5
        
    def getTips(self):
        return self.__TipRate

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

def askserviceFeeling():
    service=int(input("제공받은 서비스가 만족스럽나요? 5점 만점(정수입력): "))
    Feeling=int(input("당신의 오늘 기분은 어떠신가요? 5점 만점(정수입력): "))
    return service, Feeling

    
try:
    
    case = int(input("어떤 종류의 서비스인가요 (1.식당 홀서비스  2. 배달  3. 기타): "))
    if (case==1):
        service,Feeling=askserviceFeeling()
        staff=int(input("서빙하는 직원은 만족스럽나요? 5점 만점(정수입력): "))
        if((service>5 or service<1)or(staff>5 or staff<1)or(Feeling>5 or Feeling<1)):
            raise InputError
        a=Restaurant(service,staff,Feeling)
        a.CalculateBase()
        finrate=a.getTips()
    elif(case==2):
        service,Feeling=askserviceFeeling()
        if((service>5 or service<1)or(Feeling>5 or Feeling<1)):
            raise InputError
        a=Delivery(service,Feeling)
        a.CalculateBase()
        finrate=a.getTips()
    elif(case==3):
        service,Feeling=askserviceFeeling()
        if((service>5 or service<1)or(Feeling>5 or Feeling<1)):
            raise InputError
        a=TipDetermine(service,Feeling)
        a.CalculateBase()
        finrate=a.getTips()
    else:
        raise InputError
    
    price = int(input("서비스 가격을 입력하세요: "))
    if price<=0:
        raise InputError
    finaltip = int(((price * finrate / 100) // 100) * 100)
    print(f"추천 팁 비율: {finrate:.1f}%")  # 계산 특성상 finrate 값은 소수점 한 자리까지 나오지만, 혹시 모르니 출력 형식을 한 자리로 제한한다.
    print(f"추천 팁 금액: {finaltip}원")
    print(f"추천 지불 금액: {price+finaltip}원")

except ValueError:
    print("정수를 입력해주세요")
except InputError:
    print("잘못된 수를 입력하셨습니다. case는 1~3 점수는 1~5사이의 정수를, 가격은 양수를 입력해주세요!")


        
        
    
    
 

