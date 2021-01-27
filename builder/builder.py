from abc import ABC, abstractclassmethod, abstractproperty


class SetMeal:
    @property
    def main_dish(self):
        return self.__main_dish

    @main_dish.setter
    def main_dish(self, main_dish):
        self.__main_dish = main_dish

    @property
    def side_dish(self):
        return self.__side_dish

    @side_dish.setter
    def side_dish(self, side_dish):
        self.__side_dish = side_dish

    def __str__(self) -> str:
        return f"メインディッシュ:{self.main_dish}, サイドディッシュ:{self.side_dish}"


#
class SetMealBuilder(ABC):
    def __init__(self):
        self._set_meal = SetMeal()

    @abstractproperty
    def product(self):
        pass

    @abstractclassmethod
    def build_main_dish(self):
        pass

    @abstractclassmethod
    def build_side_dish(self):
        pass


class SanmaSetBuilder(SetMealBuilder):
    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = "さんま"

    def build_side_dish(self):
        self._set_meal.side_dish = "お味噌汁"


class PastaSetBuilder(SetMealBuilder):
    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = "パスタ"

    def build_side_dish(self):
        self._set_meal.side_dish = "スープ"


class Director:
    def __init__(self, builder: SetMealBuilder):
        self.__builder = builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    def build(self):
        self.builder.build_main_dish()
        self.builder.build_side_dish()
        return self.builder


if __name__ == "__main__":
    sanma_builder = SanmaSetBuilder()
    pasta_builder = PastaSetBuilder()

    director = Director(sanma_builder)
    print(director.build().product)
    # print(director.builder.product)

    director.builder = pasta_builder
    print(director.build().product)
    # print(director.builder.product)
