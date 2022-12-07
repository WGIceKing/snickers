import csv

class FileReader:

    def __init__(self, fileName):
        self.fileName = fileName

    def read(self):
        fileObj = open(self.fileName, "r")
        words = fileObj.read().split()
        fileObj.close()
        self.words = words

