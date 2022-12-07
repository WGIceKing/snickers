class Censore():
    def ApplyCensorship(word_list, censore_list):
        censored_list = word_list
        for word_to_censore in censore_list: # word_to_censore = index of a word to censore
            og_word = word_list[word_to_censore]
            censored_list[word_to_censore] = len(og_word) * '*'

        return censored_list
