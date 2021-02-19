from strategy_pattern.python.v3.cash_super import CashSuper

# 打折收费子类
class CashRebate(CashSuper):
    def __init__(self, moneyRebate):
        self.__moneyRebate = moneyRebate

    # 打折收费，初始化时，必须要输入折扣率，如八折，就是0.8
    def acceptCash(self, money: float) -> float:
        return money * self.__moneyRebate