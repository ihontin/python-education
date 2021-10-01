"""Итераторы и генераторы"""


class MultipleSentencesError(Exception):
    """Новый класс исключение"""

    def __str__(self):
        """принтит сообщение"""
        return "ERROR: MultipleSentencesError"


class Checkall:
    """Класс на проверки предложений, символов, вызывает исключения исключения"""

    @staticmethod
    def find_end(sign):
        """Нахождение символа конца предложения"""
        fined_sign = ""
        if sign.count(".") == 1:
            fined_sign = "."
        elif sign.count("...") == 1:
            fined_sign = "..."
        elif sign.count("!") == 1:
            fined_sign = "!"
        elif sign.count("?") == 1:
            fined_sign = "?"
        return fined_sign

    @staticmethod
    def check_sentence(val):
        """Ловит исключение MultipleSentencesError
        при нахождении ошибок выводит ошибки TypeError, ValueError"""
        try:
            if not isinstance(val, str):
                raise TypeError
            if val.count(".") == 0 and val.count("...") == 0 and val.count("!") == 0 and val.count("?") == 0:
                raise ValueError
            if val.count(".") + val.count("...") + val.count("!") + val.count("?") > 1:
                raise ValueError
            index_sign = val.index(Checkall.find_end(val))
            for i in val[index_sign:]:
                if i.isalpha():
                    raise MultipleSentencesError
            else:
                return True
        except MultipleSentencesError as my_error:
            print(my_error)


class Sentence(Checkall):
    """Надстройка над итератором.

    Принимает строку, убирает все символы кроме букв и пробелов.
     Возвращает строку по словам"""

    def __init__(self, stings):
        """Принимает, сохраняет строку, создает переменные-счетчики"""
        if Checkall.check_sentence(stings):
            self._strings, self.not_words_string = stings, ""
            self.count_not_words, self._counter = 0, 0
            self._words_string = Sentence.del_not_letters(self, stings)
            self.count_words = len(self._words_string.split())

    def __iter__(self):
        """Вызывается в цикле for и iter()
        Отправляет строку в итератор"""
        return SentenceIterator(self._words_string)


    def __repr__(self):
        """Выводит отдельно количество слов и других символов"""
        return f"Sentence(words={self.count_words}, other_chars={self.count_not_words})"

    def __getitem__(self, item):
        """Возвращает строку по словам, работает со сплайсами"""
        if isinstance(item, int):
            return self._words_string.split()[item]
        else:
            return " ".join(self._words_string.split()[item])

    def del_not_letters(self, val):
        """Убирает лишние символы из строки
        сохраняет строку с этими символами и считает их"""
        else_str = ""
        for i in val:
            if not i.isalpha():
                self.not_words_string += i + " "
                else_str += " "
                self.count_not_words += 1
                continue
            else_str += i
        return else_str.strip()

    def _words(self):
        """Возвращает функцию генератор"""
        for nex in self._words_string.split():
            yield nex

    @staticmethod
    def break_point(val, count):
        """надстройка над __next__
        выводит поочерёдно слова, останавливает цикл"""
        if count == len(val.split()):
            return "stop"
        return val.split()[count]

    @property
    def words(self):
        """печатает строку по словам"""
        # return " ".join(self._words_string.split())
        # return print(*self._words_string.split()) # для консоли
        creation_words_list = ""
        for word in Sentence(self._strings):  # через наш итератор
            if word == "stop":
                break
            creation_words_list += word + " "
        return [i for i in creation_words_list.strip().split()]

    @property
    def other_chars(self):
        """печатает символы строки по словам"""
        return self.not_words_string  # Если пробел
        # return print(*self.not_words_string.split())


class SentenceIterator:
    """Итератор принимает строку"""

    def __init__(self, val):
        """Создает счётчик и сохраняет список слов"""
        self.list_words = val
        self._count = -1

    def __len__(self):
        """находит количество слов в строке"""
        return len(self.list_words.split())

    def __next__(self):
        """Вызыватся в цикле for """
        self._count += 1
        return Sentence.break_point(self.list_words, self._count)

    def __repr__(self):
        """ Вернёт название нашего итератора"""
        return "SentenceIterator"


# ERRORS
# print(Sentence((1, 4, 7)))
# print(Sentence("Hello word! A!  "))
# print(Sentence("Hello word! A  "))

# print(Sentence("If i get some milk, i will be more serious Not to me. -"))  # <Sentence(words=13, other_chars=7)>
# print(Sentence("If i get some milk, i will be more serious Not to me. -")._words())  # <generator object Sentence._words at 0x7f4e8cb065f0>
# print(next(Sentence("Hello word!")._words()))  # 'Hello'
#
print(Sentence("If i get some milk, i will be more serious Not to me. -").words) # выводит список слов
# print(Sentence("If i get some milk, i will be more serious Not to me. -").other_chars)  # вывдоит список символов
#
# print(Sentence("Hello word!")[0])
# print(Sentence("The word not enough!")[::-1])
# for word in Sentence('Hello world!'):
#     if word == "stop":
#         break
#     print(word)
# print(iter(Sentence("Hello word!"))) # SentenceIterator


