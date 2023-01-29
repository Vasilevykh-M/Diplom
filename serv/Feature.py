# класс для парметра распределения
# хранит имя, можно ли востановить нулевые значения
# коробчатую диаграмму
# диаграмму распределения
class Feature:
    def __init__(self, name, canNull, boxplot, distributionplot):
        self.__name = name
        self.__canNull = canNull
        self.__boxplot = boxplot
        self.__distributionplot = distributionplot

    def name(self):
        return self.__name

    def canNull(self):
        return self.__canNull

    def boxplot(self):
        return self.__boxplot

    def distributionplot(self):
        return self.__distributionplot


class FeatureNum(Feature):
    def __init__(self, name, canNull, boxplot, distributionplot, std, mean):
        super().__init__(name, canNull, boxplot, distributionplot)
        self.__std = std
        self.__mean = mean

    def std(self):
        return self.__std

    def mean(self):
        return self.__mean


class FeatureCat(Feature):
    def __init__(self, name, canNull, boxplot, distributionplot, code_dictionary):
        super().__init__(name, canNull, boxplot, distributionplot)
        self.__code_dictionary = code_dictionary

    def code_dictionary(self):
        return self.__code_dictionary