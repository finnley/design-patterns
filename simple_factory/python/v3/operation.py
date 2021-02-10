'''
    业务逻辑和界面逻辑分开
    Operation 运算类
'''
class Operation(object):
    @staticmethod
    def GetResult(numberA: float, numberB: float, operate: str) -> float:
        result = 0
        o = Operation()
        result = o.switch(operate, numberA, numberB)
        return result

    def switch(self, operate, numberA, numberB):
        switcher = {
            "+": self.add,
            "-": self.sub,
            "*": self.multiply,
            "/": self.divide
        }
        method = switcher.get(operate, "wrong operate")
        return method(numberA, numberB)

    # add
    def add(self, numberA, numberB):
        return str(float(numberA) + float(numberB))

    # subtract
    def sub(self, numberA, numberB):
        return str(float(numberA) - float(numberB))

    # multiply
    def multiply(self, numberA, numberB):
        return str(float(numberA) * float(numberB))

    # divide
    def divide(self, numberA, numberB):
        if numberB != '0':
            return str(float(numberA) / float(numberB))
        else:
            return "除数不能为0"