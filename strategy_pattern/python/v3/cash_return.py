from strategy_pattern.python.v3.cash_super import CashSuper

# 返利收费子类
class CashReturn(CashSuper):
    # 返利收费，初始化时必须要输入返利条件和返利值，比如满300返100，则 moneyCondition = 300, moneyReturn =  100
    def __init__(self, moneyCondition, moneyReturn):
        self.__moneyCondition = moneyCondition
        self.__moneyReturn = moneyReturn

    def acceptCash(self, money: float) -> float:
        result = money

        # 如果大于返利条件，则需要减去返利值
        if money >= self.__moneyCondition:
            return money - float(money) / float(self.__moneyCondition) * self.__moneyReturn

        return result
