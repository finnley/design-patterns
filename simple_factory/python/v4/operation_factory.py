import OperationAdd
import OperationSub
import OperationMul
import OperationDiv

# 简单运算工厂类
class OperationFactory(object):
    @staticmethod
    def createOperate(operate):
        if operate == "+":
            return OperationAdd()
        if operate == "-":
            return OperationSub()
        if operate == "*":
            return OperationMul()
        if operate == "/":
            return OperationDiv()
