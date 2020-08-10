import random
'''
input:  5,4,3,1,2,6
output: 1,2,3,4,4,5,6
'''
def insertion_sort(elms):
    n = len(elms)
    cnt = 0
    for i in range(n):
        j = i
        while (j > 0 and elms[j] < elms[j-1]):
            cnt = cnt + 1
            elms[j-1] , elms[j] = elms[j], elms[j-1]
            j = j - 1
    print(cnt)
    return elms

# assert(insertion_sort([5,4,3,1,2,6]) == [1,2,3,4,5,6])
#inlist = list(range(10000)) 
#insertion_sort(inlist)
#inlist.reverse() # inplace, what does that mean
#insertion_sort(inlist)
#random.shuffle(inlist) # inplace, what does that mean
#insertion_sort(inlist)

'''
'''


def add(s1, s2):
    print("I am running this")
    return s1 + 10

