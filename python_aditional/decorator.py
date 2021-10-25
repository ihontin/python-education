class Contexmanager:
    """Менеджер контекста"""

    def __enter__(self):
        """входит (только передает сообщение) """
        print("start working")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """и выходит (только передает сообщение) """
        print("end working")


class ItarationCl:
    """ленивый итератор, zip для
    объединения и словарь для вывода значений"""

    def __init__(self, *args):
        """получаем набор символов, миксуем с имеющимся"""
        self._val = args
        self._key = "a", "b", "c"
        self.gathering = zip(self._key, self._val)
        self.our_dict = {}
        ItarationCl.create_dict(self, self.gathering)

    def create_dict(self, iterium):
        """создаем словарь"""
        for k, v in iterium:
            self.our_dict[v] = k

    def __getitem__(self, item):
        """выводим по ключу"""
        return self.our_dict[item]


class ItarationFast:
    """Итератор выводит элементы списка, останавливается на переданной точке"""
    def __init__(self, li, stop):
        """принимаем список, точку остановки, создаем счетчик"""
        self.list_of = list(li)
        self._stop = stop
        self.i = 0

    def __next__(self):
        """возвращаем элементы списка"""
        if self.i == self._stop:
            return "stop"
        self.i += 1
        return f"{self.list_of[self.i - 1]} элемент списка"

    def __iter__(self):
        """на всякий пожарный"""
        return self




with Contexmanager() as start:
    def upgrade(fu):
        """обвертка"""
        def wrop(*res):
            """Декоратор преувеличивает средее арифметическое"""
            num_sum = sum(res)
            length = len(res)
            lier = fu(num_sum, length)
            return lier + lier // 4
        return wrop


    @upgrade
    def outside(*val):
        """Возвращает среднее арифметическое"""
        a, b = val
        return a / b


    first = outside(3, 4, 5, 6)
    print(first)


    def generator_fun(n):
        """генерируем все чётные"""
        for m in n:
            if m % 2 == 0:
                yield m


    iteriter = ItarationFast((1, 2, 3, 4, 5), 5)
    print(next(iteriter))
    print(next(iteriter))

    mumders1 = 1, 2, 3
    d = ItarationCl(*mumders1)
    for i in mumders1:
        print(d[i])

    vow = generator_fun(range(11))
    print(next(vow), next(vow), next(vow), next(vow), next(vow), next(vow))

    # with open("text.txt", "w", encoding="utf-8") as save_in:  # you're don't want to do this
    #     save_in.write(str(first))
