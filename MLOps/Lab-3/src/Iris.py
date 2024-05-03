class Iris:
    """Для создания экземпляра класса в конструктор необходимо передать параметры:
    `sepal_length`, `sepal_width`, `petal_length`, `petal_width.`

    Будет выброшена `ValueError`, если переданы не валидные значения параметров.
    Валидные значения параметров: число `int`, число `float`, строка `str`,
    содержащая число.

    Методы:
        `get_params(): -> tuple[float, float, float,f loat]` - возвращает кортеж из
        валидированных значений:
        `sepal_length`, `sepal_width`, `petal_length`, `petal_width`.
    """

    CLASSES = ("setosa", "versicolor", "virginica")

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.__sepal_length = float(sepal_length)
        self.__sepal_width = float(sepal_width)
        self.__petal_length = float(petal_length)
        self.__petal_width = float(petal_width)

    def get_params(self):
        return (
            self.__sepal_length,
            self.__sepal_width,
            self.__petal_length,
            self.__petal_width,
        )
