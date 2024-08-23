from typing import Generator


# def f() -> Generator:
#     with open("jack.txt") as jack:
#         for line in jack:
#             words = line.split()
#             for word in words:
#                 yield word.strip(".")
#
#
# for i in f():
#     print(i)


# def echo_round() -> Generator[int, float, str]:
#     sent = yield 0
#     while sent >= 0:
#         sent = yield round(sent)
#     return 'Done'
#
#
# r = echo_round()
# print(next(r))
#
# print(r.send(5.4))

# def words_jack():
#     with open("jack.txt", "r") as file:
#         words = file.read().split()  # list str список со словами 463 слова
#
#     unique_words = list(set(words))  # список уникальных слов 48 слова
#     dct = {}
#     for i in range(len(unique_words)):
#         dct[unique_words[i]] = words.count(unique_words[i])  # добавляю в словарь количество совпадений в words по
#                                                              # ключу - слову
#     print(dct)

    # counter = 0
    # c_word = ""
    # for word in words:
    #     if word :
    #         counter += 1
    #         c_word = word
    # yield c_word, counter


# for word in words_jack():
#     print(word)

# words_jack()

from collections import Counter

c = Counter('hello world')
print(c)
c.subtract('world')
print(c)
c.subtract('world')
print(c)
# for num in c.elements():
#     print(num, end="")

