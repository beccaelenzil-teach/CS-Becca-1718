__author__ = 'becca.elenzil'

def createDictionary(fileName):
    """
    input: filename of file containing string
    output: dictionary, keys = words in text file, entries: a list of words that legally follow

    """
    punctuation = ['.', '!', '?']
    d = {}



    file = open(fileName, 'r')
    words = []
    for line in file:
        words += line.split(" ")

    for i in range(len(words)):
        if words[i][-1:] == "\n":
            words[i] = words[i][0:-1]

    for word in words:
        if word[-1] not in punctuation:
            d[word] = []

    d['$'] = [words[0]]

    for i in range(len(words)-1):
        if words[i][-1] in punctuation:
            d['$'].append(words[i+1][:])
        else:
            d[words[i]].append(words[i+1])




    return words,d

words,d = createDictionary('a.txt')
print d
