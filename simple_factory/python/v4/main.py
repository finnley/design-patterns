import OperationFactory

class Program(object):
    def main(self):
        op = OperationFactory().createOperate("-")
        op.SetNumberA(1)
        op.SetNumberB(2)
        strResult = op.GetResult()
        print("结果是: %s" % strResult)

if __name__ == "__main__":
    run = Program()
    run.main()