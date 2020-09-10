def is_isogram(string):
    #your code here
    lowstring = string.lower()
    for letter in lowstring:
        findletter = lowstring.count(letter)
        if findletter > 1:
            return False
    
    return True