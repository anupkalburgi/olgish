# def merge(A, p, q, r):
#     n1 = q - p + 1  # n1 = 1-0 + 1 = 2
#     n2 = r - q  #n2 = 3 - 1 = 2
#     left = []
#     right = []
#     k = p
#     for _ in range(0, n1):  # Copy all the sorted elements in the left
#        left.append(A[p])
#        p = p + 1
#     for _ in range(0, n2):
#         right.append(A[q+1])
#         q = q + 1
#     i = 0
#     j = 0
#     for _ in range(k , r):
#         if left[i] <= right[j]:
#             A[k] = left[i]
#             i = i + 1
#         else:
#             A[k] = right[j]
#             j = j + 1
#         k = k + 1
#     return A

# a = [1,5,2,7]
# merge(A = a, p=0, q=1, r=3)
# print(a)


def recursive_merge(larray, rarray, acc):
    if len(larray) == 0 and len(rarray) == 0:
        return acc
    elif len(larray) == 0:
        return acc + rarray
    elif len(rarray) == 0:
        return acc + larray
    else:
        lh = larray[0]
        rh = rarray[0]
        if lh <= rh:
            acc = acc + [lh]
            return recursive_merge(larray[1:], rarray, acc)
        else:
            acc = acc + [rh]
            return recursive_merge(larray, rarray[1:], acc)
        

print(recursive_merge([1,5], [2, 7] , [] ))

