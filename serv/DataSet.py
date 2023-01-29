import psycopg2
import configparser
import pandas as pd
import numpy as np
import CustomDate

class DataSet:
    def __init__(self, features, data = None):
        self.data = data
        self.__features = features

    def features(self):
        return self.features

    def addOptionalFeature(self):
        return


class DataSetUser(DataSet):
    def __init__(self, features, series):
        super().__init__(features)
        self.data = series

    def valid(self):
        return True


class DataSetEnginer(DataSet):
    def __init__(self, features):
        super().__init__(features)
        self.data = None
        self.data_test = None
        self.data_train = None

    def loadDB(self, dates):
        return

    def splitData(self, percent):
        return

    def clMiss(self):
        return

    def categor(self):
        return

    def norm(self):
        return

