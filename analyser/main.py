import csv
import os
from math import sqrt
from Levenshtein import distance
from input_preprocessing import InputPreprocessing
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
    fpath2 = r'..\data\refactored_2.txt'
    curses_list = []

    with open(fpath, 'r', encoding='utf-8') as f:
        curse_dict = f.readlines()
    
    with open(fpath, 'r', encoding='utf-8') as f:
        curse_pref_dict = f.readlines()

    curse_dict = curse_dict + curse_pref_dict

    index = 0
    previous_word = None
    for word in word_list:
        for curse in curse_dict:
            curse = curse.rstrip()
            if curse in word:
                curses_list.append(index)
                break

            lev = distance(word, curse, weights=(1, 1, 1))
            if lev <= sqrt(len(word)) - 1.5:
                curses_list.append(index)
                # print(word, ' ', lev, ' ', curse)
                break

            if previous_word != None:
                subject = previous_word + word
                if curse == subject:
                    curses_list.append(index)
                    curses_list.append(index - 1)
                    break

                lev = distance(subject, curse)
                if lev <= sqrt(len(subject)) - 1.5:
                    curses_list.append(index)
                    curses_list.append(index - 1)
                    # print(word, ' ', lev, ' ', curse)
                    break
        
        previous_word = word
            
        index += 1
    
    return curses_list

def main():
    sentence = 'Cześc, jestem Maciek, lubię krowa kurwa KvRVV4 i kur wy ch00j.'
    sentence_words = sentence.split()
    example = sentence_words
    example = InputPreprocessing.ProcessInput(example)
    words_to_censore = levstn(example) # List of indexes
    censored_text = Censore.ApplyCensorship(sentence_words, words_to_censore)
    # TODO: cesored_text to file
    print(censored_text)

if __name__ == '__main__':
    main()