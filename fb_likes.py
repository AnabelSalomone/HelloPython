def likes(names):
    #your code here
    if len(names) == 0 : return "no one likes this"
    
    if len(names) == 1 : return "".join(names) + " likes this"
    
    
    if len(names) < 4 : 
        last = names.pop(-1)
        join_str = ", ".join(names)
        return join_str + " and " + last + " like this"
    
    if len(names) >= 4:
        a, b, *rest =  names
        rest_len = len(rest)
        return a + ", " + b + " and " + str(rest_len) + " others like this"
    
    
#BEST solution:
def best_likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)