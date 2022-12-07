import re
import string

dict = {'1' : 'i',
        '3': 'e',
        '4': 'a',
        '5': 's',
        '7': 't',
        '8': 'b',
        '0': 'o',
        'v': 'u',
        'vv': 'w'}


class RepeatRemoval():
    def RemoveRepeated(word_list):

        return_list = []
        for word in word_list:
            word = word.lower()
            
            for key, initial in dict.items():
                word = word.replace(key, initial)

            word = word.translate(str.maketrans("","", string.punctuation))
            return_list.append(re.sub(r'(\w)\1+', r'\1', word))

        return return_list
