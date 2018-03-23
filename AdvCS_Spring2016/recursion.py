__author__ = 'becca.elenzil'

def find_palindrome(word):
    print word
    if len(word) < 2:
        return True
    elif word[0].lower() == word[-1].lower():
        return find_palindrome(word[1:-1])
    else:
        return False

print find_palindrome('Hannah')



