import csv
import os
from Levenshtein import distance
from repeat_removal import RepeatRemoval
from censore import Censore


class FileReader:

    def __init__(self, fileName):
        self.fileName = fileName

    def read(self):
        fileObj = open(self.fileName, "r")
        words = fileObj.read().split()
        fileObj.close()
        self.words = words

def levstn(word_list):
    fpath = r'..\data\refactored.txt'
    curses_list = []

    with open(fpath, 'r', encoding='utf-8') as f:
        curse_dict = f.readlines()

    index = 0
    for word in word_list:
        for curse in curse_dict:
            curse = curse.rstrip()
            lev = distance(word, curse)
            if lev <= 2:
                curses_list.append(index)
                break
            
        index += 1
    
    return curses_list
        

def main():
    example = ['kurwa', 'jebać', 'gniazdo', 'Maciek', 'rura', 'kuuuuuuuuurwa']
    example = RepeatRemoval.RemoveRepeated(example)
    words_to_censore = levstn(example)
    censored_text = Censore.ApplyCensorship(example, words_to_censore)
    print(censored_text)

if __name__ == '__main__':
    main()