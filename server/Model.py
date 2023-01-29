from enum import Enum

class ModelType(Enum):
    Boosting = 1
    SVM = 2
    NN = 3

class Model:
    def __init__(self, type, acc_train, acc_test, f1_train, f1_test, cf):
        self.__type = type
        self.__acc_train = acc_train
        self.__acc_test = acc_test
        self.__f1_train = f1_train
        self.__f1_test = f1_test
        self.__cf = cf

    def Type(self):
        return self.__type

    def acc_train(self):
        return self.__acc_train

    def acc_test(self):
        return self.__acc_test

    def f1_train(self):
        return self.__f1_train

    def f1_test(self):
        return self.__f1_test

    def cf(self):
        return self.__cf

    def fit(self, Data):
        return

    def predict(self, Data):
        return

    def f1(self, Y_true, Y_predict):
        return

    def accuracy(self, Y_true, Y_predict):
        return

    def CF(self, Y_true, Y_predict):
        return

    def saveModel(self):
        return
