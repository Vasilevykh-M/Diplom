class Date:
    def __init__(self, start, end, count):
        self.__start = start
        self.__end = end
        self.__count = count

    def start(self):
        return self.__start

    def end(self):
        return self.__end

    def count(self):
        return self.__count