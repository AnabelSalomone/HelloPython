def array_diff(a, b):
    #your code here
    lista = a
    listb = b
    
    for itema in lista:
        for itemb in listb:
            if len(lista) > len(listb):
                itemb = listb[len(listb)-1]
                if itema == itemb:
                    lista.remove(itemb)
    return lista