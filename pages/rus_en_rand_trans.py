from googletrans import Translator
from random import sample


def rus_en_rand_trans(PATH, NUM_OF_WORDS):
    with open(PATH, encoding='cp1251') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    rand_words = sample(lines, NUM_OF_WORDS)
    translator = Translator()
    words_trans = []
    for word in rand_words:
        trans = translator.translate(text=word, src='ru').text
        words_trans.append("{} - {}".format(word, trans))

    return words_trans