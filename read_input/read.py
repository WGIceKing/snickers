import csv

class readFile:

    def __init__(self, fileName):
        self.fileName = fileName

    def read(self):
        fileObj = open(self.fileName, "r")
        words = fileObj.read().split()
        fileObj.close()
        self.words = words


def main():
    temporary = readFile('example.csv')
    temporary.read()
    print(temporary.words[0], temporary.words[1])

if __name__ == "__main__":
    main()
