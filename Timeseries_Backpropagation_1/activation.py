import math

class ActivationFunction:
    # __singleton = None
    # def __new__(cls):
    #     cls.__singleton = cls
    def __init__(self, types='Sigmoid'):
        # if self.__singleton is None:
        #     self.__singleton = self
        # cls = self.__singleton
        self.func = self.sigmoid
        self.dfunc = self.dsigmoid

        if types == 'Sigmoid':
            self.func = self.sigmoid
            self.dfunc = self.dsigmoid

    def run(self, x):
        return self.func(x)

    def sigmoid(self, x):
        return math.tanh(x)

    # derivative of our sigmoid function, in terms of the output (i.e. y)
    def dsigmoid(self, y):
        return 1.0 - y**2


if __name__ == '__main__':
    myfunc = ActivationFunction('Sigmoid')
