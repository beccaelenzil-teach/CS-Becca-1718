__author__ = 'becca.elenzil'

def replaceAll(str,oldStr,newStr):
    n = len(oldStr)
    m = len(str)
    k = 0
    newWord = ''
    while k < m:
        if str[k:k+n] == oldStr:
            k += n
            newWord += newStr
        else:
            newWord += str[k]
            k += 1
    return newWord

newWord = replaceAll('to be or not to be','to','2')
print newWord



