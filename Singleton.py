class CalculatorBuilder:
    def __init__(self):
        self.calc = None

    def instance(self):
        if self.calc is None:
            self.calc = self.Calculator()
        return self.calc

    class Calculator:
        def add(self, x, y):
            return x + y

        def sub(self, x, y):
            return x - y

        def mult(self, x, y):
            return x * y

        def div(self, x, y):
            return x / y



cb1 = CalculatorBuilder()
calc = cb1.instance()
calc2 = cb1.instance()
assert(calc is calc2)
