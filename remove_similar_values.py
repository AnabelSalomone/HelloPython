def array_diff(a, b):
  #your code here
  lista = a
  listb = b
  listc = []
  
  for itema in lista:
    print("item a", itema)
    for itemb in listb:
      print("item b", itemb)
      if len(lista) > len(listb):
        itemb = listb[len(listb)-1]
        if itema == itemb:
          listc.append(itema)

  return lista


a = [1,2,2]
b = [2]

array_diff(a, b)