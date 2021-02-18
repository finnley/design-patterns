class Program(object):
    def main(self):
        # 生命一个变量 total 来计算总计
        total = 0

        price = input("请输入商品单价: ")
        print("price: ", price)

        num = input("请输入商品数量: ")
        print("num: ", num)

        # 声明一个变量 totalPrices 来计算每个商品的单价 * 数量
        totalPrices = float(price) * float(num)

        # 将每个商品合计计入总计
        total = total + totalPrices

        # 展示信息
        print("单价：" + price + " 数量：" + num + " 合计：" + str(total))

if __name__ == "__main__":
    run = Program()
    run.main()