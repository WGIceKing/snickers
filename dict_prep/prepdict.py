import re

class toDict():
    def __init__(this):
        with open("message.txt", 'r', encoding="utf-8") as file:
            data = file.read().replace('\n', '')
            res = re.findall(r'\[\[.*?\]\]', data)
            with open("data/refactored_og.txt", 'w', encoding="utf-8") as save_file:
                for word in res:
                    save_file.write(word[2:-2] + '\n')

toDict()