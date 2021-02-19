from strategy_pattern.python.v3.cash_normal import CashNormal
from strategy_pattern.python.v3.cash_rebate import CashRebate
from strategy_pattern.python.v3.cash_return import CashReturn

# 现金收费工厂类
class CashFactory(object):
    @staticmethod
    def createCashAccept(type):
        if type == "正常收费":
            return CashNormal()
        elif type == "满 300 返 100":
            return CashReturn("300", "100")
        elif type == "打 8 折":
            return CashRebate("0.8")