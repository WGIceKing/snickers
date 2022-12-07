import csv
import os
from math import sqrt
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
            if lev <= sqrt(len(word)) - 1:
                curses_list.append(index)
                # print(word, ' ', lev, ' ', curse)
                break
            
        index += 1
    
    return curses_list
        

def main():
    sentence = 'Kurwa wymyślać, przekleństwa muszę japierdole onomatopeja chędożenie chedozenie'
    example = sentence.split()
    example = RepeatRemoval.RemoveRepeated(example)
    words_to_censore = levstn(example) # List of indexes
    censored_text = Censore.ApplyCensorship(example, words_to_censore)
    # TODO: cesored_text to file
    print(censored_text)

if __name__ == '__main__':
    main()