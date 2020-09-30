import string

def name_value(my_list):
  count = 0
  rslt = []
  alphabet=string.ascii_lowercase
  
  for str in my_list:
    count +=1 
    letter_count = 0
    for i, letter in enumerate(str):
      letter_count += alphabet.find(letter) + 1
      if i == len(str) -1:
        rslt.append(letter_count * count)
  return rslt