import csv
import os
from math import sqrt
from Levenshtein import distance
from input_preprocessing import InputPreprocessing
from censore import Censore

def levstn(word_list):
    fpath = '../data/refactored.txt'
    fpath2 = '../data/refactored_2.txt'
    curses_list = []

    with open(fpath, 'r', encoding='utf-8') as f:
        curse_dict = f.readlines()
    
    with open(fpath2, 'r', encoding='utf-8') as f:
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
                    break
        
        previous_word = word
            
        index += 1
    
    return curses_list

def main():
    fineName = 'message.txt'
    with open(fineName, 'r', encoding='utf-8') as f:
        sentence = f.read()
    sentence_words = sentence.split()
    example = sentence_words
    example = InputPreprocessing.ProcessInput(example)
    words_to_censore = levstn(example) # List of indexes
    censored_text = Censore.ApplyCensorship(sentence_words, words_to_censore)
    print(' '.join(censored_text))
    fineName = 'message_filtred.txt'
    with open(fineName, 'w', encoding='utf-8') as f:
        f.write(' '.join(sentence_words))

if __name__ == '__main__':
    main()