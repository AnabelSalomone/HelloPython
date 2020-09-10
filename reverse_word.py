def reverse_words(text):
  #go for it
    result = []
    splitted = text.split(" ")
    
    for word in splitted:
        reversed = word[::-1]
        result.append(reversed)
        
    return " ".join(result)        