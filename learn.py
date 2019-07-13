"""
    Making my own python functions
    Sorry for the clumsiness

"""



def toUpper(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultString = ''
    for letter in string:
        if letter in alphabet:
            letterIndex = alphabet.index(letter)
            letter = alphabetUpper[letterIndex]
        elif letter in alphabetUpper:
            pass
        else:
            pass
        resultString += letter
    return resultString

def count(string, char):
    total = 0
    for i in string:
        if i == char:
            total += 1

    return total

def startwith(string, substring):
    tempString = ''
    length = len(substring)
    for i in range(length):
        if string[i] == substring[i]:
            tempString += string[i]
    if tempString == substring:
        return 1
    else:
        return 0

# sepstring is the string seperating each item in list
def join(sepstring, joinlist):
    pass



def quadratic(a, b, c):
    import math
    posResult = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
    negResult = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
    math.factorial()
    return (posResult, negResult)


def polynomial(a, b, c, d, factor):
    # My god this is gonna be hard
    # Assume (x + 3) is factor here for ease
    pass

def algebra(string):
    import re
    # 2x^2 + 2x - 34
    regex = re.compile(r'\d\D\^\d|\d\D|\d+|-|\+')
    result = regex.findall(string)
    print(result)
    # Return the powers and the coeffients
    def getCoefficent(result):
        coeffients = []
        first = (result[0][0], result[0][3])
        second = (result[2][0], result[2][3])
        third = result[4]

        return [first, second, third]

    return getCoefficent(result)


quadratic = '3x^4 - 2x^1 - 23'
print(algebra(quadratic))















#
# string = 'Im a very good boi!?'
#
# print(startwith(string, 'Im a very good boi'))
# print(quadratic(1, 23, 25))
# print(toUpper(string))
# print(count(string, 'a'))
