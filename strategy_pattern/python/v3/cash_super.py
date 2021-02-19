from abc import ABCMeta, abstractmethod, abstractproperty, ABC

# 现金收费抽象类
class CashSuper(metaclass=ABCMeta):
    '''
       现金收取超类的抽象方法，收取现金，参数为原价，返回为当前价
    '''
    @abstractmethod
    def acceptCash(self, money: float) -> float:
        pass