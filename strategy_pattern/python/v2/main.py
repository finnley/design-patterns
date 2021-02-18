# 增加打折
class Program(object):
    discountMessage = {
        'a': '正常收费',
        'b': '打八折',
        'c': '打七折',
        'd': '打五折'
    }

    discount = {
        'a': 1,
        'b': 0.8,
        'c': 0.7,
        'd': 0.5
    }

    # 折扣
    def getDistcountMessage(self, index='a'):
        return self.discountMessage.get(index)

    def main(self):
        print("please input 'a', 正常收费")
        print("please input 'b', 打八折")
        print("please input 'c', 打七折")
        print("please input 'd', 打五折")

        index = input("请选择折扣: ")
        print("您选择的是: ", index)

        totalPrices = 0
        total = 0

        price = input("请输入商品单价: ")
        print("price: ", price)

        num = input("请输入商品数量: ")
        print("num: ", num)

        if index == 'a':
            totalPrices = float(price) * float(num)
        elif index == 'b':
            totalPrices = float(price) * float(num) * 0.8
        elif index == 'c':
            totalPrices = float(price) * float(num) * 0.7
        elif index == 'd':
            totalPrices = float(price) * float(num) * 0.5

        total = total + totalPrices

        print("单价：" + price + " 数量：" + num + " 折扣: " + self.getDistcountMessage(index) + " 合计：" + str(total))


run = Program()
run.main()

'''
总结：
该方法重复代码太多，比如 float(price)；
而且4个分支要执行的语句除了打折多少以外几乎没有什么不同，可以考虑重构；
如果添加需求，商场活动加大，需要有满300返100的促销算法，怎么办？
'''