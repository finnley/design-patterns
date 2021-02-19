from strategy_pattern.python.v3.cash_super import CashSuper


class CashNormal(CashSuper):
    '''
    正常收费吗，原价返回
    '''
    def acceptCash(self, money: float) -> float:
        return money