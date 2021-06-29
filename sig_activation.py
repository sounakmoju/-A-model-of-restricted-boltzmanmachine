class Sigmoid():
    def __call__(self, x):
        return 1/(1+np.exp(-x))
    def gradient(self,x):
        return self.__call__(self, x)*(1-self.__call__(self, x))
