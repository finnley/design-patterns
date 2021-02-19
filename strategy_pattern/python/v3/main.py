from strategy_pattern.python.v3.cash_factory import CashFactory

# 利用简单工厂模式根据不同类型胜场相应对应
class Program(object):
    discountMessage = {
        'a': '正常收费',
        'b': '满 300 返 100',
        'c': '打 8 折',
    }

    discount = {
        'a': 1,
        'b': 0.8,
        'c': 0.7,
    }

    # 折扣
    def getDiscountMessage(self, index='a'):
        return self.discountMessage.get(index)

    def main(self):
        print("please input 'a', 正常收费")
        print("please input 'b', 满 300 返 100")
        print("please input 'c', 打 8 折")

        index = input("请选择折扣: ")
        print("您选择的是: ", index)

        csuper = CashFactory.createCashAccept(self.getDiscountMessage(index))

        total = 0

        price = input("请输入商品单价: ")
        print("price: ", price)

        num = input("请输入商品数量: ")
        print("num: ", num)

        totalPrices = csuper.acceptCash(float(price) * float(num))
        total = total + totalPrices

        print("单价：" + price + " 数量：" + num + " 折扣: " + self.getDiscountMessage(index) + " 合计：" + str(total))


if __name__ == "__main__":
    run = Program()
    run.main()

'''
总结：
如果增加需求，需要打五折并且满500送200的促销活动？
如果再增加需求，满100积分10点，以后积分到一定时候可以领取奖品？

简单工厂虽然可以解决上面问题，但这个模式只是解决对象的创建问题，而且工厂本身包括了所有的收费方式，
商场时可能进场性的更改很糟糕的处理方式，所以它不是最好的办法，面对算法的市场变动，需要有更好的办法

比如策略模式(Strategy):
定义算法家族，分别封装起来，让它们之间可以相互替换，此模式让算法的变化，不会影响到使用算法的客户
'''