
class DataStatistics(object):

    def __init__(self, data: list) -> None:
        self.__data = data
        self.__data_inverted = []
        self.__min_value = 0
        self.__max_value = 0
        self.__building()

    def __building(self):
        # Sort the list
        self.__data.sort()
        self.__data_inverted = sorted(self.__data, reverse=True)
        self.__min_value = self.__data[0]
        self.__max_value = self.__data[-1]

    def less(self, value: int, inclusive: bool = False) -> list:
        result = []
        if value > self.__min_value:
            result = [
                num for num in self.__data if self.__lte_check(num=num, value=value, inclusive=inclusive)
            ] if value <= self.__max_value else self.__data
        return result

    def greater(self, value: int, inclusive: bool = False) -> list:
        result = []

        if value < self.__max_value:
            result = [
                num for num in self.__data[::-1] if self.__gte_check(num=num, value=value, inclusive=inclusive)
            ][::-1]
        return result

    def between(self, value_min: int, value_max: int) -> list:
        left = self.less(value=value_max, inclusive=True)
        right = self.greater(value=value_min, inclusive=True)

        long, short = (left, right) if len(left) > len(right) else (right, left)

        result = [
            l for l in long if l in short
        ]

        return result

    @staticmethod
    def __gte_check(num: int, value: int, inclusive: bool = False) -> bool:
        return num > value if not inclusive else num >= value

    @staticmethod
    def __lte_check(num: int, value: int, inclusive: bool = False) -> bool:
        return num < value if not inclusive else num <= value


class DataCapture(object):

    def __init__(self) -> None:
        self.__data = []

    def add(self, value: int) -> None:
        self.__data.append(value)

    def build_stats(self) -> DataStatistics:
        return DataStatistics(data=self.__data)
