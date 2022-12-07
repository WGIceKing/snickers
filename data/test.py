
fineName = 'refactored.txt'
fileObj = open(fineName, "r")
words = fileObj.read().split()
fileObj.close()
words = words

print(len(words))
words = [*set(words)]
print(len(words))