import random

class GenTipDeter:
    def __init__(self,aboutService,aboutStaff,yourFeel):
        self.__serPoint=aboutService
        self.__staPoint=aboutStaff
        self.__feel=yourFeel

    def CalculateBase(self):  #이건 자식 클래스로 내릴건데 일단 쓴다
        self__TeamRate=10+1.5*(self.__serPoint-3)+1.5*(aboutStaff-3)+(aboutStaff-3)+round(random.random() * 5)*0.5
        
    def getTips(self):
        return self__TeamRate

class Restaurant(GenTipDeter):
    
 

