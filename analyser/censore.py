import string

class Censore():
    def ApplyCensorship(word_list, censore_list):
        censored_list = word_list
        for word_to_censore in censore_list: # word_to_censore = index of a word to censore
            og_word = word_list[word_to_censore]
            if og_word[-1] in string.punctuation:
                i = len(og_word) - 1
                punct_counter = 0
                while og_word[i] in string.punctuation:
                    punct_counter += 1
                    i -= 1
                censored_list[word_to_censore] = (len(og_word) - punct_counter) * '*' + punct_counter * og_word[-1]
            else:
                censored_list[word_to_censore] = len(og_word) * '*'

        return censored_list
