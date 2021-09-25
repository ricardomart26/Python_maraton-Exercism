
def capitalize_title(title):
    """

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """

    return title.upper()
    pass


def check_sentence_ending(sentence):
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """
    if sentence[-1] == '.':
        return True
    else:
        return False
    pass


def clean_up_spacing(sentence):
    """

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """
    size = len(sentence)
    for i in range(0, size):
        for i == ' ': 
    pass


def replace_word_choice(sentence, old_word, new_word):
    """

    :param sentence: str a sentence to replace words in.
    :param new_word: str replacement word
    :param old_word: str word to replace
    :return:  str input sentence with new words in place of old words
    """

    pass

print(check_sentence_ending("teste."))
