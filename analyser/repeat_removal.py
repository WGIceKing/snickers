import re

class RepeatRemoval():
    def RemoveRepeated(word_list):

        return_list = []
        for word in word_list:
            return_list.append(re.sub(r'(\w)\1+', r'\1', word))

        return return_list
