class Calculator:
    def plus(a,b):
        return a+b

    def minus(a,b):
        return a-b

    def multiply(a, b):
        return a*b

    def divide(a,b):
        return a/b



if __name__ == '__main__':
    print("{0} + {1} = {2} ".format(7,4, Calculator.plus(7,4)))
    print("{0} - {1} = {2} ".format(7,4, Calculator.minus(7,4)))
    print("{0} * {1} = {2} ".format(7,4, Calculator.multiply(7,4)))
    print("{0} / {1} = {2} ".format(7,4, Calculator.divide(7,4)))