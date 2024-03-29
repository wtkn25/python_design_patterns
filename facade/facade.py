class Knife:
    def __init__(self, name):
        self.__name = name

    def cut_vegetables(self):
        print(f"野菜を{self.__name}でカットします")


class Boiler:
    def __init__(self, name):
        self.__name = name

    def boil_vegetables(self):
        print(f"野菜を{self.__name}でボイルします")


class Frier:
    def __init__(self, name):
        self.__name = name

    def fry_vegetables(self):
        print(f"野菜を{self.__name}でカットします")


# facadeを活用する
class Cook:
    def __init__(self, knife: Knife, frier: Frier, boiler: Boiler):
        self.__knife = knife
        self.__frier = frier
        self.__boiler = boiler

    def cook_dish(self):
        self.__knife.cut_vegetables()
        self.__frier.fry_vegetables()
        self.__boiler.boil_vegetables()


if __name__ == "__main__":
    knife = Knife("My Knife")
    frier = Frier("My Frier")
    boiler = Boiler("My Boiler")

    # knife.cut_vegetables()
    # frier.fry_vegetables()
    # boiler.boil_vegetables()

    cook = Cook(knife, frier, boiler)
    cook.cook_dish()
