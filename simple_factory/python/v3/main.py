import operation

'''
    业务逻辑和界面逻辑分开
    客户端代码
'''
class Program(object):
    def main(self):
        try:
            strNumberA = input("请输入数字A: ")
            print("strNumberA: ", strNumberA)

            strOperate = input("请选择运算符号(+、-、*、/): ")
            print("strOperate: ", strOperate)

            strNumberB = input("请输入数字B: ")
            print("strNumberB: ", strNumberB)

            print("Expression: strResult = A %s B = %s %s %s" % (strOperate, strNumberA, strOperate, strNumberB))

            strResult = operation.Operation.GetResult(strNumberA, strNumberB, strOperate)
            print("结果是: %s" % strResult)
        except BaseException as e:
            print("结果有误: ", e)

if __name__ == "__main__":
    run = Program()
    run.main()