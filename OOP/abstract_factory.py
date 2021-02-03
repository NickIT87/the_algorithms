from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    @abstractmethod
    def get_dimensions(self):
        """The Chair Interface"""


class BigChair(IChair):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class ChairFactory():
    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype == "BigChair":
                return BigChair()
            raise AssertionError("Chair is not found")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    CHAIR = ChairFactory.get_chair("BigChair")
    print(CHAIR.get_dimensions())