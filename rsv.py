# Remove similar values


def array_diff(a, b):
  lista = a
  listb = b
  listc = []

  for x in lista:
    for y in listb:
      if x is not y:
        listc.append(x)

  if len(listb) == 0:
    return lista
    
  return listc

  
  
# Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
# Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
# Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
# Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
# Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")