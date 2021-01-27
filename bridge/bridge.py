from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @abstractmethod
    def create_shape_str(self):
        pass


class RectangleShape(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def create_shape_str(self):
        rectangle = "*" * self._width + "\n"
        for _ in range(self._height - 2):
            rectangle += "*" + " " * (self._width - 2) + "*" + "\n"
        rectangle += "*" * self._width + "\n"
        return rectangle


class SquareShape(Shape):
    def __init__(self, width, height=None):
        super().__init__(width, width)

    def create_shape_str(self):
        square = "*" * self._width + "\n"
        for _ in range(self._width):
            square += "*" + " " * (self._width - 2) + "*" + "\n"
        square += "*" * self._width + "\n"
        return square


# Bridgeを生かした機能追加
class WirteAbstraction(ABC):
    def __init__(self, shape: Shape):
        self._shape = shape

    def read_shape(self):
        return self._shape.create_shape_str()

    @abstractmethod
    def write_to_text(self, file_name):
        pass


class WriteShape(WirteAbstraction):
    def write_to_text(self, file_name):
        with open(file_name, mode="w", encoding="utf-8") as fh:
            fh.write(self.read_shape())


if __name__ == "__main__":
    rectangle = RectangleShape(10, 5)
    print(rectangle.create_shape_str())
    square = SquareShape(10)
    print(square.create_shape_str())

    write_shape = WriteShape(rectangle)
    write_shape.write_to_text("tmp.txt")
